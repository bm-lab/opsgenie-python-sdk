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

from opsgenie_swagger.models.team_member import TeamMember  # noqa: F401,E501


class CreateTeamPayload(object):
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
        'name': 'str',
        'description': 'str',
        'members': 'list[TeamMember]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'members': 'members'
    }

    def __init__(self, name=None, description=None, members=None):  # noqa: E501
        """CreateTeamPayload - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._members = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if members is not None:
            self.members = members

    @property
    def name(self):
        """Gets the name of this CreateTeamPayload.  # noqa: E501

        Name of the team  # noqa: E501

        :return: The name of this CreateTeamPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTeamPayload.

        Name of the team  # noqa: E501

        :param name: The name of this CreateTeamPayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTeamPayload.  # noqa: E501

        The description of team  # noqa: E501

        :return: The description of this CreateTeamPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTeamPayload.

        The description of team  # noqa: E501

        :param description: The description of this CreateTeamPayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def members(self):
        """Gets the members of this CreateTeamPayload.  # noqa: E501

        The users which will be added to team, and optionally their roles.  # noqa: E501

        :return: The members of this CreateTeamPayload.  # noqa: E501
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this CreateTeamPayload.

        The users which will be added to team, and optionally their roles.  # noqa: E501

        :param members: The members of this CreateTeamPayload.  # noqa: E501
        :type: list[TeamMember]
        """

        self._members = members

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
        if not isinstance(other, CreateTeamPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
