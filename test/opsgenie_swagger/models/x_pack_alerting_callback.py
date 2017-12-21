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

from opsgenie_swagger.models.alert_filter import AlertFilter  # noqa: F401,E501
from opsgenie_swagger.models.bidirectional_callback import BidirectionalCallback  # noqa: F401,E501


class XPackAlertingCallback(object):
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
        'eswatcher_action_id': 'str',
        'eswatcher_host_id': 'str'
    }

    attribute_map = {
        'eswatcher_action_id': 'eswatcherActionId',
        'eswatcher_host_id': 'eswatcherHostId'
    }

    def __init__(self, eswatcher_action_id=None, eswatcher_host_id=None):  # noqa: E501
        """XPackAlertingCallback - a model defined in Swagger"""  # noqa: E501

        self._eswatcher_action_id = None
        self._eswatcher_host_id = None
        self.discriminator = None

        if eswatcher_action_id is not None:
            self.eswatcher_action_id = eswatcher_action_id
        if eswatcher_host_id is not None:
            self.eswatcher_host_id = eswatcher_host_id

    @property
    def eswatcher_action_id(self):
        """Gets the eswatcher_action_id of this XPackAlertingCallback.  # noqa: E501


        :return: The eswatcher_action_id of this XPackAlertingCallback.  # noqa: E501
        :rtype: str
        """
        return self._eswatcher_action_id

    @eswatcher_action_id.setter
    def eswatcher_action_id(self, eswatcher_action_id):
        """Sets the eswatcher_action_id of this XPackAlertingCallback.


        :param eswatcher_action_id: The eswatcher_action_id of this XPackAlertingCallback.  # noqa: E501
        :type: str
        """

        self._eswatcher_action_id = eswatcher_action_id

    @property
    def eswatcher_host_id(self):
        """Gets the eswatcher_host_id of this XPackAlertingCallback.  # noqa: E501


        :return: The eswatcher_host_id of this XPackAlertingCallback.  # noqa: E501
        :rtype: str
        """
        return self._eswatcher_host_id

    @eswatcher_host_id.setter
    def eswatcher_host_id(self, eswatcher_host_id):
        """Sets the eswatcher_host_id of this XPackAlertingCallback.


        :param eswatcher_host_id: The eswatcher_host_id of this XPackAlertingCallback.  # noqa: E501
        :type: str
        """

        self._eswatcher_host_id = eswatcher_host_id

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
        if not isinstance(other, XPackAlertingCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other