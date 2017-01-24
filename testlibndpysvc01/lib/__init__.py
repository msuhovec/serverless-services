import json
import os

here = os.path.dirname(os.path.realpath(__file__))

def all_redirects():
	with open(os.path.join(here, '../redirects.json')) as redirect_file:
	        redirects = json.load(redirect_file)
	        return redirects
