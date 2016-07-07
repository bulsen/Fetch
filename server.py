# -*- encoding: utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from pymongo import MongoClient
client = MongoClient()

# you can change the database and collection names with
#           db = client.desired_database_name
#           collection = db.desired_collection_name

db = client.fetchdatabase
collection = db.metadata

""" Fetch function """
'''def search(querry):
	ret_elems = []
	ret_elemi = []
	n = 1
	for posts in collection.find({"querry" : querry}):
		"""if not posts["title"] in ret_elems:
			ret_elems.append(posts["title"])"""
		ret_elems.append({'id' : n, 'tit' : posts["filename"]})	
		n +=1
	return ret_elems
'''

def search(querry):
	ret_elems = []
	ret_elemi = []
	n = 1
	for posts in collection.find({"querry" : querry}):
		direc = posts["filename"]
		direc = direc[2:]
		ret_elems.append({'id' : n, 'filename' :posts["filename"], 'page': posts["pagenumber"], 'querry': posts["querry"] })	
		n +=1
	return ret_elems

""" web service """
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)

# fetch's web thing
@app.route('/<que>')
def motor(que):
	# re define
	arg = que
	querry = re.compile(arg ,re.IGNORECASE)
	data =[]
	data = search(querry)
	return render_template("show_enteries.html", data = data)

# adding favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

# 404 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# help page
@app.route("/hjalpington")
def helpington():
	return render_template('/hjalp.html')

@app.route('/hjalpington', methods=['GET','POST'])
def hjalp_form_post():
	if request.method == "POST":
	    return redirect("/%s"%request.form['search'])

# main page
@app.route('/')
def main():
	return render_template("main.html")

@app.route('/', methods=['GET','POST'])
def my_form_post():
	if request.method == "POST":
	    return redirect("/%s"%request.form['search'])

# for slides
"""@app.route("/showme/<dirname>/<number>")
def shigga(dirname,number):
	# file download
	return send_from_directory("svgdude/" + dirname, number+ ".svg")
"""
@app.route("/loco/<dirname>/<number>")
def shuga(dirname,number):
	# file download
	return send_from_directory("svgdude/" + dirname, number+ ".svg")

@app.route("/showme/<dirname>/<number>")
def shigga(dirname,number):
	# file download
	return render_template("slider.html", dirname = dirname, number = number)

@app.route('/meraba')
def contact():
	return render_template("author.html")

if __name__ == '__main__':
	""" this runs on port 80, so... fuck security """
	app.run(host ="0.0.0.0", port=80)





