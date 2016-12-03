import solrhandler
from wit import Wit

def converse(Query):
	access_token = "HUYFSZATE2FRGLETGVWWTCHNSVTXBKDC" 


	def send(request, response):
	    print(response['text'])
	actions = {
	    'send': send,    
	}

	client = Wit(access_token=access_token, actions=actions)
	data=client.converse(1,Query)
	X=""
	for key in data['entities'].keys():
	   	X=X+" "+(data['entities'][key][0]['value'])
	tweet=solrhandler.solrcall(X)
	return tweet
