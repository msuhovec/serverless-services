import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# this adds the component-level `lib` directory to the Python import path
import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

# import the shared library, now anything in component/lib/__init__.py can be
# referenced as `lib.something`
import lib


def read(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    redirects = lib.all_redirects()

    body = {
        "message": "What, me worry?",
        "input": event['queryStringParameters']
    }

    response = {
        "statusCode": 302,
	"body": json.dumps(body)
    }


    return response
