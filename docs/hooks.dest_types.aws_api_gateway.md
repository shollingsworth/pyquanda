<!-- markdownlint-disable -->

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks.dest_types.aws_api_gateway`
Aws API Gateway Hook 

**Global Variables**
---------------
- **DEST_TYPE_AWS_API_GATEWAY**


---

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `WebHookAwsApiGw`
WebHookNoAuth. 

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `async_send`

```python
async_send(dct: Dict)
```

async_send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 

---

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 

---

<a href="../src/pyquanda/hooks/dest_types/aws_api_gateway.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `sign_headers`

```python
sign_headers(payload: Dict)
```

Sign AWS API request headers. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
