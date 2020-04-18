#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def msg(alert_json):
    have_instance = False
    message = f"*[{alert_json['status'].upper()}] {alert_json['labels']['alertname']}*\n"
    if (('summary' in alert_json['annotations'] and alert_json['labels']['instance'] in alert_json['annotations']['summary'])
        or ('description' in alert_json['annotations'] and alert_json['labels']['instance'] in alert_json['annotations']['description'])):
        have_instance = True
    for key in alert_json['labels']:
        if key == 'alertname':
            continue
        elif key == 'instance' and have_instance:
            continue
        else:
            message = message + f" {key}: `{alert_json['labels'][key]}`\n"
    if 'summary' in alert_json['annotations'] and alert_json['annotations']:
        message = message + f" *summary*: `{alert_json['annotations']['summary']}`\n"
    if 'description' in alert_json['annotations'] and alert_json['annotations']:
        message = message + f" *description*: `{alert_json['annotations']['description']}`\n"
    return message

def alert_msg_handler(alert_json):
    result = ""
    result = msg(alert_json)
    return result
