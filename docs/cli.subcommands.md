<!-- markdownlint-disable -->

<a href="../src/pyquanda/cli/subcommands.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `cli.subcommands`
cli subcommands. 

**Global Variables**
---------------
- **MOCK_CONFIG**
- **XONSH_TXT**

---

<a href="../src/pyquanda/cli/subcommands.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `yesno`

```python
yesno(question: str) → bool
```

Simple Yes/No Function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CreateNewModule`
CreateNewModule. 

<a href="../src/pyquanda/cli/subcommands.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_new_module`

```python
create_new_module(args: Namespace)
```

Run main function. 


---

<a href="../src/pyquanda/cli/subcommands.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunModule`
RunModule. 

<a href="../src/pyquanda/cli/subcommands.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RunAllModules`
RunAllModules. 

<a href="../src/pyquanda/cli/subcommands.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AssembleQuestions`
AssembleQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L196"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TestQuestions`
TestQuestions. 

<a href="../src/pyquanda/cli/subcommands.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L266"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Demo`
Demo. 

<a href="../src/pyquanda/cli/subcommands.py#L269"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L288"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(args: Namespace)
```

run. 



**Args:**
 
 - <b>`args`</b> (argparse.Namespace):  args 


---

<a href="../src/pyquanda/cli/subcommands.py#L334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SaveUserData`
SaveUserData. 

<a href="../src/pyquanda/cli/subcommands.py#L337"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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


---

<a href="../src/pyquanda/cli/subcommands.py#L374"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`
Bootstrap. 

<a href="../src/pyquanda/cli/subcommands.py#L377"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/pyquanda/cli/subcommands.py#L398"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
