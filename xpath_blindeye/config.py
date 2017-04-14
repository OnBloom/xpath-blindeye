#
# These defaults should be fine
ROOT_PATH = '/*[1]'
MAX_NODE_NAME_LENGTH = 100
# Setting to true will power through matching errors
SOFT_CHARSET_FAIL = True
INJECTION_FORMAT = "' and {} and 'a'='a"

#
#
# Common Configuration
# The settings below work with the included flask server and example.xml
#
# Max number of processes spawned
MAX_WORKERS = 5
# Full URL
URL = "http://localhost:5000/"
# PARAMETERS is used for both GET and POST requests.
# You must provide a parameter that results in a TRUE response. Add {inject} to the end of the value
PARAMETERS = {'name': 'Cowslip{inject}'}
# The name of the parameter to inject
INJECT_PARAMETER_NAME = "name"
# GET or POST
HTTP_MODE = "GET"
# A string only present on a TRUE response to search for
SUCCESS = "true"
