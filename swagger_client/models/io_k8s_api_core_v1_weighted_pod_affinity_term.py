# coding: utf-8

"""
    Kubernetes Queen API

    A simple API to interact with Kubernetes clusters

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IoK8sApiCoreV1WeightedPodAffinityTerm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pod_affinity_term': 'IoK8sApiCoreV1PodAffinityTerm',
        'weight': 'int'
    }

    attribute_map = {
        'pod_affinity_term': 'podAffinityTerm',
        'weight': 'weight'
    }

    def __init__(self, pod_affinity_term=None, weight=None):
        """
        IoK8sApiCoreV1WeightedPodAffinityTerm - a model defined in Swagger
        """

        self._pod_affinity_term = None
        self._weight = None

        self.pod_affinity_term = pod_affinity_term
        self.weight = weight

    @property
    def pod_affinity_term(self):
        """
        Gets the pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        Required. A pod affinity term, associated with the corresponding weight.

        :return: The pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        :rtype: IoK8sApiCoreV1PodAffinityTerm
        """
        return self._pod_affinity_term

    @pod_affinity_term.setter
    def pod_affinity_term(self, pod_affinity_term):
        """
        Sets the pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        Required. A pod affinity term, associated with the corresponding weight.

        :param pod_affinity_term: The pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        :type: IoK8sApiCoreV1PodAffinityTerm
        """
        if pod_affinity_term is None:
            raise ValueError("Invalid value for `pod_affinity_term`, must not be `None`")

        self._pod_affinity_term = pod_affinity_term

    @property
    def weight(self):
        """
        Gets the weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :return: The weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :param weight: The weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.
        :type: int
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")

        self._weight = weight

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IoK8sApiCoreV1WeightedPodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
