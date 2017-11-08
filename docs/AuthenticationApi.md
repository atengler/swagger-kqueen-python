# swagger_client.AuthenticationApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_post**](AuthenticationApi.md#auth_post) | **POST** /auth | 


# **auth_post**
> InlineResponse200 auth_post(credentials)



Authentication URL which returns JWT tokens

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
credentials = swagger_client.Credentials() # Credentials | 

try: 
    api_response = api_instance.auth_post(credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

