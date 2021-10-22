<!-- markdownlint-disable -->

<a href="../src/pyquanda/hooks/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hooks`
base classes for hooks module. 



---

<a href="../src/pyquanda/hooks/__init__.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Hook`
BaseHookType. 

<a href="../src/pyquanda/hooks/__init__.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: str, config: Dict) → None
```

__init__. 



**Args:**
 
 - <b>`config`</b> (Dict):  config 



**Returns:**
 None: 




---

<a href="../src/pyquanda/hooks/__init__.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `async_send`

```python
async_send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 

---

<a href="../src/pyquanda/hooks/__init__.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `fmt_json`

```python
fmt_json(dct: Dict) → Dict
```

fmt_json. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 



**Returns:**
 
 - <b>`Dict`</b>:  response dict 

---

<a href="../src/pyquanda/hooks/__init__.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(dct: Dict)
```

send. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
