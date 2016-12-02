import solrhandler
from wit import Wit

print(solrhandler.solrcall('Hello'))
def converse(Query):
	access_token = "7MI6KCEAOV24GWYB7TD7RALBDXMANCB3"


	def send(request, response):
	    print(response['text'])
	actions = {
	    'send': send,    
	}

	client = Wit(access_token=access_token, actions=actions)
	data=client.converse(1,Query)
	X=[]
	for key in data['entities'].keys():
	   	X.append(data['entities'][key][0]['value'])
	return X
