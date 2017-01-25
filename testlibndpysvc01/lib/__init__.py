import json
import os


here = os.path.dirname(os.path.realpath(__file__))

def all_redirects():
	with open(os.path.join(here, '../redirects.json')) as redirect_file:
	        raw_data = json.load(redirect_file)
		redirects = {}
		for item in raw_data['items']:
			redirects[item['fields']['purlToken']] = item['fields']
	        return redirects
