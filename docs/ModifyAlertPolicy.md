# ModifyAlertPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_original_alert_actions** | **bool** |  | [optional] 
**ignore_original_details** | **bool** | If set to true, policy will ignore the original details of the alert. Default value is false | [optional] 
**ignore_original_recipients** | **bool** | If set to true, policy will ignore the original recipients of the alert. Default value is false | [optional] 
**ignore_original_tags** | **bool** | If set to true, policy will ignore the original tags of the alert. Default value is false | [optional] 
**ignore_original_teams** | **bool** | If set to true, policy will ignore the original teams of the alert. Default value is false | [optional] 
**_continue** | **bool** | Will continue with other modify policies if set to true | [optional] 
**alias** | **str** | Alias of the alert. You can use {{alias}} to refer to the original alias. Default value is {{alias}} | [optional] 
**description** | **str** | Description of the alert. You can use {{description}} to refer to the original alert description. Default value is {{description}} | [optional] 
**entity** | **str** | Entity field of the alert. You can use {{entity}} to refer to the original entity. Default value is {{entity}} | [optional] 
**message** | **str** | Message of the alert | [optional] 
**source** | **str** | Source field of the alert. You can use {{source}} to refer to the original source. Default value is {{source}} | [optional] 
**actions** | **list[str]** | Alert actions as a list of strings to add to the alerts original actions value. If ignoreOriginalAlertActions field is set to true, this will replace the original actions. | [optional] 
**recipients** | [**list[Recipient]**](Recipient.md) | Recipients to add to the alerts original recipients value as a list of escalations, schedules, teams, users or the reserved word none or all. If ignoreOriginalRecipients field is set to true, this will replace the original recipients. | [optional] 
**tags** | **list[str]** | Tags to add to the alerts original tags value as a list of strings. If ignoreOriginalRecipients field is set to true, this will replace the original recipients. | [optional] 
**details** | **dict(str, str)** | Custom properties to add to the alerts original details value as a list of strings. If ignoreOriginalDetails field is set to true, this will replace the original details. | [optional] 
**priority** | **str** | Priority level of the alert | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


