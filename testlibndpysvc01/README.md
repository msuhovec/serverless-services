# Serverless Python Purl Prototype

Python Purl Prototype Using Serverless.com Framework

##Getting Started:

Requirements:

* Contentful Python Client - https://github.com/contentful/contentful.py
* Serverless Client for Your Platform - https://serverless.com/framework/docs/providers/aws/guide/installation/
* AWS IAM role 'serverless' for use in running serverless client - https://serverless.com/framework/docs/providers/aws/guide/credentials/
* environment variables LIBND_PURL_SVC_ID and LIBND_PURL_SVC_KEY, set to the values of the Contentful Space and Token containing the Purl Mappings 

Installation:

```console
$ serverless install --url http://github.com/msuhovec/serverless-services
$ serverless deploy
```
To View Logs:

```console
$ serverless logs -f redirect
```
