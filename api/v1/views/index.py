#!/usr/bin/python3
""" index file for view"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """ Return status of the request """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """
    endpoint retrieves the number of each object by type
    """
    objects = {"amenities": storage.count("Amenity"),
               "cities": storage.count("City"),
               "places": storage.count("Place"),
               "reviews": storage.count("Review"),
               "states": storage.count("State"),
               "users": storage.count("User")}
    return jsonify(objects)
