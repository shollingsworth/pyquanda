<!-- markdownlint-disable -->

<a href="../src/pyquanda/cli/subcommands.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `cli.subcommands`
cli subcommands. 

**Global Variables**
---------------
- **MOCK_CONFIG**
- **XONSH_TXT**

---

<a href="../src/pyquanda/cli/subcommands.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `yesno`

```python
yesno(question: str) → bool
```

Simple Yes/No Function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CreateNewModule`
CreateNewModule. 

<a href="../src/pyquanda/cli/subcommands.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_new_module`

```python
create_new_module(args: Namespace)
```

Run main function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunModule`
RunModule. 

<a href="../src/pyquanda/cli/subcommands.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunAllModules`
RunAllModules. 

<a href="../src/pyquanda/cli/subcommands.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AssembleQuestions`
AssembleQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TestQuestions`
TestQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Demo`
Demo. 

<a href="../src/pyquanda/cli/subcommands.py#L258"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SaveUserData`
SaveUserData. 

<a href="../src/pyquanda/cli/subcommands.py#L298"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L333"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`
Bootstrap. 

<a href="../src/pyquanda/cli/subcommands.py#L336"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L357"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
