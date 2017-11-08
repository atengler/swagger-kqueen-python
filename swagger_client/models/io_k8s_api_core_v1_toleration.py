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


class IoK8sApiCoreV1Toleration(object):
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
        'effect': 'str',
        'key': 'str',
        'operator': 'str',
        'toleration_seconds': 'int',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'operator': 'operator',
        'toleration_seconds': 'tolerationSeconds',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, operator=None, toleration_seconds=None, value=None):
        """
        IoK8sApiCoreV1Toleration - a model defined in Swagger
        """

        self._effect = None
        self._key = None
        self._operator = None
        self._toleration_seconds = None
        self._value = None

        if effect is not None:
          self.effect = effect
        if key is not None:
          self.key = key
        if operator is not None:
          self.operator = operator
        if toleration_seconds is not None:
          self.toleration_seconds = toleration_seconds
        if value is not None:
          self.value = value

    @property
    def effect(self):
        """
        Gets the effect of this IoK8sApiCoreV1Toleration.
        Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

        :return: The effect of this IoK8sApiCoreV1Toleration.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """
        Sets the effect of this IoK8sApiCoreV1Toleration.
        Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

        :param effect: The effect of this IoK8sApiCoreV1Toleration.
        :type: str
        """

        self._effect = effect

    @property
    def key(self):
        """
        Gets the key of this IoK8sApiCoreV1Toleration.
        Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.

        :return: The key of this IoK8sApiCoreV1Toleration.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this IoK8sApiCoreV1Toleration.
        Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.

        :param key: The key of this IoK8sApiCoreV1Toleration.
        :type: str
        """

        self._key = key

    @property
    def operator(self):
        """
        Gets the operator of this IoK8sApiCoreV1Toleration.
        Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.

        :return: The operator of this IoK8sApiCoreV1Toleration.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this IoK8sApiCoreV1Toleration.
        Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.

        :param operator: The operator of this IoK8sApiCoreV1Toleration.
        :type: str
        """

        self._operator = operator

    @property
    def toleration_seconds(self):
        """
        Gets the toleration_seconds of this IoK8sApiCoreV1Toleration.
        TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.

        :return: The toleration_seconds of this IoK8sApiCoreV1Toleration.
        :rtype: int
        """
        return self._toleration_seconds

    @toleration_seconds.setter
    def toleration_seconds(self, toleration_seconds):
        """
        Sets the toleration_seconds of this IoK8sApiCoreV1Toleration.
        TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.

        :param toleration_seconds: The toleration_seconds of this IoK8sApiCoreV1Toleration.
        :type: int
        """

        self._toleration_seconds = toleration_seconds

    @property
    def value(self):
        """
        Gets the value of this IoK8sApiCoreV1Toleration.
        Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.

        :return: The value of this IoK8sApiCoreV1Toleration.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this IoK8sApiCoreV1Toleration.
        Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.

        :param value: The value of this IoK8sApiCoreV1Toleration.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, IoK8sApiCoreV1Toleration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
