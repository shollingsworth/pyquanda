<!-- markdownlint-disable -->

<a href="../src/pyquanda/environment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `environment`
Environment variables, configuration and static filepaths. 

**Global Variables**
---------------
- **MOCK_CONFIG**


---

<a href="../src/pyquanda/environment.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `InterviewConfig`
InterviewConfig. 

<a href="../src/pyquanda/environment.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(mod_path: Path = None)
```

__init__. 



**Args:**
 
 - <b>`mod_path`</b> (Path):  mod_path 


---

#### <kbd>property</kbd> allow_sudo

allow_sudo. 



**Args:**
 



**Returns:**
 
 - <b>`List[str]`</b>:  list of allowed sudo commands 

---

#### <kbd>property</kbd> firstname

firstname. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> fqdn

fqdn. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> lastname

lastname. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> quanda_id

instance / state id for hooks. 

You may or may not care about this. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> restricted_commands

restricted_commands. 



**Args:**
 



**Returns:**
 
 - <b>`List[str]`</b>:  list of restricted commands, i.e. bash, zsh, etc shells that might be used to breakout 

---

#### <kbd>property</kbd> username

username. 



**Args:**
 



**Returns:**
  str: 



---

<a href="../src/pyquanda/environment.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  object dict representation 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
