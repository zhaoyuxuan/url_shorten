from flask import Flask,render_template,request,redirect,url_for
import requests,os
import sys,hashlib
from pymongo import MongoClient

# DATA = {
#         "url": "https://www.maharsh.net",
#         "_id": "32sd1"
#         }
app = Flask(__name__)
client = MongoClient("mongodb://demo:demo@ds139761.mlab.com:39761/urlshort")
db = client.get_default_database()
urls = db["urls"]

db = client.get_default_database()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten',methods=["POST"])
def shorten():

    link = request.form["website_url"]
    link=link.encode('utf-8')
    hash_object = hashlib.md5(link)
    code=hash_object.hexdigest()[:5]
    DATA={}
    DATA["url"]=link
    DATA["_id"]=code
    urls.insert_one(DATA)
    collection = db.test_collection

    return code

@app.route('/<link>')
def generate(link):
    link = request.form["code"]
    


    return "2"




if __name__ == "__main__":
    app.run(debug=True)
