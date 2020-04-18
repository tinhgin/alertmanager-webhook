#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def msg(alert_json):
    message = f"*[{alert_json['status'].upper()}] {alert_json['labels']['alertname']}*\n"
    for key in alert_json['labels']:
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
