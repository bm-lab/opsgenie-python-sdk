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


class CallbackCondition(object):
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
        'field': 'str',
        '_not': 'bool',
        'operation': 'str',
        'expected_value': 'str',
        'order': 'int'
    }

    attribute_map = {
        'field': 'field',
        '_not': 'not',
        'operation': 'operation',
        'expected_value': 'expectedValue',
        'order': 'order'
    }

    def __init__(self, field=None, _not=None, operation=None, expected_value=None, order=None):  # noqa: E501
        """CallbackCondition - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self.__not = None
        self._operation = None
        self._expected_value = None
        self._order = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if _not is not None:
            self._not = _not
        if operation is not None:
            self.operation = operation
        if expected_value is not None:
            self.expected_value = expected_value
        if order is not None:
            self.order = order

    @property
    def field(self):
        """Gets the field of this CallbackCondition.  # noqa: E501


        :return: The field of this CallbackCondition.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this CallbackCondition.


        :param field: The field of this CallbackCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["message", "alias", "description", "source", "entity", "tags", "actions", "extra-properties", "recipients", "teams", "priority"]  # noqa: E501
        if field not in allowed_values:
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                .format(field, allowed_values)
            )

        self._field = field

    @property
    def _not(self):
        """Gets the _not of this CallbackCondition.  # noqa: E501


        :return: The _not of this CallbackCondition.  # noqa: E501
        :rtype: bool
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this CallbackCondition.


        :param _not: The _not of this CallbackCondition.  # noqa: E501
        :type: bool
        """

        self.__not = _not

    @property
    def operation(self):
        """Gets the operation of this CallbackCondition.  # noqa: E501


        :return: The operation of this CallbackCondition.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this CallbackCondition.


        :param operation: The operation of this CallbackCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["matches", "contains", "starts-with", "ends-with", "equals", "contains-key", "contains-value", "greater-than", "less-than", "is-empty", "equals-ignore-whitespace"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def expected_value(self):
        """Gets the expected_value of this CallbackCondition.  # noqa: E501


        :return: The expected_value of this CallbackCondition.  # noqa: E501
        :rtype: str
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, expected_value):
        """Sets the expected_value of this CallbackCondition.


        :param expected_value: The expected_value of this CallbackCondition.  # noqa: E501
        :type: str
        """

        self._expected_value = expected_value

    @property
    def order(self):
        """Gets the order of this CallbackCondition.  # noqa: E501


        :return: The order of this CallbackCondition.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CallbackCondition.


        :param order: The order of this CallbackCondition.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if not isinstance(other, CallbackCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
