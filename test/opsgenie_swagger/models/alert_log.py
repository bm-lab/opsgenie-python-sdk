# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AlertLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'log': 'str',
        'type': 'str',
        'owner': 'str',
        'created_at': 'datetime',
        'offset': 'str'
    }

    attribute_map = {
        'log': 'log',
        'type': 'type',
        'owner': 'owner',
        'created_at': 'createdAt',
        'offset': 'offset'
    }

    def __init__(self, log=None, type=None, owner=None, created_at=None, offset=None):  # noqa: E501
        """AlertLog - a model defined in Swagger"""  # noqa: E501

        self._log = None
        self._type = None
        self._owner = None
        self._created_at = None
        self._offset = None
        self.discriminator = None

        if log is not None:
            self.log = log
        if type is not None:
            self.type = type
        if owner is not None:
            self.owner = owner
        if created_at is not None:
            self.created_at = created_at
        if offset is not None:
            self.offset = offset

    @property
    def log(self):
        """Gets the log of this AlertLog.  # noqa: E501


        :return: The log of this AlertLog.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this AlertLog.


        :param log: The log of this AlertLog.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def type(self):
        """Gets the type of this AlertLog.  # noqa: E501


        :return: The type of this AlertLog.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertLog.


        :param type: The type of this AlertLog.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def owner(self):
        """Gets the owner of this AlertLog.  # noqa: E501


        :return: The owner of this AlertLog.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AlertLog.


        :param owner: The owner of this AlertLog.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def created_at(self):
        """Gets the created_at of this AlertLog.  # noqa: E501


        :return: The created_at of this AlertLog.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AlertLog.


        :param created_at: The created_at of this AlertLog.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def offset(self):
        """Gets the offset of this AlertLog.  # noqa: E501


        :return: The offset of this AlertLog.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AlertLog.


        :param offset: The offset of this AlertLog.  # noqa: E501
        :type: str
        """

        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
