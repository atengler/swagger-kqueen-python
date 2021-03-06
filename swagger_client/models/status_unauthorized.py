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


class StatusUnauthorized(object):
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
        'description': 'str',
        'error': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'description': 'description',
        'error': 'error',
        'status_code': 'status_code'
    }

    def __init__(self, description=None, error=None, status_code=None):
        """
        StatusUnauthorized - a model defined in Swagger
        """

        self._description = None
        self._error = None
        self._status_code = None

        if description is not None:
          self.description = description
        if error is not None:
          self.error = error
        if status_code is not None:
          self.status_code = status_code

    @property
    def description(self):
        """
        Gets the description of this StatusUnauthorized.
        Error description

        :return: The description of this StatusUnauthorized.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StatusUnauthorized.
        Error description

        :param description: The description of this StatusUnauthorized.
        :type: str
        """

        self._description = description

    @property
    def error(self):
        """
        Gets the error of this StatusUnauthorized.
        HTTP error

        :return: The error of this StatusUnauthorized.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this StatusUnauthorized.
        HTTP error

        :param error: The error of this StatusUnauthorized.
        :type: str
        """

        self._error = error

    @property
    def status_code(self):
        """
        Gets the status_code of this StatusUnauthorized.
        HTTP error code

        :return: The status_code of this StatusUnauthorized.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this StatusUnauthorized.
        HTTP error code

        :param status_code: The status_code of this StatusUnauthorized.
        :type: int
        """

        self._status_code = status_code

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
        if not isinstance(other, StatusUnauthorized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
