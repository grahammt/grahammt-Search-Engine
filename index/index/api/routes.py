"""Routes for index API."""
import re
import math
import functools
import flask
import index


@index.app.route('/api/v1/', methods=['GET'])
def get_hits():
    """List of services."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)


def score_comp(item1, item2):
    """Compare documents."""
    if item2["score"] > item1["score"]:
        return 1
    if item2["score"] == item1["score"]:
        if item2["docid"] < item1["docid"]:
            return 1
        return -1
    return -1


@index.app.route('/api/v1/hits/', methods=['GET'])
def resolve_query():
    """Send a query response."""
    inverted_index = index.app.config["inverted_index"]
    stop_words = index.app.config['stop_words']
    weight = float(flask.request.args.get('w', None))
    query = flask.request.args.get('q', None)
    query = query.lower()
    query = query.split()

    lock = True
    document_intersection = []
    query_count = {}

    for werd in query:
        word = re.sub(r'[^a-zA-Z0-9]+', '', werd)
        if word in stop_words:
            continue
        if word not in inverted_index:
            context = {
                "hits": []
            }
            return flask.jsonify(**context)
        if lock:
            document_intersection = inverted_index[word]["docs"].keys()
            lock = False
        else:
            previous_set = set(document_intersection)
            new_set = set(inverted_index[word]["docs"].keys())

            document_intersection = list(previous_set & new_set)
        if word not in query_count:
            query_count[word] = 1
        else:
            query_count[word] += 1

    scores = get_scores(
        document_intersection,
        inverted_index,
        query_count,
        weight
    )

    scores.sort(key=functools.cmp_to_key(score_comp))
    context = {
        "hits": scores
    }
    return flask.jsonify(**context)


def get_scores(document_intersection, inverted_index, query_count, weight):
    """Get scores for documents."""
    scores = []
    for document in document_intersection:
        val = 0
        prod = 0
        page_rank = index.app.config["page_rank"][document]
        for word, tfq in query_count.items():
            doc_norm = math.sqrt(
                inverted_index[word]["docs"][document]["docnorm"]
            )
            tfd = inverted_index[word]["docs"][document]["frequency"]
            prod += (inverted_index[word]["idf"] ** 2) * tfq * tfd
            val += (tfq**2)*(inverted_index[word]["idf"]**2)
        weight = float(weight)
        score = weight*page_rank + (1-weight) * prod/(math.sqrt(val)*doc_norm)
        scores.append({"docid": document, "score": score})
    return scores
