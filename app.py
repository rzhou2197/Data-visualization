#!flask/bin/python
from flask import Flask, jsonify,render_template, request,redirect

import numpy as np
import os,sys
import json
import importlib
import csv
from math import *

importlib.reload(sys)
f = open("data/map.json",encoding='UTF-8')
text = f.read()
us_json = json.loads(text)

app = Flask(__name__)


@app.route('/')
def index():
	
	
	 return redirect('/u.json');
	
	
@app.route('/u.json')
def ajson():
	def disp(reader):
		df=[]
		for row in reader:
				df.append(row)
		return df
	with open("data.csv",'r+',encoding='UTF-8') as f:
		reader = csv.reader(f)
		df = disp(reader)
	
	return render_template("index.html",ujson=us_json,df=df)
		
if __name__ == '__main__':
        app.run(debug=True)







'''def disp(reader):
		df=[]
		for row in reader:
				df.append(row)
		return df
	with open("countriesData.csv",'r+') as f:
		reader = csv.reader(f)
		df = disp(reader)
		#us_json=jsonify(us_json)'''



		
'''@app.route('/user', methods=['POST'])
def sendjson():
	CountryName=request.form.get("countryName")
	SeriesName=request.form.get("seriesName")
	fyear=request.form.get("2010year")
	syear=request.form.get("2011year")
	tyear=request.form.get("2012year")
	lyear=request.form.get("2013year")	
	uyear=request.form.get("2014year")
	with open("countriesData.csv",'a+') as f:
		writer = csv.writer(f)
		writer.writerow([CountryName,'NAN',SeriesName,'NAN',fyear,syear,tyear,lyear,uyear])
	f.close()	
	return redirect(('/1'))

@app.route('/<int:page_num>')
def read_csv(page_num):
	restriction = 5
	def disp(reader,page_num=page_num,restriction=restriction):
		df=[]
		for row in reader:
			if (page_num*restriction>=reader.line_num)and(reader.line_num>(page_num-1)*restriction):
				df.append(row)
		return df
	with open("countriesData.csv",'r+') as f:
		row_length = len(f.readlines())
		if(row_length%restriction==0):
			pages=row_length/restriction
		else:
			pages = int(ceil(row_length/restriction))+1
	f.close()
	with open("countriesData.csv",'r+') as f:
		reader = csv.reader(f)
		df = disp(reader,page_num,restriction)
	f.close()
	#print "pages is",pages
	return render_template("index.html",df=df,pages=pages,page_num=page_num)'''