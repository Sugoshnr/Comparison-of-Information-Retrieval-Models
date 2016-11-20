# -*- coding: utf-8 -*-
import json
import io
import urllib,urllib2

f=open("qrel.txt","r")
o=open("rel.txt","w")
for line in f:
	X=line.split()
	if(X[3]!="-1"):
		o.write(X[0]+" "+X[2]+" "+X[3]+"\n")
		inurl = "http://localhost:8983/solr/BM25/select?q="+X[2]+"&wt=json"
		data = urllib2.urlopen(inurl)
		docs = json.load(data)['response']['docs']
		if docs[0]['text_en'].encode('utf-8')!="":
			o.write(docs[0]['text_en'].encode('utf-8')+"\n")
		elif docs[0]['text_de'].encode('utf-8')!="":
			o.write(docs[0]['text_de'].encode('utf-8')+"\n")			
		elif docs[0]['text_ru'].encode('utf-8')!="":
			o.write(docs[0]['text_ru'].encode('utf-8')+"\n")


f.close()
o.close()



