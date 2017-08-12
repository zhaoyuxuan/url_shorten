from flask import Flask,render_template,request,redirect,url_for
import requests,os
import sys,hashlib,validators
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://demo:demo@ds139761.mlab.com:39761/urlshort")
db = client.get_default_database()
urls = db["urls"]

db = client.get_default_database()
link=''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2736f')
def test():
    return '2736f'

@app.route('/shorten',methods=["POST"])
def shorten():
    link = request.form["website_url"]
    is_valid=validators.url(link,public=False)
    if (not is_valid):
        return "not a website"
    else :
        link=link.encode('utf-8')
        hash_object = hashlib.md5(link)
        code=hash_object.hexdigest()[:5]
    try:
        website=urls.find_one({"_id":code})['url'].decode('ascii')
    except:
        DATA={}
        DATA["url"]=link
        DATA["_id"]=code
        urls.insert_one(DATA)
    cur.close()
    return code

@app.route('/<link>')
def generate(link):
    #  token=request.form["code"]
    website=urls.find_one({"_id":link})['url'].decode('ascii')
    # print(website)
    return redirect(website, code=302)
if __name__ == "__main__":
    app.run(debug=True)
