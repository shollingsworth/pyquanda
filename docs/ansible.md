<!-- markdownlint-disable -->

<a href="../src/pyquanda/ansible/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ansible`
Main Ansible Module Builder. 

**Global Variables**
---------------
- **ansible_runner**
- **HOOK_TYPE_ANSIBLE_EVENT**
- **HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE**
- **SUPRESS_OUTPUT**
- **EVENT_FAILURE**
- **EVENT_OK**
- **EVENT_RUNBOOK_DONE**


---

<a href="../src/pyquanda/ansible/__init__.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Ansible`
Ansible. 

<a href="../src/pyquanda/ansible/__init__.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: Path) → None
```

__init__. 



**Args:**
 
 - <b>`path`</b> (Path):  path 



**Returns:**
 None: 




---

<a href="../src/pyquanda/ansible/__init__.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `copy_dirs`

```python
copy_dirs() → List[str]
```

copy_dirs. 



**Args:**
 



**Returns:**
 
 - <b>`List[str]`</b>:  list of directory strings 

---

<a href="../src/pyquanda/ansible/__init__.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `event_handler`

```python
event_handler(evt_dct: Dict)
```

event_handler. 



**Args:**
 
 - <b>`evt_dct`</b> (Dict):  evt_dct 

---

<a href="../src/pyquanda/ansible/__init__.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run()
```

run. 

---

<a href="../src/pyquanda/ansible/__init__.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `status_handler`

```python
status_handler(args: Dict, **kwargs)
```

status_handler. 



**Args:**
 
 - <b>`args`</b>:  ansible event args 
 - <b>`kwargs`</b>:  Not used 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
