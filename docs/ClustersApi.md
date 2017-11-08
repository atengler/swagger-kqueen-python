# swagger_client.ClustersApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | 
[**clusters_id_delete**](ClustersApi.md#clusters_id_delete) | **DELETE** /clusters/{id} | 
[**clusters_id_get**](ClustersApi.md#clusters_id_get) | **GET** /clusters/{id} | 
[**clusters_id_kubeconfig_get**](ClustersApi.md#clusters_id_kubeconfig_get) | **GET** /clusters/{id}/kubeconfig | 
[**clusters_id_patch**](ClustersApi.md#clusters_id_patch) | **PATCH** /clusters/{id} | 
[**clusters_id_status_get**](ClustersApi.md#clusters_id_status_get) | **GET** /clusters/{id}/status | 
[**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | 


# **clusters_get**
> list[GetCluster] clusters_get()



List all Clusters

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
api_instance = swagger_client.ClustersApi()

try: 
    api_response = api_instance.clusters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetCluster]**](GetCluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_delete**
> InlineResponse2001 clusters_id_delete(id)



Delete target Cluster

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
api_instance = swagger_client.ClustersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.clusters_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_id_delete: %s\n" % e)
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

# **clusters_id_get**
> GetCluster clusters_id_get(id)



Get information about target Cluster

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
api_instance = swagger_client.ClustersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.clusters_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetCluster**](GetCluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_kubeconfig_get**
> object clusters_id_kubeconfig_get(id)



Get Kubeconfig from target Cluster

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
api_instance = swagger_client.ClustersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.clusters_id_kubeconfig_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_id_kubeconfig_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_patch**
> GetCluster clusters_id_patch(id, body)



Update data of target Cluster

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
api_instance = swagger_client.ClustersApi()
id = 'id_example' # str | 
body = swagger_client.PostCluster() # PostCluster | 

try: 
    api_response = api_instance.clusters_id_patch(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**PostCluster**](PostCluster.md)|  | 

### Return type

[**GetCluster**](GetCluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_status_get**
> ClusterStatus clusters_id_status_get(id)



Get information about target Cluster directly from KubeAPI

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
api_instance = swagger_client.ClustersApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.clusters_id_status_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_post**
> GetCluster clusters_post(body)



Create new Cluster

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
api_instance = swagger_client.ClustersApi()
body = swagger_client.PostCluster() # PostCluster | 

try: 
    api_response = api_instance.clusters_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCluster**](PostCluster.md)|  | 

### Return type

[**GetCluster**](GetCluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

