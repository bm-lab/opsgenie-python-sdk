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

from opsgenie_swagger.models.timeline_rotation import TimelineRotation  # noqa: F401,E501


class Timeline(object):
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
        'rotations': 'list[TimelineRotation]'
    }

    attribute_map = {
        'rotations': 'rotations'
    }

    def __init__(self, rotations=None):  # noqa: E501
        """Timeline - a model defined in Swagger"""  # noqa: E501

        self._rotations = None
        self.discriminator = None

        if rotations is not None:
            self.rotations = rotations

    @property
    def rotations(self):
        """Gets the rotations of this Timeline.  # noqa: E501


        :return: The rotations of this Timeline.  # noqa: E501
        :rtype: list[TimelineRotation]
        """
        return self._rotations

    @rotations.setter
    def rotations(self, rotations):
        """Sets the rotations of this Timeline.


        :param rotations: The rotations of this Timeline.  # noqa: E501
        :type: list[TimelineRotation]
        """

        self._rotations = rotations

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
        if not isinstance(other, Timeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
