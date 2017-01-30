import os
import sys
import json
import logging

#set up Logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#Pull redirecrt info from Contentful`
def get_redirects():
	# put external dependencies in path
	here = os.path.dirname(os.path.realpath(__file__))
	sys.path.append(os.path.join(here, "./vendored"))
	import contentful

	# get contentful credentials from environment
	contentful_api_id = os.getenv('LIBND_PURL_SVC_ID')
	contentful_api_key = os.getenv('LIBND_PURL_SVC_KEY')
	log.debug("api_id = {}".format(contentful_api_id))
	log.debug("api_key = {}".format(contentful_api_key))

	# read redirect entries from contentful
	# string info form contentful in Unicode- deal with it
	redirects = {}
	client = contentful.Client( contentful_api_id, contentful_api_key)
	entries = client.entries()
	for entry in entries:
		redirects[str(entry.purl_token)] = str(entry.purl_uri)
	return redirects

def redirect(event, context):
	log.debug("received event {}".format(json.dumps(event)))
	redirects = get_redirects()
	log.debug("received redirects {}".format(json.dumps(redirects)))

	statuscode = 302
	headers = {}
	message = 'url has been redirected'

	body = {
        	"message": message,
        	"input": event
	}

	log.debug(event['pathParameters']['code'])
	if event['pathParameters'] == None or event['pathParameters']['code'] == None or redirects.get(event['pathParameters']['code'], None) == None:
		statuscode = 404
		body['message'] = "Redirect Code was not Provided, or was  Not Found"
	else:
		headers['Location'] = redirects[event['pathParameters']['code']]

	response = {
		"statusCode": statuscode,
		"body": json.dumps(body),
		"headers": headers
	}

	return response

