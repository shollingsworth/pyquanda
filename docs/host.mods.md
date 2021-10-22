<!-- markdownlint-disable -->

<a href="../src/pyquanda/host/mods.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `host.mods`
Abstract method for other modules. 

**Global Variables**
---------------
- **ME**: # -*- coding: utf-8 -*-

- **TYPE_PROBLEM**
- **TYPE_SYSTEM**
- **TYPE_INTRO**
- **TYPES**


---

<a href="../src/pyquanda/host/mods.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseModule`
Module interface. 

<a href="../src/pyquanda/host/mods.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: Path)
```

initialize class. 


---

#### <kbd>property</kbd> log

log. 



**Args:**
 



**Returns:**
  Logger: 

---

#### <kbd>property</kbd> network_ports

network_ports. 



**Args:**
 



**Returns:**
  List[Dict[str, int]]: 



---

<a href="../src/pyquanda/host/mods.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  Dict representing the questions object 


---

<a href="../src/pyquanda/host/mods.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SystemModule`




<a href="../src/pyquanda/host/mods.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: Path)
```






---

#### <kbd>property</kbd> log

log. 



**Args:**
 



**Returns:**
  Logger: 

---

#### <kbd>property</kbd> network_ports

network_ports. 



**Args:**
 



**Returns:**
  List[Dict[str, int]]: 



---

<a href="../src/pyquanda/host/mods.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  Dict representing the questions object 


---

<a href="../src/pyquanda/host/mods.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `QuestionModule`




<a href="../src/pyquanda/host/mods.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: Path)
```






---

#### <kbd>property</kbd> log

log. 



**Args:**
 



**Returns:**
  Logger: 

---

#### <kbd>property</kbd> network_ports

network_ports. 



**Args:**
 



**Returns:**
  List[Dict[str, int]]: 

---

#### <kbd>property</kbd> question_intro

question_intro. 



**Args:**
 



**Returns:**
  Intro: 

---

#### <kbd>property</kbd> questions

questions. 



**Args:**
 



**Returns:**
  List[str]: 

---

#### <kbd>property</kbd> runtime_background_processes

runtime_background_processes. 



**Args:**
 



**Returns:**
  List[str]: 



---

<a href="../src/pyquanda/host/mods.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  Dict representing the questions object 

---

<a href="../src/pyquanda/host/mods.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `question_export_entry`

```python
question_export_entry() → Dict[str, Any]
```

question_export_entry. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, Any]`</b>:  export ready to insert into questions.json 


---

<a href="../src/pyquanda/host/mods.py#L203"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MainIntroModule`




<a href="../src/pyquanda/host/mods.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(path: Path)
```






---

#### <kbd>property</kbd> log

log. 



**Args:**
 



**Returns:**
  Logger: 

---

#### <kbd>property</kbd> main_intro

question_intro. 



**Args:**
 



**Returns:**
  Intro: 

---

#### <kbd>property</kbd> network_ports

network_ports. 



**Args:**
 



**Returns:**
  List[Dict[str, int]]: 



---

<a href="../src/pyquanda/host/mods.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  Dict representing the questions object 

---

<a href="../src/pyquanda/host/mods.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `main_info_export_entry`

```python
main_info_export_entry() → Dict[str, Any]
```






---

<a href="../src/pyquanda/host/mods.py#L231"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ModulesCollection`
Collection of modules. 




---

<a href="../src/pyquanda/host/mods.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `all`

```python
all() → Iterator[BaseModule]
```

all. 



**Args:**
 



**Yields:**
 
 - <b>`Module`</b>:  yield all modules 

---

<a href="../src/pyquanda/host/mods.py#L287"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `main_intro`

```python
main_intro() → MainIntroModule
```

main_intro. 



**Args:**
 



**Returns:**
 
 - <b>`Module`</b>:  main intro module 



**Raises:**
 
 - <b>`PreCheckFail`</b>:  if validation fails 

---

<a href="../src/pyquanda/host/mods.py#L320"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `network_ports`

```python
network_ports() → Iterator[Tuple[str, int]]
```

network_ports. 



**Args:**
 



**Yields:**
  Tuple[str, int] 

---

<a href="../src/pyquanda/host/mods.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `problem_collection`

```python
problem_collection() → Iterator[QuestionModule]
```

problem_collection. 



**Args:**
 



**Yields:**
  Module: 

---

<a href="../src/pyquanda/host/mods.py#L242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `register`

```python
register(module: BaseModule)
```

register. 



**Args:**
 
 - <b>`module`</b> (Module):  module 



**Raises:**
 
 - <b>`PreCheckFail`</b>:  if validation fails 

---

<a href="../src/pyquanda/host/mods.py#L308"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `system_collection`

```python
system_collection() → Iterator[SystemModule]
```

system_collection. 



**Args:**
 



**Yields:**
  Module: 


---

<a href="../src/pyquanda/host/mods.py#L334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ModuleLoader`







---

<a href="../src/pyquanda/host/mods.py#L341"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `load`

```python
load(path: Path)
```

initialize class. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
