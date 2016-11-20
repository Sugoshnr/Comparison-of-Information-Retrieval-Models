# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""
import os
import json
# if you are using python 3, you should 
#import urllib.request 
import urllib,urllib2
path="/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/Project_3_data/trec_eval.9.0/"
os.system("rm "+path+"BM25.txt")
os.system("rm "+path+"VSM.txt")
os.system("rm "+path+"DFR.txt")
os.system("/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/bin/solr restart -s /media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/twitter/solr")
os.system("/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/bin/post -c BM25 /media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/train.json")
os.system("/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/bin/post -c VSM /media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/train.json")
os.system("/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/bin/post -c DFR /media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/solr-6.2.1/train.json")

f=open("test_query.txt","r");
for line in f:
	X=[]
	X.append(line[0:3])
	X.append(line[4:])
	for core in ["BM25", "DFR", "VSM"]:
		if(X[0]=="004"):
			query_text=X[1]
		else:
			query_text=X[1]
		#query_text="Russia's intervention in Syria"
		query_text=urllib.quote(query_text)
		# change the url according to your own koding username and query
		inurl = "http://localhost:8983/solr/"+core+"/select?q="+query_text+"&fl=id%2Cscore&wt=json&indent=true&rows=20"
		outfn = str(int(X[0][2]))+".txt"
		#outfn=core+".txt"
		# change query id and IRModel name accordingly
		qid = X[0]
		IRModel=core
		if core == "BM25":
			IRModel="default"	
		outf = open("/media/sugosh/New Volume/CSE535-Information_Retrieval/Project_3/Project_3_data/"+core+"/"+outfn, 'a+')
		data = urllib2.urlopen(inurl)
		# if you're using python 3, you should use
		# data = urllib.request.urlopen(inurl)

		docs = json.load(data)['response']['docs']
		# the ranking should start from 1 and increase
		rank = 1
		for doc in docs:
		    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
		    rank += 1
		outf.close()
#os.system("/media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/Project_3_data/trec_eval.9.0/trec_eval -q -c -M 1000 -m map qrel.txt /media/sugosh/New\ Volume/CSE535-Information_Retrieval/Project_3/Project_3_data/trec_eval.9.0/BM25.txt")
