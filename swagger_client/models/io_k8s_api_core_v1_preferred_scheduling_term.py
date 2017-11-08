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


class IoK8sApiCoreV1PreferredSchedulingTerm(object):
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
        'preference': 'IoK8sApiCoreV1NodeSelectorTerm',
        'weight': 'int'
    }

    attribute_map = {
        'preference': 'preference',
        'weight': 'weight'
    }

    def __init__(self, preference=None, weight=None):
        """
        IoK8sApiCoreV1PreferredSchedulingTerm - a model defined in Swagger
        """

        self._preference = None
        self._weight = None

        self.preference = preference
        self.weight = weight

    @property
    def preference(self):
        """
        Gets the preference of this IoK8sApiCoreV1PreferredSchedulingTerm.
        A node selector term, associated with the corresponding weight.

        :return: The preference of this IoK8sApiCoreV1PreferredSchedulingTerm.
        :rtype: IoK8sApiCoreV1NodeSelectorTerm
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """
        Sets the preference of this IoK8sApiCoreV1PreferredSchedulingTerm.
        A node selector term, associated with the corresponding weight.

        :param preference: The preference of this IoK8sApiCoreV1PreferredSchedulingTerm.
        :type: IoK8sApiCoreV1NodeSelectorTerm
        """
        if preference is None:
            raise ValueError("Invalid value for `preference`, must not be `None`")

        self._preference = preference

    @property
    def weight(self):
        """
        Gets the weight of this IoK8sApiCoreV1PreferredSchedulingTerm.
        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :return: The weight of this IoK8sApiCoreV1PreferredSchedulingTerm.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this IoK8sApiCoreV1PreferredSchedulingTerm.
        Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :param weight: The weight of this IoK8sApiCoreV1PreferredSchedulingTerm.
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
        if not isinstance(other, IoK8sApiCoreV1PreferredSchedulingTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
