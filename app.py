from sys import argv
import bottle
import urllib.request
import json


@bottle.route("/")
def index():
    return """
    <h1>Verkefni 4</h1>
    <a href="/1">4.1 - Local JSON</a>
    <br>
    <a href="/2">4.2 - JSON API</a>
    """


@bottle.route("/static/<filename:path>")
def static_file(filename):
    return bottle.static_file(filename, root="static")


# 4.1 - Local JSON file
@bottle.route("/1")
def index_a():
    return bottle.template("index_1.tpl")


# 4.2 - JSON API
# Read exchange rate from apis.is
with urllib.request.urlopen("http://apis.is/currency/lb") as url:
    e_rate = json.loads(url.read())


@bottle.route("/2")
def index_b():
    return bottle.template("index_2.tpl", e_rate=e_rate)


@bottle.error(404)
def error404(error):
    return "<h1>Error 404: Page not found.</h1>"


bottle.run(host="0.0.0.0", port=argv[1], reloader=True, debug=True)
