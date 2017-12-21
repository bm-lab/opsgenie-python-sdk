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

from opsgenie_swagger.models.alert_integration import AlertIntegration  # noqa: F401,E501
from opsgenie_swagger.models.alert_report import AlertReport  # noqa: F401,E501
from opsgenie_swagger.models.alert_team_meta import AlertTeamMeta  # noqa: F401,E501
from opsgenie_swagger.models.base_alert import BaseAlert  # noqa: F401,E501


class Alert(object):
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
        'id': 'str',
        'tiny_id': 'str',
        'alias': 'str',
        'message': 'str',
        'status': 'str',
        'acknowledged': 'bool',
        'is_seen': 'bool',
        'tags': 'list[str]',
        'snoozed': 'bool',
        'snoozed_until': 'datetime',
        'count': 'int',
        'last_occurred_at': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'source': 'str',
        'owner': 'str',
        'priority': 'str',
        'teams': 'list[AlertTeamMeta]',
        'integration': 'AlertIntegration',
        'report': 'AlertReport',
        'actions': 'list[str]',
        'entity': 'str',
        'description': 'str',
        'details': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'tiny_id': 'tinyId',
        'alias': 'alias',
        'message': 'message',
        'status': 'status',
        'acknowledged': 'acknowledged',
        'is_seen': 'isSeen',
        'tags': 'tags',
        'snoozed': 'snoozed',
        'snoozed_until': 'snoozedUntil',
        'count': 'count',
        'last_occurred_at': 'lastOccurredAt',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'source': 'source',
        'owner': 'owner',
        'priority': 'priority',
        'teams': 'teams',
        'integration': 'integration',
        'report': 'report',
        'actions': 'actions',
        'entity': 'entity',
        'description': 'description',
        'details': 'details'
    }

    def __init__(self, id=None, tiny_id=None, alias=None, message=None, status=None, acknowledged=None, is_seen=None, tags=None, snoozed=None, snoozed_until=None, count=None, last_occurred_at=None, created_at=None, updated_at=None, source=None, owner=None, priority=None, teams=None, integration=None, report=None, actions=None, entity=None, description=None, details=None):  # noqa: E501
        """Alert - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._tiny_id = None
        self._alias = None
        self._message = None
        self._status = None
        self._acknowledged = None
        self._is_seen = None
        self._tags = None
        self._snoozed = None
        self._snoozed_until = None
        self._count = None
        self._last_occurred_at = None
        self._created_at = None
        self._updated_at = None
        self._source = None
        self._owner = None
        self._priority = None
        self._teams = None
        self._integration = None
        self._report = None
        self._actions = None
        self._entity = None
        self._description = None
        self._details = None
        self.discriminator = None

        self.id = id
        if tiny_id is not None:
            self.tiny_id = tiny_id
        if alias is not None:
            self.alias = alias
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if acknowledged is not None:
            self.acknowledged = acknowledged
        if is_seen is not None:
            self.is_seen = is_seen
        if tags is not None:
            self.tags = tags
        if snoozed is not None:
            self.snoozed = snoozed
        if snoozed_until is not None:
            self.snoozed_until = snoozed_until
        if count is not None:
            self.count = count
        if last_occurred_at is not None:
            self.last_occurred_at = last_occurred_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source is not None:
            self.source = source
        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        if teams is not None:
            self.teams = teams
        if integration is not None:
            self.integration = integration
        if report is not None:
            self.report = report
        if actions is not None:
            self.actions = actions
        if entity is not None:
            self.entity = entity
        if description is not None:
            self.description = description
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this Alert.  # noqa: E501


        :return: The id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alert.


        :param id: The id of this Alert.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tiny_id(self):
        """Gets the tiny_id of this Alert.  # noqa: E501


        :return: The tiny_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._tiny_id

    @tiny_id.setter
    def tiny_id(self, tiny_id):
        """Sets the tiny_id of this Alert.


        :param tiny_id: The tiny_id of this Alert.  # noqa: E501
        :type: str
        """

        self._tiny_id = tiny_id

    @property
    def alias(self):
        """Gets the alias of this Alert.  # noqa: E501


        :return: The alias of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Alert.


        :param alias: The alias of this Alert.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def message(self):
        """Gets the message of this Alert.  # noqa: E501


        :return: The message of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Alert.


        :param message: The message of this Alert.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this Alert.  # noqa: E501


        :return: The status of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Alert.


        :param status: The status of this Alert.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def acknowledged(self):
        """Gets the acknowledged of this Alert.  # noqa: E501


        :return: The acknowledged of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """Sets the acknowledged of this Alert.


        :param acknowledged: The acknowledged of this Alert.  # noqa: E501
        :type: bool
        """

        self._acknowledged = acknowledged

    @property
    def is_seen(self):
        """Gets the is_seen of this Alert.  # noqa: E501


        :return: The is_seen of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._is_seen

    @is_seen.setter
    def is_seen(self, is_seen):
        """Sets the is_seen of this Alert.


        :param is_seen: The is_seen of this Alert.  # noqa: E501
        :type: bool
        """

        self._is_seen = is_seen

    @property
    def tags(self):
        """Gets the tags of this Alert.  # noqa: E501


        :return: The tags of this Alert.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Alert.


        :param tags: The tags of this Alert.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def snoozed(self):
        """Gets the snoozed of this Alert.  # noqa: E501


        :return: The snoozed of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._snoozed

    @snoozed.setter
    def snoozed(self, snoozed):
        """Sets the snoozed of this Alert.


        :param snoozed: The snoozed of this Alert.  # noqa: E501
        :type: bool
        """

        self._snoozed = snoozed

    @property
    def snoozed_until(self):
        """Gets the snoozed_until of this Alert.  # noqa: E501


        :return: The snoozed_until of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._snoozed_until

    @snoozed_until.setter
    def snoozed_until(self, snoozed_until):
        """Sets the snoozed_until of this Alert.


        :param snoozed_until: The snoozed_until of this Alert.  # noqa: E501
        :type: datetime
        """

        self._snoozed_until = snoozed_until

    @property
    def count(self):
        """Gets the count of this Alert.  # noqa: E501


        :return: The count of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Alert.


        :param count: The count of this Alert.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def last_occurred_at(self):
        """Gets the last_occurred_at of this Alert.  # noqa: E501


        :return: The last_occurred_at of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._last_occurred_at

    @last_occurred_at.setter
    def last_occurred_at(self, last_occurred_at):
        """Sets the last_occurred_at of this Alert.


        :param last_occurred_at: The last_occurred_at of this Alert.  # noqa: E501
        :type: datetime
        """

        self._last_occurred_at = last_occurred_at

    @property
    def created_at(self):
        """Gets the created_at of this Alert.  # noqa: E501


        :return: The created_at of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Alert.


        :param created_at: The created_at of this Alert.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Alert.  # noqa: E501


        :return: The updated_at of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Alert.


        :param updated_at: The updated_at of this Alert.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def source(self):
        """Gets the source of this Alert.  # noqa: E501


        :return: The source of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Alert.


        :param source: The source of this Alert.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def owner(self):
        """Gets the owner of this Alert.  # noqa: E501


        :return: The owner of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Alert.


        :param owner: The owner of this Alert.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def priority(self):
        """Gets the priority of this Alert.  # noqa: E501


        :return: The priority of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Alert.


        :param priority: The priority of this Alert.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def teams(self):
        """Gets the teams of this Alert.  # noqa: E501


        :return: The teams of this Alert.  # noqa: E501
        :rtype: list[AlertTeamMeta]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Alert.


        :param teams: The teams of this Alert.  # noqa: E501
        :type: list[AlertTeamMeta]
        """

        self._teams = teams

    @property
    def integration(self):
        """Gets the integration of this Alert.  # noqa: E501


        :return: The integration of this Alert.  # noqa: E501
        :rtype: AlertIntegration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this Alert.


        :param integration: The integration of this Alert.  # noqa: E501
        :type: AlertIntegration
        """

        self._integration = integration

    @property
    def report(self):
        """Gets the report of this Alert.  # noqa: E501


        :return: The report of this Alert.  # noqa: E501
        :rtype: AlertReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this Alert.


        :param report: The report of this Alert.  # noqa: E501
        :type: AlertReport
        """

        self._report = report

    @property
    def actions(self):
        """Gets the actions of this Alert.  # noqa: E501


        :return: The actions of this Alert.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Alert.


        :param actions: The actions of this Alert.  # noqa: E501
        :type: list[str]
        """

        self._actions = actions

    @property
    def entity(self):
        """Gets the entity of this Alert.  # noqa: E501


        :return: The entity of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Alert.


        :param entity: The entity of this Alert.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def description(self):
        """Gets the description of this Alert.  # noqa: E501


        :return: The description of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Alert.


        :param description: The description of this Alert.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def details(self):
        """Gets the details of this Alert.  # noqa: E501


        :return: The details of this Alert.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Alert.


        :param details: The details of this Alert.  # noqa: E501
        :type: dict(str, str)
        """

        self._details = details

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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
