<!-- markdownlint-disable -->

<a href="../src/pyquanda/cli/subcommands.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `cli.subcommands`
cli subcommands. 

**Global Variables**
---------------
- **MOCK_CONFIG**
- **XONSH_TXT**

---

<a href="../src/pyquanda/cli/subcommands.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `yesno`

```python
yesno(question: str) → bool
```

Simple Yes/No Function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CreateNewModule`
CreateNewModule. 

<a href="../src/pyquanda/cli/subcommands.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_new_module`

```python
create_new_module(args: Namespace)
```

Run main function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunModule`
RunModule. 

<a href="../src/pyquanda/cli/subcommands.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunAllModules`
RunAllModules. 

<a href="../src/pyquanda/cli/subcommands.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AssembleQuestions`
AssembleQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TestQuestions`
TestQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 



**Raises:**
 
 - <b>`SystemExit`</b>:  if there is an issue 


---

<a href="../src/pyquanda/cli/subcommands.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Demo`
Demo. 

<a href="../src/pyquanda/cli/subcommands.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SaveUserData`
SaveUserData. 

<a href="../src/pyquanda/cli/subcommands.py#L320"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L340"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L358"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`
Bootstrap. 

<a href="../src/pyquanda/cli/subcommands.py#L361"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent: MainParser) → None
```

__init__. 



**Args:**
 
 - <b>`parent`</b> (MainParser):  parent 



**Returns:**
 None: 




---

<a href="../src/pyquanda/cli/subcommands.py#L383"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 

**Raises:**
 
 - <b>`SystemExit`</b>:  on error 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
