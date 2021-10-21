<!-- markdownlint-disable -->

<a href="../src/pyquanda/host/xonsh.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `host.xonsh`
XenSH question interface. 

**Global Variables**
---------------
- **HOOK_TYPE_QUESTIONABLE**
- **HOOK_TYPE_ANSWER**
- **HOOK_TYPE_XONSH_COMMAND_ENTERED**
- **RESTRICTED**
- **SUDO_OK**
- **MAX_ANSWER_LEN**

---

<a href="../src/pyquanda/host/xonsh.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `width`

```python
width()
```

width. 


---

<a href="../src/pyquanda/host/xonsh.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `height`

```python
height()
```

height. 


---

<a href="../src/pyquanda/host/xonsh.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `twrap`

```python
twrap(content: str) → str
```

twrap. 



**Args:**
 
 - <b>`content`</b> (str):  content 



**Returns:**
 
 - <b>`str`</b>:  return wrapped string 


---

<a href="../src/pyquanda/host/xonsh.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bash_filter`

```python
bash_filter(**kwargs) → None
```

bash_filter. 

Restricted stuff is here 



**Args:**
 

**kwargs:**
 


---

<a href="../src/pyquanda/host/xonsh.py#L311"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `cmd_event`

```python
cmd_event(**kwargs) → None
```

cmd_event. 



**Args:**
 

**kwargs:**
 


---

<a href="../src/pyquanda/host/xonsh.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `QuestionPrompt`
QuestionPrompt. 

<a href="../src/pyquanda/host/xonsh.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

__init__. 




---

<a href="../src/pyquanda/host/xonsh.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `answer`

```python
answer(args: List, stdin: Optional[TextIOWrapper] = None)
```

answer. 



**Args:**
 
 - <b>`args`</b> (List):  args 
 - <b>`stdin`</b> (Optional[TextIOWrapper]):  stdin 

---

<a href="../src/pyquanda/host/xonsh.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `auto_intro`

```python
auto_intro()
```

auto_intro. 

---

<a href="../src/pyquanda/host/xonsh.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `command_entered`

```python
command_entered(**kwargs)
```

command_entered. 



**Args:**
 

**kwargs:**
 

---

<a href="../src/pyquanda/host/xonsh.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `prompt`

```python
prompt() → str
```

prompt. 



**Args:**
 



**Returns:**
 
 - <b>`str`</b>:  return prompt string 

---

<a href="../src/pyquanda/host/xonsh.py#L243"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run_background_task`

```python
run_background_task(cmd: str)
```

start the process and send it into the background. 

---

<a href="../src/pyquanda/host/xonsh.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `toggle_command_show`

```python
toggle_command_show()
```

toggle_command_show. 

---

<a href="../src/pyquanda/host/xonsh.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `toggle_toolbar`

```python
toggle_toolbar()
```

toggle_toolbar. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
