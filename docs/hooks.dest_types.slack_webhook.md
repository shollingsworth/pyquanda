<!-- markdownlint-disable -->

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks.dest_types.slack_webhook`
Abstract method for other modules. 

**Global Variables**
---------------
- **DEST_TYPE_SLACK_WEBHOOK**


---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SlackSend`
Send slack messages to ops-interviews channel. 

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(webhook_url: str)
```

__init__. 



**Args:**
 
 - <b>`webhook_url`</b> (str):  webhook_url 


---

#### <kbd>property</kbd> log

Slack logger. 



---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `async_send`

```python
async_send(dct: Dict)
```

Hit send. 

---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 


---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SlackWebhook`
WebHookNoAuth. 

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: str, config: Dict) → None
```

__init__. 



**Args:**
 
 - <b>`config`</b> (Dict):  config 



**Returns:**
 None: 



**Raises:**
 
 - <b>`PreCheckFail`</b>:  on validation error 




---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `async_send`

```python
async_send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 

---

<a href="../src/pyquanda/hooks/dest_types/slack_webhook.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
