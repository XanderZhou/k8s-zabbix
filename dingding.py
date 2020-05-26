#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=5eca7ddcc4c80dc9f397b37107f17e18a83b3201a170cffb769daa4359bad4bb"

def msg(text):
    json_text= {
     "msgtype": "markdown",
        "at": {
            "atMobiles": [
                "test"
            ],
            "isAtAll": False
        },
        "markdown": {
            "title": "zabbix monitor",
            "text": text,
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content

if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)