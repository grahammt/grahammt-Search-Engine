"""Routes for search GUI."""
import flask
import requests
import search


@search.app.route('/', methods=['GET'])
def search_gui():
    """Display a search GUI."""
    query = flask.request.args.get("q", None)
    weight = flask.request.args.get("w", None)
    documents = []
    if query is None and weight is None:
        context = {
            "documents": documents,
            "len": len(documents)
        }
        return flask.render_template("index.html", **context)

    par = {"q": query, "w": weight}
    req = requests.get(url=search.app.config["INDEX_API_URL"], params=par)

    json_data = req.json()

    hits = json_data["hits"]

    docids = [doc["docid"] for doc in hits]
    connection = search.model.get_db()
    i = 0
    for docid in docids:
        cur = connection.execute(
            "SELECT * FROM DOCUMENTS WHERE docid=?",
            (docid, )
        )
        cur = cur.fetchall()
        cur = list(cur)
        documents.append(cur[0])
        i += 1
        if i == 10:
            break
    context = {
        "documents": documents,
        "len": len(documents)
    }
    return flask.render_template("index.html", **context)
