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


class IoK8sApiCoreV1Taint(object):
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
        'time_added': 'IoK8sApimachineryPkgApisMetaV1Time',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'time_added': 'timeAdded',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, time_added=None, value=None):
        """
        IoK8sApiCoreV1Taint - a model defined in Swagger
        """

        self._effect = None
        self._key = None
        self._time_added = None
        self._value = None

        self.effect = effect
        self.key = key
        if time_added is not None:
          self.time_added = time_added
        if value is not None:
          self.value = value

    @property
    def effect(self):
        """
        Gets the effect of this IoK8sApiCoreV1Taint.
        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.

        :return: The effect of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """
        Sets the effect of this IoK8sApiCoreV1Taint.
        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.

        :param effect: The effect of this IoK8sApiCoreV1Taint.
        :type: str
        """
        if effect is None:
            raise ValueError("Invalid value for `effect`, must not be `None`")

        self._effect = effect

    @property
    def key(self):
        """
        Gets the key of this IoK8sApiCoreV1Taint.
        Required. The taint key to be applied to a node.

        :return: The key of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this IoK8sApiCoreV1Taint.
        Required. The taint key to be applied to a node.

        :param key: The key of this IoK8sApiCoreV1Taint.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def time_added(self):
        """
        Gets the time_added of this IoK8sApiCoreV1Taint.
        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.

        :return: The time_added of this IoK8sApiCoreV1Taint.
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._time_added

    @time_added.setter
    def time_added(self, time_added):
        """
        Sets the time_added of this IoK8sApiCoreV1Taint.
        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.

        :param time_added: The time_added of this IoK8sApiCoreV1Taint.
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._time_added = time_added

    @property
    def value(self):
        """
        Gets the value of this IoK8sApiCoreV1Taint.
        Required. The taint value corresponding to the taint key.

        :return: The value of this IoK8sApiCoreV1Taint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this IoK8sApiCoreV1Taint.
        Required. The taint value corresponding to the taint key.

        :param value: The value of this IoK8sApiCoreV1Taint.
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
        if not isinstance(other, IoK8sApiCoreV1Taint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
