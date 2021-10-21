<!-- markdownlint-disable -->

<a href="../src/pyquanda/cli/subcommands.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `cli.subcommands`
cli subcommands. 

**Global Variables**
---------------
- **MOCK_CONFIG**
- **XONSH_TXT**

---

<a href="../src/pyquanda/cli/subcommands.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `yesno`

```python
yesno(question: str) → bool
```

Simple Yes/No Function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CreateNewModule`
CreateNewModule. 

<a href="../src/pyquanda/cli/subcommands.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_new_module`

```python
create_new_module(args: Namespace)
```

Run main function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunModule`
RunModule. 

<a href="../src/pyquanda/cli/subcommands.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunAllModules`
RunAllModules. 

<a href="../src/pyquanda/cli/subcommands.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AssembleQuestions`
AssembleQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L197"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TestQuestions`
TestQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Demo`
Demo. 

<a href="../src/pyquanda/cli/subcommands.py#L267"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L284"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L304"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SaveUserData`
SaveUserData. 

<a href="../src/pyquanda/cli/subcommands.py#L307"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L325"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L341"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`
Bootstrap. 

<a href="../src/pyquanda/cli/subcommands.py#L344"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L365"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
