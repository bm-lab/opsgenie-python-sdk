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

from opsgenie_swagger.models.filter import Filter  # noqa: F401,E501
from opsgenie_swagger.models.notification_action_type import NotificationActionType  # noqa: F401,E501
from opsgenie_swagger.models.notification_repeat import NotificationRepeat  # noqa: F401,E501
from opsgenie_swagger.models.notification_rule_step import NotificationRuleStep  # noqa: F401,E501
from opsgenie_swagger.models.notify_time import NotifyTime  # noqa: F401,E501
from opsgenie_swagger.models.schedule_recipient import ScheduleRecipient  # noqa: F401,E501
from opsgenie_swagger.models.time_restriction_interval import TimeRestrictionInterval  # noqa: F401,E501


class NotificationRule(object):
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
        'name': 'str',
        'action_type': 'NotificationActionType',
        'criteria': 'Filter',
        'notification_time': 'list[NotifyTime]',
        'order': 'int',
        'time_restriction': 'TimeRestrictionInterval',
        'steps': 'list[NotificationRuleStep]',
        'schedules': 'list[ScheduleRecipient]',
        'repeat': 'NotificationRepeat',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'action_type': 'actionType',
        'criteria': 'criteria',
        'notification_time': 'notificationTime',
        'order': 'order',
        'time_restriction': 'timeRestriction',
        'steps': 'steps',
        'schedules': 'schedules',
        'repeat': 'repeat',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, name=None, action_type=None, criteria=None, notification_time=None, order=None, time_restriction=None, steps=None, schedules=None, repeat=None, enabled=None):  # noqa: E501
        """NotificationRule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._action_type = None
        self._criteria = None
        self._notification_time = None
        self._order = None
        self._time_restriction = None
        self._steps = None
        self._schedules = None
        self._repeat = None
        self._enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if action_type is not None:
            self.action_type = action_type
        if criteria is not None:
            self.criteria = criteria
        if notification_time is not None:
            self.notification_time = notification_time
        if order is not None:
            self.order = order
        if time_restriction is not None:
            self.time_restriction = time_restriction
        if steps is not None:
            self.steps = steps
        if schedules is not None:
            self.schedules = schedules
        if repeat is not None:
            self.repeat = repeat
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this NotificationRule.  # noqa: E501


        :return: The id of this NotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationRule.


        :param id: The id of this NotificationRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NotificationRule.  # noqa: E501


        :return: The name of this NotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationRule.


        :param name: The name of this NotificationRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def action_type(self):
        """Gets the action_type of this NotificationRule.  # noqa: E501


        :return: The action_type of this NotificationRule.  # noqa: E501
        :rtype: NotificationActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this NotificationRule.


        :param action_type: The action_type of this NotificationRule.  # noqa: E501
        :type: NotificationActionType
        """

        self._action_type = action_type

    @property
    def criteria(self):
        """Gets the criteria of this NotificationRule.  # noqa: E501


        :return: The criteria of this NotificationRule.  # noqa: E501
        :rtype: Filter
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this NotificationRule.


        :param criteria: The criteria of this NotificationRule.  # noqa: E501
        :type: Filter
        """

        self._criteria = criteria

    @property
    def notification_time(self):
        """Gets the notification_time of this NotificationRule.  # noqa: E501


        :return: The notification_time of this NotificationRule.  # noqa: E501
        :rtype: list[NotifyTime]
        """
        return self._notification_time

    @notification_time.setter
    def notification_time(self, notification_time):
        """Sets the notification_time of this NotificationRule.


        :param notification_time: The notification_time of this NotificationRule.  # noqa: E501
        :type: list[NotifyTime]
        """

        self._notification_time = notification_time

    @property
    def order(self):
        """Gets the order of this NotificationRule.  # noqa: E501


        :return: The order of this NotificationRule.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this NotificationRule.


        :param order: The order of this NotificationRule.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def time_restriction(self):
        """Gets the time_restriction of this NotificationRule.  # noqa: E501


        :return: The time_restriction of this NotificationRule.  # noqa: E501
        :rtype: TimeRestrictionInterval
        """
        return self._time_restriction

    @time_restriction.setter
    def time_restriction(self, time_restriction):
        """Sets the time_restriction of this NotificationRule.


        :param time_restriction: The time_restriction of this NotificationRule.  # noqa: E501
        :type: TimeRestrictionInterval
        """

        self._time_restriction = time_restriction

    @property
    def steps(self):
        """Gets the steps of this NotificationRule.  # noqa: E501


        :return: The steps of this NotificationRule.  # noqa: E501
        :rtype: list[NotificationRuleStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this NotificationRule.


        :param steps: The steps of this NotificationRule.  # noqa: E501
        :type: list[NotificationRuleStep]
        """

        self._steps = steps

    @property
    def schedules(self):
        """Gets the schedules of this NotificationRule.  # noqa: E501


        :return: The schedules of this NotificationRule.  # noqa: E501
        :rtype: list[ScheduleRecipient]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this NotificationRule.


        :param schedules: The schedules of this NotificationRule.  # noqa: E501
        :type: list[ScheduleRecipient]
        """

        self._schedules = schedules

    @property
    def repeat(self):
        """Gets the repeat of this NotificationRule.  # noqa: E501


        :return: The repeat of this NotificationRule.  # noqa: E501
        :rtype: NotificationRepeat
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this NotificationRule.


        :param repeat: The repeat of this NotificationRule.  # noqa: E501
        :type: NotificationRepeat
        """

        self._repeat = repeat

    @property
    def enabled(self):
        """Gets the enabled of this NotificationRule.  # noqa: E501


        :return: The enabled of this NotificationRule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NotificationRule.


        :param enabled: The enabled of this NotificationRule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, NotificationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
