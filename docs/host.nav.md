<!-- markdownlint-disable -->

<a href="../src/pyquanda/host/nav.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `host.nav`
Navigation related utils. 


---

<a href="../src/pyquanda/host/nav.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `color`

```python
color(color_name: str, txt: str) → str
```

color. 



**Args:**
 
 - <b>`color_name`</b> (str):  color 
 - <b>`txt`</b> (str):  txt 



**Returns:**
 
 - <b>`str`</b>:  color ansi 


---

<a href="../src/pyquanda/host/nav.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Navigation`
Navigation. 

<a href="../src/pyquanda/host/nav.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

__init__. 


---

#### <kbd>property</kbd> all_questions

all_questions. 

---

#### <kbd>property</kbd> background_commands

background_commands. 



**Args:**
 



**Returns:**
  List: 

---

#### <kbd>property</kbd> current_module_index

current_module_index. 

---

#### <kbd>property</kbd> current_module_name

current_module_name. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> current_question

current_question. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> current_question_index

current_question_index. 

---

#### <kbd>property</kbd> current_question_set

current_question_set. 



**Args:**
 



**Returns:**
  List: 

---

#### <kbd>property</kbd> description

description. 



**Args:**
 



**Returns:**
  str: 

---

#### <kbd>property</kbd> has_next_module

has_next_module. 

---

#### <kbd>property</kbd> has_next_question

has_next_question. 

---

#### <kbd>property</kbd> has_previous_module

has_previous_module. 

---

#### <kbd>property</kbd> has_previous_question

has_previous_question. 

---

#### <kbd>property</kbd> introduction

introduction. 



**Args:**
 



**Returns:**
  Intro: 

---

#### <kbd>property</kbd> key

key. 

---

#### <kbd>property</kbd> main_intro

main_intro. 



**Args:**
 



**Returns:**
  Intro: 

---

#### <kbd>property</kbd> mod_x_of_y

mod_x_of_y. 

---

#### <kbd>property</kbd> percentage

percentage. 



**Args:**
 



**Returns:**
  int: 

---

#### <kbd>property</kbd> question_x_of_y

question_x_of_y. 

---

#### <kbd>property</kbd> seen_intro

seen_intro. 

---

#### <kbd>property</kbd> seen_main_intro

seen_main_intro. 



---

<a href="../src/pyquanda/host/nav.py#L336"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `as_dict`

```python
as_dict() → Dict[str, str]
```

as_dict. 



**Args:**
 



**Returns:**
 
 - <b>`Dict[str, str]`</b>:  object dict representation 

---

<a href="../src/pyquanda/host/nav.py#L316"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `go_next`

```python
go_next()
```

next. 

---

<a href="../src/pyquanda/host/nav.py#L326"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `go_previous`

```python
go_previous()
```

previous. 


---

<a href="../src/pyquanda/host/nav.py#L365"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `NavFooter`
NavFooter. 




---

<a href="../src/pyquanda/host/nav.py#L368"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(
    nav: Navigation,
    command_map: Dict[str, str],
    show: bool,
    show_cmds: bool
) → str
```

get. 



**Args:**
 
 - <b>`nav`</b> (Navigation):  nav 
 - <b>`command_map`</b> (Dict[str, str]):  command_map 
 - <b>`show`</b> (bool):  show 
 - <b>`show_cmds`</b> (bool):  show_cmds 



**Returns:**
 
 - <b>`str`</b>:  navigation footer 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
