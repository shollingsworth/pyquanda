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


---

<a href="../src/pyquanda/ansible/__init__.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Ansible`
Ansible. 




---

<a href="../src/pyquanda/ansible/__init__.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `copy_dirs`

```python
copy_dirs() → List[str]
```

copy_dirs. 



**Args:**
 



**Returns:**
 
 - <b>`List[str]`</b>:  list of directory strings 

---

<a href="../src/pyquanda/ansible/__init__.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `event_handler`

```python
event_handler(evt_dct: Dict) → bool
```





---

<a href="../src/pyquanda/ansible/__init__.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `run_all`

```python
run_all(modules_directory: Path, debug_only: bool)
```

run. 

---

<a href="../src/pyquanda/ansible/__init__.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `run_single`

```python
run_single(module_path: Path, debug_only: bool)
```

run. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
