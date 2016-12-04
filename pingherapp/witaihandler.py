import solrhandler
from wit import Wit
import json
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))
def converse(Query):
	access_token = "HUYFSZATE2FRGLETGVWWTCHNSVTXBKDC" 


	def send(request, response):
	    print(response['text'])
	actions = {
	    'send': send,    
	}
	tweet={"tweet_text":"","tweet_url":[]}
	
	client = Wit(access_token=access_token, actions=actions)
	#Query=""
	data=client.converse(1,Query)
	X=""
	for key in data['entities'].keys():
	   	X=X+" "+(data['entities'][key][0]['value'])
	mydict=json.load(open(os.path.join(BASE, "mydict.json")))
	solr=True
	for key_list in mydict.keys():
		flag=True
		for key in data['entities'].keys():
			if str(data['entities'][key][0]['value']).upper() not in str(key_list):
				flag=False
		if flag:
			tweet['tweet_text']=mydict[key_list]
			solr=False
	if len(data['entities'].keys())==0:
		solr=True
		X=Query
	if solr:
		tweet=solrhandler.solrcall(X,data)
	return tweet

