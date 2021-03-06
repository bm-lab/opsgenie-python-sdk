# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from opsgenie_swagger.api_client import ApiClient


class ForwardingRuleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_forwarding_rule(self, body, **kwargs):  # noqa: E501
        """Create Forwarding Rule  # noqa: E501

        Creates a new forwarding rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_forwarding_rule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateForwardingRulePayload body: Request payload to created forwarding rule (required)
        :return: CreateForwardingRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_forwarding_rule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_forwarding_rule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_forwarding_rule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Forwarding Rule  # noqa: E501

        Creates a new forwarding rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_forwarding_rule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateForwardingRulePayload body: Request payload to created forwarding rule (required)
        :return: CreateForwardingRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_forwarding_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_forwarding_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/forwarding-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateForwardingRuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_forwarding_rule(self, identifier, **kwargs):  # noqa: E501
        """Delete Forwarding Rule  # noqa: E501

        Deletes forwarding rule with given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_forwarding_rule(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_forwarding_rule_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_forwarding_rule_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def delete_forwarding_rule_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Delete Forwarding Rule  # noqa: E501

        Deletes forwarding rule with given identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_forwarding_rule_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_forwarding_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_forwarding_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/forwarding-rules/{identifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_forwarding_rule(self, identifier, **kwargs):  # noqa: E501
        """Get Forwarding Rule  # noqa: E501

        Returns forwarding rule with given id or alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_forwarding_rule(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: GetForwardingRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_forwarding_rule_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_forwarding_rule_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_forwarding_rule_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Forwarding Rule  # noqa: E501

        Returns forwarding rule with given id or alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_forwarding_rule_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: GetForwardingRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_forwarding_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_forwarding_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/forwarding-rules/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetForwardingRuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_forwarding_rules(self, **kwargs):  # noqa: E501
        """List Forwarding Rules  # noqa: E501

        Returns list of forwarding rules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_forwarding_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListForwardingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_forwarding_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_forwarding_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_forwarding_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List Forwarding Rules  # noqa: E501

        Returns list of forwarding rules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_forwarding_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListForwardingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_forwarding_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/forwarding-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListForwardingRulesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_forwarding_rule(self, identifier, body, **kwargs):  # noqa: E501
        """Update Forwarding Rule  # noqa: E501

        Update forwarding rule with given rule id or alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_forwarding_rule(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param UpdateForwardingRulePayload body: Request payload of update forwarding rule action (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_forwarding_rule_with_http_info(identifier, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_forwarding_rule_with_http_info(identifier, body, **kwargs)  # noqa: E501
            return data

    def update_forwarding_rule_with_http_info(self, identifier, body, **kwargs):  # noqa: E501
        """Update Forwarding Rule  # noqa: E501

        Update forwarding rule with given rule id or alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_forwarding_rule_with_http_info(identifier, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias' (required)
        :param UpdateForwardingRulePayload body: Request payload of update forwarding rule action (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'body', 'identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_forwarding_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_forwarding_rule`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_forwarding_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/forwarding-rules/{identifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
