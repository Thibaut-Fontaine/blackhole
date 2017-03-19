#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


def getToken():
	data = {
	  'grant_type': 'client_credentials',
	  'client_id': '33c9ac3c0bcfeebde83bfc6d2ba54eb0a0e0ceeb821b864f07ab6db712e86999',
	  'client_secret': 'ffc5da723a36a4f4c8b0339be6d8d882f6a98c37c85afdd5e1bbf970f7d82f56'
	}
	r =  requests.post('https://api.intra.42.fr/oauth/token', data=data)
	token = json.loads(r.text)['access_token']
	return token

def get_all():
	finalier = []
	# finaler = []
	token = getToken()
	headers = {
	    'Authorization': 'Bearer '+token+'',
	}
	j = 0
	# num = 0;
	for i in range(100):
		r = requests.get('https://api.intra.42.fr/v2/users?filter[pool_year]=2016&campus_id=1&page='+str(i), headers=headers)
		if r.text == '[]':
			break
		final = json.loads(r.text)
		for info in final:
			finalier.append(info)
			print str(j) + "-->" + info['id']
			# q = requests.get('https://api.intra.42.fr/v2/users/'+ info['login'] + '/cursus_users', headers=headers)
			# if q.text != '[]':
			# 	trad = json.loads(q.text)
			# 	finaler.append(trad)
				# if len(trad) > 1:
				# 	print trad[0]['level']
				# if trad[0]['level'] > 8.18:
					# num += 1;
			j += 1
	# print 'le total est de :' + str(num)
	return finalier

def get_all_piscinard_petard():
	token = getToken()
	final = []
	headers = {
	    'Authorization': 'Bearer '+token+'',
	}
	with open("piscine.txt", "r") as f:
		tout = json.loads(f.read())
	for user in tout:
		print user['login']
		token = getToken()
		r = requests.get('https://api.intra.42.fr/v2/users/'+str(user["id"]), headers=headers)
		final.append(json.loads(r.text))
	return final

def work_on_piscinard_babar():
	with open("act.txt") as f:
		tout = json.loads(f.read())
	for user in tout:
		if user['pool_month'] != 'march':
			continue
		print user['login'] + " ---> " + str(user['cursus_users'][-1]['level']) + "----> " + str(user['location']).replace("None", "")
	print
	print
	for user in tout:
		if user['pool_month'] != 'march':
			continue
		if user['cursus_users'][-1]['level'] > 0:
			print user['login'] + "-->" + str(user['cursus_users'][-1]['level'])

def make_html_of_piscinard():
	with open("piscine.txt", "r") as f:
		tout = json.loads(f.read())
	final = ""
	for user in tout:
		final += '<img src="https://cdn.intra.42.fr/users/medium_'+user['login']+'.jpg" alt="'+user["login"]+'">\n'
	with open("/var/www/html/piscine.html", "w") as f:
		f.write(final)
if __name__ == "__main__":
	get_all()
#	with open("act.txt", "w") as f:
		# f.write(json.dumps(get_all_piscinard_petard()))
	# work_on_piscinard_babar()
	#make_html_of_piscinard()
