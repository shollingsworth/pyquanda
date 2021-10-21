<!-- markdownlint-disable -->

<a href="../src/pyquanda/host/intro.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `host.intro`
Introduction builder. 

**Global Variables**
---------------
- **ANSI_COLOR_NAMES**

---

<a href="../src/pyquanda/host/intro.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `show_all_colors`

```python
show_all_colors() → None
```

show_all_colors. 



**Args:**
 



**Returns:**
  None: 


---

<a href="../src/pyquanda/host/intro.py#L304"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `intro_load_pickle_b64`

```python
intro_load_pickle_b64(b64: str) → Intro
```

intro_load_pickle_b64. 



**Args:**
 
 - <b>`b64`</b> (str):  b64 



**Returns:**
 
 - <b>`Intro`</b>:  intro object 


---

<a href="../src/pyquanda/host/intro.py#L316"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `intro_export_b64`

```python
intro_export_b64(intro: Intro) → str
```

intro_export_b64. 



**Args:**
 
 - <b>`intro`</b> (Intro):  intro 



**Returns:**
 
 - <b>`str`</b>:  exported b64 encoded intro object 


---

<a href="../src/pyquanda/host/intro.py#L241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Intro`
Intro. 

<a href="../src/pyquanda/host/intro.py#L244"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(title: str, template_path: Path, config: Dict)
```

__init__. 



**Args:**
 
 - <b>`title`</b> (str):  title 
 - <b>`template_path`</b> (Path):  template_path 
 - <b>`config`</b> (Dict):  config 


---

#### <kbd>property</kbd> console

console. 



**Args:**
 



**Returns:**
  Console: 

---

#### <kbd>property</kbd> title

title. 



**Args:**
 



**Returns:**
  str: 



---

<a href="../src/pyquanda/host/intro.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `PADDING`

```python
PADDING(el: Any) → Padding
```

PADDING. 



**Args:**
 
 - <b>`el`</b> (Any):  el 



**Returns:**
 
 - <b>`Padding`</b>:  pad object 

---

<a href="../src/pyquanda/host/intro.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `code`

```python
code(code_dct: Dict) → None
```

code. 



**Args:**
 
 - <b>`code_dct`</b> (Dict):  code_dct 

---

<a href="../src/pyquanda/host/intro.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_code`

```python
get_code(code_dct: Dict) → Syntax
```

get_code. 



**Args:**
 
 - <b>`code_dct`</b> (Dict):  code_dct 



**Returns:**
 
 - <b>`Syntax`</b>:  code syntax object syntax 

---

<a href="../src/pyquanda/host/intro.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `header`

```python
header(header_txt: str) → None
```

header. 



**Args:**
 
 - <b>`header_txt`</b> (str):  header_txt 

---

<a href="../src/pyquanda/host/intro.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `j2`

```python
j2(filename: str) → None
```

j2. 



**Args:**
 
 - <b>`filename`</b> (str):  filename 

---

<a href="../src/pyquanda/host/intro.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `load`

```python
load(datafile: Path, values: List[Dict[str, str]]) → None
```

load. 



**Args:**
 
 - <b>`datafile`</b> (Path):  datafile 
 - <b>`values`</b> (List[Dict[str, str]]):  values 



**Raises:**
 
 - <b>`PreCheckFail`</b>:  if validation fails 

---

<a href="../src/pyquanda/host/intro.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run() → None
```

run. 

---

<a href="../src/pyquanda/host/intro.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `table`

```python
table(dct: Dict) → None
```

table. 



**Args:**
 
 - <b>`dct`</b> (Dict):  dct 



**Returns:**
 None: 

---

<a href="../src/pyquanda/host/intro.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `txt`

```python
txt(text: str) → None
```

txt. 



**Args:**
 
 - <b>`text`</b> (str):  text 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
