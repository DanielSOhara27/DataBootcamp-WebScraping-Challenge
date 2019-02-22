from flask import Flask, render_template, redirect
from pymongo import MongoClient

import scrape.scrape_mars as mars

app = Flask(__name__)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    client = MongoClient(port=27017)
    db = client.mars
    myData = db.mars_data.find_one()
    return render_template("index.html", mars_data=myData)


@app.route("/scrape")
def scraper():
    data = mars.scrape()

    client = MongoClient(port=27017)
    db = client.mars
    db.mars_data.update({}, data, upsert=True)

    return redirect("/", code=302)

@app.route("/test")
def test():
    client = MongoClient(port=27017)
    db = client.mars
    myData = db.mars_data.find_one()
    print(type(myData['usgs']))
    print(myData['usgs'][0])

    return myData['usgs']


if __name__ == "__main__":
    app.run(debug=True)

