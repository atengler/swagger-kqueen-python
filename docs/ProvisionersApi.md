# swagger_client.ProvisionersApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provisioners_get**](ProvisionersApi.md#provisioners_get) | **GET** /provisioners | 
[**provisioners_id_delete**](ProvisionersApi.md#provisioners_id_delete) | **DELETE** /provisioners/{id} | 
[**provisioners_id_get**](ProvisionersApi.md#provisioners_id_get) | **GET** /provisioners/{id} | 
[**provisioners_id_patch**](ProvisionersApi.md#provisioners_id_patch) | **PATCH** /provisioners/{id} | 
[**provisioners_post**](ProvisionersApi.md#provisioners_post) | **POST** /provisioners | 


# **provisioners_get**
> list[Provisioner] provisioners_get()



List all Provisioners

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProvisionersApi()

try: 
    api_response = api_instance.provisioners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionersApi->provisioners_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Provisioner]**](Provisioner.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioners_id_delete**
> InlineResponse2001 provisioners_id_delete(id)



Delete target Provisioner

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProvisionersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.provisioners_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionersApi->provisioners_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioners_id_get**
> Provisioner provisioners_id_get(id)



Get information about target Provisioner

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProvisionersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.provisioners_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionersApi->provisioners_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Provisioner**](Provisioner.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioners_id_patch**
> Provisioner provisioners_id_patch(id, body)



Update data of target Provisioner

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProvisionersApi()
id = 'id_example' # str | 
body = swagger_client.Provisioner() # Provisioner | 

try: 
    api_response = api_instance.provisioners_id_patch(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionersApi->provisioners_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Provisioner**](Provisioner.md)|  | 

### Return type

[**Provisioner**](Provisioner.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioners_post**
> Provisioner provisioners_post(body)



Create new Provisioner

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProvisionersApi()
body = swagger_client.Provisioner() # Provisioner | 

try: 
    api_response = api_instance.provisioners_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionersApi->provisioners_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Provisioner**](Provisioner.md)|  | 

### Return type

[**Provisioner**](Provisioner.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

