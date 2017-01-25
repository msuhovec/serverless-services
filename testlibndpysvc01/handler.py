import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# this adds the component-level `liy` directory to the python import path
import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

# import the shared library, now anything in component/lib/__init__.py can be
# referenced as `lib.something`
import lib


def redirect(event, context):
	log.debug("received event {}".format(json.dumps(event)))
	redirects = lib.all_redirects()
	log.debug("received redirects {}".format(json.dumps(redirects)))

	statuscode = 302
	headers = {}
	message = 'url has been redirected'

	body = {
        	"message": message,
        	"input": event['queryStringParameters']
	}

	if body['input'] == None or body['input']['redirect_code'] == None or redirects[body['input']['redirect_code']] == None:
		statuscode = 404
		body['message'] = "Redirect Code was Not Found"
	else:
		headers['Location'] = redirects[event['queryStringParameters']['redirect_code']]['purlUri'] 

	response = {
		"statusCode": statuscode,
		"body": json.dumps(body),
		"headers": headers
	}



	return response
