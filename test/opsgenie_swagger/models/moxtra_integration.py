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
from opsgenie_swagger.models.integration import Integration  # noqa: F401,E501
from opsgenie_swagger.models.team_meta import TeamMeta  # noqa: F401,E501
from opsgenie_swagger.models.webhook_callback import WebhookCallback  # noqa: F401,E501


class MoxtraIntegration(object):
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
        'alert_filter': 'AlertFilter',
        'alert_actions': 'list[str]',
        'callback_type': 'str',
        'url': 'str',
        'headers': 'dict(str, str)'
    }

    attribute_map = {
        'alert_filter': 'alertFilter',
        'alert_actions': 'alertActions',
        'callback_type': 'callback-type',
        'url': 'url',
        'headers': 'headers'
    }

    def __init__(self, alert_filter=None, alert_actions=None, callback_type=None, url=None, headers=None):  # noqa: E501
        """MoxtraIntegration - a model defined in Swagger"""  # noqa: E501

        self._alert_filter = None
        self._alert_actions = None
        self._callback_type = None
        self._url = None
        self._headers = None
        self.discriminator = None

        if alert_filter is not None:
            self.alert_filter = alert_filter
        if alert_actions is not None:
            self.alert_actions = alert_actions
        if callback_type is not None:
            self.callback_type = callback_type
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers

    @property
    def alert_filter(self):
        """Gets the alert_filter of this MoxtraIntegration.  # noqa: E501


        :return: The alert_filter of this MoxtraIntegration.  # noqa: E501
        :rtype: AlertFilter
        """
        return self._alert_filter

    @alert_filter.setter
    def alert_filter(self, alert_filter):
        """Sets the alert_filter of this MoxtraIntegration.


        :param alert_filter: The alert_filter of this MoxtraIntegration.  # noqa: E501
        :type: AlertFilter
        """

        self._alert_filter = alert_filter

    @property
    def alert_actions(self):
        """Gets the alert_actions of this MoxtraIntegration.  # noqa: E501


        :return: The alert_actions of this MoxtraIntegration.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_actions

    @alert_actions.setter
    def alert_actions(self, alert_actions):
        """Sets the alert_actions of this MoxtraIntegration.


        :param alert_actions: The alert_actions of this MoxtraIntegration.  # noqa: E501
        :type: list[str]
        """

        self._alert_actions = alert_actions

    @property
    def callback_type(self):
        """Gets the callback_type of this MoxtraIntegration.  # noqa: E501


        :return: The callback_type of this MoxtraIntegration.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this MoxtraIntegration.


        :param callback_type: The callback_type of this MoxtraIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["bidirectional-callback", "webhook-callback", "campfire-callback", "flowdock-callback", "flowdock-v2-callback", "planio-callback"]  # noqa: E501
        if callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(callback_type, allowed_values)
            )

        self._callback_type = callback_type

    @property
    def url(self):
        """Gets the url of this MoxtraIntegration.  # noqa: E501


        :return: The url of this MoxtraIntegration.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MoxtraIntegration.


        :param url: The url of this MoxtraIntegration.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this MoxtraIntegration.  # noqa: E501


        :return: The headers of this MoxtraIntegration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this MoxtraIntegration.


        :param headers: The headers of this MoxtraIntegration.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

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
        if not isinstance(other, MoxtraIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
