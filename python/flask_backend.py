from flask import Flask, jsonify, request, render_template, session, redirect, url_for
import json
import requests
from backend import *

app = Flask(__name__)

@app.route('/mainPage', methods=['GET'])
def mainPage():
    return jsonify(getMainPage())

@app.route('/restaurant', methods=['GET'])
def getRestaurantInformation():
    restaurant = request.args.get('name')
    return jsonify(getRestaurant(restaurant))

app.run(host='0.0.0.0')
