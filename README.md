# k8s-zabbix
根据官方Dockerfile修改
## 修改内容
zabbix-server-mysql
- 安装pip 
- 安装 python requests库
- 修改时区为中国

```shell
apk add py2-pip
apk add tzdata
pip install requests 
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
apk del tzdata
```

## 告警

```python
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
```

告警内容

```markdown
### <font color=#FF0000>---故障---</font>
#### {HOST.NAME}
### {TRIGGER.NAME}
##### 发生时间：{EVENT.DATE} {EVENT.TIME}
> 来自阿里云zabbix监控
```

恢复内容

```markdown
###  <font color=#006000>---恢复---</font>
#### {HOST.NAME}
### {TRIGGER.NAME}
##### 恢复时间：{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}
##### 持续时长:{EVENT.AGE}
## **{ITEM.LASTVALUE}**
> 来自阿里云zabbix监控
```
