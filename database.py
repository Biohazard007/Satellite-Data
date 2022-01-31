from flask import Flask, request, url_for
from flask_pymongo import PyMongo

ap = Flask(__name__)
app. config['MONGO_URI'] =