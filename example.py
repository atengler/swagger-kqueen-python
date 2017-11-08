from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# get auth token
auth_client = swagger_client.AuthenticationApi()
credentials = swagger_client.Credentials(username="admin", password="default") # Credentials |

try:
    api_response = auth_client.auth_post(credentials)
    token = api_response.access_token
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)

# configure authorization header
swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
swagger_client.configuration.api_key['Authorization'] = token

# init resource API
clusters_client = swagger_client.ClustersApi()

try:
    api_response = clusters_client.clusters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
