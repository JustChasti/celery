from flask import Flask, request, jsonify
import json
import requests
import config
from src import db


application = Flask(__name__)


@application.route("/")
def hello():
   return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/links/all/", methods=["GET"])
def get_all():
    """Add a new link to base"""
    return jsonify(db.get_all())


@application.route("/links/parse/", methods=["GET"])
def send_urls():
    """Send links to parser"""
    return jsonify(db.get_links())


@application.route("/links/update/", methods=["PUT"])
def get_parse_urls():
    """Get links from parser and update in base"""
    j_request = request.get_json(force=True)
    db.update_link(j_request[0]['url'], j_request[0]['Name'],
                   j_request[0]['Price'], j_request[0]['Art'],
                   j_request[0]['Col_otz'], j_request[1])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@application.route("/links/add/", methods=["POST"])
def get_link():
    """Add a new link to base"""
    j_request = request.json
    db.append_link(j_request['link'])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    application.run()
