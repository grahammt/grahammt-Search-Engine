"""Search engine package initializer."""
from pathlib import Path
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

inverted_index = {}
file = open("index/index/inverted_index.txt", "r")


for line in file:
    tup = line.split()
    inverted_index[tup[0]] = {}
    inverted_index[tup[0]]["idf"] = float(tup[1])
    inverted_index[tup[0]]["docs"] = {}
    i = 2
    while i < len(tup):
        docid = int(tup[i])
        freq = int(tup[i+1])
        docnorm = float(tup[i+2])
        inverted_index[tup[0]]["docs"][docid] = {}
        inverted_index[tup[0]]["docs"][docid]["frequency"] = int(freq)
        inverted_index[tup[0]]["docs"][docid]["docnorm"] = float(docnorm)
        i += 3

app.config["inverted_index"] = inverted_index

stop_words = open('index/index/stopwords.txt', 'r').read().split("\n")

app.config["stop_words"] = stop_words

page_rank_file = open('index/index/pagerank.out', 'r')

page_rank = {}

for line in page_rank_file:
    tup = line.split(',')
    page_rank[int(tup[0])] = float(tup[1])
app.config["page_rank"] = page_rank

# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import index.api  # noqa: E402  pylint: disable=wrong-import-position
