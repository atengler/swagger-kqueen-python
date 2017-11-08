# swagger-client
A simple API to interact with Kubernetes clusters

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.8
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_post**](docs/AuthenticationApi.md#auth_post) | **POST** /auth | 
*ClustersApi* | [**clusters_get**](docs/ClustersApi.md#clusters_get) | **GET** /clusters | 
*ClustersApi* | [**clusters_id_delete**](docs/ClustersApi.md#clusters_id_delete) | **DELETE** /clusters/{id} | 
*ClustersApi* | [**clusters_id_get**](docs/ClustersApi.md#clusters_id_get) | **GET** /clusters/{id} | 
*ClustersApi* | [**clusters_id_kubeconfig_get**](docs/ClustersApi.md#clusters_id_kubeconfig_get) | **GET** /clusters/{id}/kubeconfig | 
*ClustersApi* | [**clusters_id_patch**](docs/ClustersApi.md#clusters_id_patch) | **PATCH** /clusters/{id} | 
*ClustersApi* | [**clusters_id_status_get**](docs/ClustersApi.md#clusters_id_status_get) | **GET** /clusters/{id}/status | 
*ClustersApi* | [**clusters_post**](docs/ClustersApi.md#clusters_post) | **POST** /clusters | 
*OrganizationsApi* | [**organizations_get**](docs/OrganizationsApi.md#organizations_get) | **GET** /organizations | 
*OrganizationsApi* | [**organizations_id_delete**](docs/OrganizationsApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | 
*OrganizationsApi* | [**organizations_id_get**](docs/OrganizationsApi.md#organizations_id_get) | **GET** /organizations/{id} | 
*OrganizationsApi* | [**organizations_id_patch**](docs/OrganizationsApi.md#organizations_id_patch) | **PATCH** /organizations/{id} | 
*OrganizationsApi* | [**organizations_post**](docs/OrganizationsApi.md#organizations_post) | **POST** /organizations | 
*ProvisionersApi* | [**provisioners_get**](docs/ProvisionersApi.md#provisioners_get) | **GET** /provisioners | 
*ProvisionersApi* | [**provisioners_id_delete**](docs/ProvisionersApi.md#provisioners_id_delete) | **DELETE** /provisioners/{id} | 
*ProvisionersApi* | [**provisioners_id_get**](docs/ProvisionersApi.md#provisioners_id_get) | **GET** /provisioners/{id} | 
*ProvisionersApi* | [**provisioners_id_patch**](docs/ProvisionersApi.md#provisioners_id_patch) | **PATCH** /provisioners/{id} | 
*ProvisionersApi* | [**provisioners_post**](docs/ProvisionersApi.md#provisioners_post) | **POST** /provisioners | 
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | 
*UsersApi* | [**users_id_delete**](docs/UsersApi.md#users_id_delete) | **DELETE** /users/{id} | 
*UsersApi* | [**users_id_get**](docs/UsersApi.md#users_id_get) | **GET** /users/{id} | 
*UsersApi* | [**users_id_patch**](docs/UsersApi.md#users_id_patch) | **PATCH** /users/{id} | 
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | 


## Documentation For Models

 - [Addon](docs/Addon.md)
 - [ClusterStatus](docs/ClusterStatus.md)
 - [Credentials](docs/Credentials.md)
 - [GetCluster](docs/GetCluster.md)
 - [GetUser](docs/GetUser.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [IoK8sApiAppsV1Deployment](docs/IoK8sApiAppsV1Deployment.md)
 - [IoK8sApiAppsV1DeploymentCondition](docs/IoK8sApiAppsV1DeploymentCondition.md)
 - [IoK8sApiAppsV1DeploymentList](docs/IoK8sApiAppsV1DeploymentList.md)
 - [IoK8sApiAppsV1DeploymentSpec](docs/IoK8sApiAppsV1DeploymentSpec.md)
 - [IoK8sApiAppsV1DeploymentStatus](docs/IoK8sApiAppsV1DeploymentStatus.md)
 - [IoK8sApiAppsV1DeploymentStrategy](docs/IoK8sApiAppsV1DeploymentStrategy.md)
 - [IoK8sApiAppsV1ReplicaSet](docs/IoK8sApiAppsV1ReplicaSet.md)
 - [IoK8sApiAppsV1ReplicaSetCondition](docs/IoK8sApiAppsV1ReplicaSetCondition.md)
 - [IoK8sApiAppsV1ReplicaSetList](docs/IoK8sApiAppsV1ReplicaSetList.md)
 - [IoK8sApiAppsV1ReplicaSetSpec](docs/IoK8sApiAppsV1ReplicaSetSpec.md)
 - [IoK8sApiAppsV1ReplicaSetStatus](docs/IoK8sApiAppsV1ReplicaSetStatus.md)
 - [IoK8sApiAppsV1RollingUpdateDeployment](docs/IoK8sApiAppsV1RollingUpdateDeployment.md)
 - [IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource](docs/IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource.md)
 - [IoK8sApiCoreV1Affinity](docs/IoK8sApiCoreV1Affinity.md)
 - [IoK8sApiCoreV1AttachedVolume](docs/IoK8sApiCoreV1AttachedVolume.md)
 - [IoK8sApiCoreV1AzureDiskVolumeSource](docs/IoK8sApiCoreV1AzureDiskVolumeSource.md)
 - [IoK8sApiCoreV1AzureFilePersistentVolumeSource](docs/IoK8sApiCoreV1AzureFilePersistentVolumeSource.md)
 - [IoK8sApiCoreV1AzureFileVolumeSource](docs/IoK8sApiCoreV1AzureFileVolumeSource.md)
 - [IoK8sApiCoreV1Capabilities](docs/IoK8sApiCoreV1Capabilities.md)
 - [IoK8sApiCoreV1CephFSPersistentVolumeSource](docs/IoK8sApiCoreV1CephFSPersistentVolumeSource.md)
 - [IoK8sApiCoreV1CephFSVolumeSource](docs/IoK8sApiCoreV1CephFSVolumeSource.md)
 - [IoK8sApiCoreV1CinderVolumeSource](docs/IoK8sApiCoreV1CinderVolumeSource.md)
 - [IoK8sApiCoreV1ClientIPConfig](docs/IoK8sApiCoreV1ClientIPConfig.md)
 - [IoK8sApiCoreV1ConfigMapEnvSource](docs/IoK8sApiCoreV1ConfigMapEnvSource.md)
 - [IoK8sApiCoreV1ConfigMapKeySelector](docs/IoK8sApiCoreV1ConfigMapKeySelector.md)
 - [IoK8sApiCoreV1ConfigMapProjection](docs/IoK8sApiCoreV1ConfigMapProjection.md)
 - [IoK8sApiCoreV1ConfigMapVolumeSource](docs/IoK8sApiCoreV1ConfigMapVolumeSource.md)
 - [IoK8sApiCoreV1Container](docs/IoK8sApiCoreV1Container.md)
 - [IoK8sApiCoreV1ContainerImage](docs/IoK8sApiCoreV1ContainerImage.md)
 - [IoK8sApiCoreV1ContainerPort](docs/IoK8sApiCoreV1ContainerPort.md)
 - [IoK8sApiCoreV1ContainerState](docs/IoK8sApiCoreV1ContainerState.md)
 - [IoK8sApiCoreV1ContainerStateRunning](docs/IoK8sApiCoreV1ContainerStateRunning.md)
 - [IoK8sApiCoreV1ContainerStateTerminated](docs/IoK8sApiCoreV1ContainerStateTerminated.md)
 - [IoK8sApiCoreV1ContainerStateWaiting](docs/IoK8sApiCoreV1ContainerStateWaiting.md)
 - [IoK8sApiCoreV1ContainerStatus](docs/IoK8sApiCoreV1ContainerStatus.md)
 - [IoK8sApiCoreV1DaemonEndpoint](docs/IoK8sApiCoreV1DaemonEndpoint.md)
 - [IoK8sApiCoreV1DownwardAPIProjection](docs/IoK8sApiCoreV1DownwardAPIProjection.md)
 - [IoK8sApiCoreV1DownwardAPIVolumeFile](docs/IoK8sApiCoreV1DownwardAPIVolumeFile.md)
 - [IoK8sApiCoreV1DownwardAPIVolumeSource](docs/IoK8sApiCoreV1DownwardAPIVolumeSource.md)
 - [IoK8sApiCoreV1EmptyDirVolumeSource](docs/IoK8sApiCoreV1EmptyDirVolumeSource.md)
 - [IoK8sApiCoreV1EnvFromSource](docs/IoK8sApiCoreV1EnvFromSource.md)
 - [IoK8sApiCoreV1EnvVar](docs/IoK8sApiCoreV1EnvVar.md)
 - [IoK8sApiCoreV1EnvVarSource](docs/IoK8sApiCoreV1EnvVarSource.md)
 - [IoK8sApiCoreV1ExecAction](docs/IoK8sApiCoreV1ExecAction.md)
 - [IoK8sApiCoreV1FCVolumeSource](docs/IoK8sApiCoreV1FCVolumeSource.md)
 - [IoK8sApiCoreV1FlexVolumeSource](docs/IoK8sApiCoreV1FlexVolumeSource.md)
 - [IoK8sApiCoreV1FlockerVolumeSource](docs/IoK8sApiCoreV1FlockerVolumeSource.md)
 - [IoK8sApiCoreV1GCEPersistentDiskVolumeSource](docs/IoK8sApiCoreV1GCEPersistentDiskVolumeSource.md)
 - [IoK8sApiCoreV1GitRepoVolumeSource](docs/IoK8sApiCoreV1GitRepoVolumeSource.md)
 - [IoK8sApiCoreV1GlusterfsVolumeSource](docs/IoK8sApiCoreV1GlusterfsVolumeSource.md)
 - [IoK8sApiCoreV1HTTPGetAction](docs/IoK8sApiCoreV1HTTPGetAction.md)
 - [IoK8sApiCoreV1HTTPHeader](docs/IoK8sApiCoreV1HTTPHeader.md)
 - [IoK8sApiCoreV1Handler](docs/IoK8sApiCoreV1Handler.md)
 - [IoK8sApiCoreV1HostAlias](docs/IoK8sApiCoreV1HostAlias.md)
 - [IoK8sApiCoreV1HostPathVolumeSource](docs/IoK8sApiCoreV1HostPathVolumeSource.md)
 - [IoK8sApiCoreV1ISCSIVolumeSource](docs/IoK8sApiCoreV1ISCSIVolumeSource.md)
 - [IoK8sApiCoreV1KeyToPath](docs/IoK8sApiCoreV1KeyToPath.md)
 - [IoK8sApiCoreV1Lifecycle](docs/IoK8sApiCoreV1Lifecycle.md)
 - [IoK8sApiCoreV1LoadBalancerIngress](docs/IoK8sApiCoreV1LoadBalancerIngress.md)
 - [IoK8sApiCoreV1LoadBalancerStatus](docs/IoK8sApiCoreV1LoadBalancerStatus.md)
 - [IoK8sApiCoreV1LocalObjectReference](docs/IoK8sApiCoreV1LocalObjectReference.md)
 - [IoK8sApiCoreV1LocalVolumeSource](docs/IoK8sApiCoreV1LocalVolumeSource.md)
 - [IoK8sApiCoreV1NFSVolumeSource](docs/IoK8sApiCoreV1NFSVolumeSource.md)
 - [IoK8sApiCoreV1Node](docs/IoK8sApiCoreV1Node.md)
 - [IoK8sApiCoreV1NodeAddress](docs/IoK8sApiCoreV1NodeAddress.md)
 - [IoK8sApiCoreV1NodeAffinity](docs/IoK8sApiCoreV1NodeAffinity.md)
 - [IoK8sApiCoreV1NodeCondition](docs/IoK8sApiCoreV1NodeCondition.md)
 - [IoK8sApiCoreV1NodeConfigSource](docs/IoK8sApiCoreV1NodeConfigSource.md)
 - [IoK8sApiCoreV1NodeDaemonEndpoints](docs/IoK8sApiCoreV1NodeDaemonEndpoints.md)
 - [IoK8sApiCoreV1NodeList](docs/IoK8sApiCoreV1NodeList.md)
 - [IoK8sApiCoreV1NodeSelector](docs/IoK8sApiCoreV1NodeSelector.md)
 - [IoK8sApiCoreV1NodeSelectorRequirement](docs/IoK8sApiCoreV1NodeSelectorRequirement.md)
 - [IoK8sApiCoreV1NodeSelectorTerm](docs/IoK8sApiCoreV1NodeSelectorTerm.md)
 - [IoK8sApiCoreV1NodeSpec](docs/IoK8sApiCoreV1NodeSpec.md)
 - [IoK8sApiCoreV1NodeStatus](docs/IoK8sApiCoreV1NodeStatus.md)
 - [IoK8sApiCoreV1NodeSystemInfo](docs/IoK8sApiCoreV1NodeSystemInfo.md)
 - [IoK8sApiCoreV1ObjectFieldSelector](docs/IoK8sApiCoreV1ObjectFieldSelector.md)
 - [IoK8sApiCoreV1ObjectReference](docs/IoK8sApiCoreV1ObjectReference.md)
 - [IoK8sApiCoreV1PersistentVolume](docs/IoK8sApiCoreV1PersistentVolume.md)
 - [IoK8sApiCoreV1PersistentVolumeClaim](docs/IoK8sApiCoreV1PersistentVolumeClaim.md)
 - [IoK8sApiCoreV1PersistentVolumeClaimCondition](docs/IoK8sApiCoreV1PersistentVolumeClaimCondition.md)
 - [IoK8sApiCoreV1PersistentVolumeClaimList](docs/IoK8sApiCoreV1PersistentVolumeClaimList.md)
 - [IoK8sApiCoreV1PersistentVolumeClaimSpec](docs/IoK8sApiCoreV1PersistentVolumeClaimSpec.md)
 - [IoK8sApiCoreV1PersistentVolumeClaimStatus](docs/IoK8sApiCoreV1PersistentVolumeClaimStatus.md)
 - [IoK8sApiCoreV1PersistentVolumeClaimVolumeSource](docs/IoK8sApiCoreV1PersistentVolumeClaimVolumeSource.md)
 - [IoK8sApiCoreV1PersistentVolumeList](docs/IoK8sApiCoreV1PersistentVolumeList.md)
 - [IoK8sApiCoreV1PersistentVolumeSpec](docs/IoK8sApiCoreV1PersistentVolumeSpec.md)
 - [IoK8sApiCoreV1PersistentVolumeStatus](docs/IoK8sApiCoreV1PersistentVolumeStatus.md)
 - [IoK8sApiCoreV1PhotonPersistentDiskVolumeSource](docs/IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.md)
 - [IoK8sApiCoreV1Pod](docs/IoK8sApiCoreV1Pod.md)
 - [IoK8sApiCoreV1PodAffinity](docs/IoK8sApiCoreV1PodAffinity.md)
 - [IoK8sApiCoreV1PodAffinityTerm](docs/IoK8sApiCoreV1PodAffinityTerm.md)
 - [IoK8sApiCoreV1PodAntiAffinity](docs/IoK8sApiCoreV1PodAntiAffinity.md)
 - [IoK8sApiCoreV1PodCondition](docs/IoK8sApiCoreV1PodCondition.md)
 - [IoK8sApiCoreV1PodList](docs/IoK8sApiCoreV1PodList.md)
 - [IoK8sApiCoreV1PodSecurityContext](docs/IoK8sApiCoreV1PodSecurityContext.md)
 - [IoK8sApiCoreV1PodSpec](docs/IoK8sApiCoreV1PodSpec.md)
 - [IoK8sApiCoreV1PodStatus](docs/IoK8sApiCoreV1PodStatus.md)
 - [IoK8sApiCoreV1PodTemplateSpec](docs/IoK8sApiCoreV1PodTemplateSpec.md)
 - [IoK8sApiCoreV1PortworxVolumeSource](docs/IoK8sApiCoreV1PortworxVolumeSource.md)
 - [IoK8sApiCoreV1PreferredSchedulingTerm](docs/IoK8sApiCoreV1PreferredSchedulingTerm.md)
 - [IoK8sApiCoreV1Probe](docs/IoK8sApiCoreV1Probe.md)
 - [IoK8sApiCoreV1ProjectedVolumeSource](docs/IoK8sApiCoreV1ProjectedVolumeSource.md)
 - [IoK8sApiCoreV1QuobyteVolumeSource](docs/IoK8sApiCoreV1QuobyteVolumeSource.md)
 - [IoK8sApiCoreV1RBDPersistentVolumeSource](docs/IoK8sApiCoreV1RBDPersistentVolumeSource.md)
 - [IoK8sApiCoreV1RBDVolumeSource](docs/IoK8sApiCoreV1RBDVolumeSource.md)
 - [IoK8sApiCoreV1ResourceFieldSelector](docs/IoK8sApiCoreV1ResourceFieldSelector.md)
 - [IoK8sApiCoreV1ResourceRequirements](docs/IoK8sApiCoreV1ResourceRequirements.md)
 - [IoK8sApiCoreV1SELinuxOptions](docs/IoK8sApiCoreV1SELinuxOptions.md)
 - [IoK8sApiCoreV1ScaleIOPersistentVolumeSource](docs/IoK8sApiCoreV1ScaleIOPersistentVolumeSource.md)
 - [IoK8sApiCoreV1ScaleIOVolumeSource](docs/IoK8sApiCoreV1ScaleIOVolumeSource.md)
 - [IoK8sApiCoreV1SecretEnvSource](docs/IoK8sApiCoreV1SecretEnvSource.md)
 - [IoK8sApiCoreV1SecretKeySelector](docs/IoK8sApiCoreV1SecretKeySelector.md)
 - [IoK8sApiCoreV1SecretProjection](docs/IoK8sApiCoreV1SecretProjection.md)
 - [IoK8sApiCoreV1SecretReference](docs/IoK8sApiCoreV1SecretReference.md)
 - [IoK8sApiCoreV1SecretVolumeSource](docs/IoK8sApiCoreV1SecretVolumeSource.md)
 - [IoK8sApiCoreV1SecurityContext](docs/IoK8sApiCoreV1SecurityContext.md)
 - [IoK8sApiCoreV1Service](docs/IoK8sApiCoreV1Service.md)
 - [IoK8sApiCoreV1ServiceList](docs/IoK8sApiCoreV1ServiceList.md)
 - [IoK8sApiCoreV1ServicePort](docs/IoK8sApiCoreV1ServicePort.md)
 - [IoK8sApiCoreV1ServiceSpec](docs/IoK8sApiCoreV1ServiceSpec.md)
 - [IoK8sApiCoreV1ServiceStatus](docs/IoK8sApiCoreV1ServiceStatus.md)
 - [IoK8sApiCoreV1SessionAffinityConfig](docs/IoK8sApiCoreV1SessionAffinityConfig.md)
 - [IoK8sApiCoreV1StorageOSPersistentVolumeSource](docs/IoK8sApiCoreV1StorageOSPersistentVolumeSource.md)
 - [IoK8sApiCoreV1StorageOSVolumeSource](docs/IoK8sApiCoreV1StorageOSVolumeSource.md)
 - [IoK8sApiCoreV1TCPSocketAction](docs/IoK8sApiCoreV1TCPSocketAction.md)
 - [IoK8sApiCoreV1Taint](docs/IoK8sApiCoreV1Taint.md)
 - [IoK8sApiCoreV1Toleration](docs/IoK8sApiCoreV1Toleration.md)
 - [IoK8sApiCoreV1Volume](docs/IoK8sApiCoreV1Volume.md)
 - [IoK8sApiCoreV1VolumeMount](docs/IoK8sApiCoreV1VolumeMount.md)
 - [IoK8sApiCoreV1VolumeProjection](docs/IoK8sApiCoreV1VolumeProjection.md)
 - [IoK8sApiCoreV1VsphereVirtualDiskVolumeSource](docs/IoK8sApiCoreV1VsphereVirtualDiskVolumeSource.md)
 - [IoK8sApiCoreV1WeightedPodAffinityTerm](docs/IoK8sApiCoreV1WeightedPodAffinityTerm.md)
 - [IoK8sApimachineryPkgApiResourceQuantity](docs/IoK8sApimachineryPkgApiResourceQuantity.md)
 - [IoK8sApimachineryPkgApisMetaV1Initializer](docs/IoK8sApimachineryPkgApisMetaV1Initializer.md)
 - [IoK8sApimachineryPkgApisMetaV1Initializers](docs/IoK8sApimachineryPkgApisMetaV1Initializers.md)
 - [IoK8sApimachineryPkgApisMetaV1LabelSelector](docs/IoK8sApimachineryPkgApisMetaV1LabelSelector.md)
 - [IoK8sApimachineryPkgApisMetaV1LabelSelectorRequirement](docs/IoK8sApimachineryPkgApisMetaV1LabelSelectorRequirement.md)
 - [IoK8sApimachineryPkgApisMetaV1ListMeta](docs/IoK8sApimachineryPkgApisMetaV1ListMeta.md)
 - [IoK8sApimachineryPkgApisMetaV1ObjectMeta](docs/IoK8sApimachineryPkgApisMetaV1ObjectMeta.md)
 - [IoK8sApimachineryPkgApisMetaV1OwnerReference](docs/IoK8sApimachineryPkgApisMetaV1OwnerReference.md)
 - [IoK8sApimachineryPkgApisMetaV1Status](docs/IoK8sApimachineryPkgApisMetaV1Status.md)
 - [IoK8sApimachineryPkgApisMetaV1StatusCause](docs/IoK8sApimachineryPkgApisMetaV1StatusCause.md)
 - [IoK8sApimachineryPkgApisMetaV1StatusDetails](docs/IoK8sApimachineryPkgApisMetaV1StatusDetails.md)
 - [IoK8sApimachineryPkgApisMetaV1Time](docs/IoK8sApimachineryPkgApisMetaV1Time.md)
 - [IoK8sApimachineryPkgUtilIntstrIntOrString](docs/IoK8sApimachineryPkgUtilIntstrIntOrString.md)
 - [IoK8sApimachineryPkgVersionInfo](docs/IoK8sApimachineryPkgVersionInfo.md)
 - [NodePod](docs/NodePod.md)
 - [Organization](docs/Organization.md)
 - [PostCluster](docs/PostCluster.md)
 - [PostUser](docs/PostUser.md)
 - [Provisioner](docs/Provisioner.md)
 - [StatusUnauthorized](docs/StatusUnauthorized.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


