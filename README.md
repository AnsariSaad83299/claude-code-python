# Claude-Code in Python  
> An autonomous AI coding agent that can read files, write code, and execute shell commands using LLM-powered tool calling and agent loops.

Claude-Code in Python is a minimal yet powerful implementation of how modern AI coding assistants like Claude Code and Copilot Workspace work internally.  
It demonstrates how Large Language Models can **reason, act, observe, and iterate** until a task is completed — without human intervention.

This is not a chatbot.  
It is an **agentic execution system**.

---

## 🚀 Overview

This project implements a full **tool-using autonomous agent loop** where the LLM:

- Chooses tools at runtime  
- Executes file operations  
- Runs shell commands  
- Observes outputs  
- Updates its reasoning  
- Repeats until completion

---

## ✨ Features

- 🔄 **Autonomous Agent Loop** – iterative think/act/observe cycle  
- 📁 **File System Tools** – read/write any project file  
- 💻 **Shell Command Tool** – run system commands safely  
- 🧠 **Structured Tool Calling** – JSON schema based function calls  
- 📝 **Conversation Memory** – multi-step context persistence  
- ⚡ **Python Core** – fast iteration, easy extension  

---

## 🧰 Available Tools

| Tool | Description | Parameters |
|------|------------|------------|
| `read_file` | Read file contents | `file_path` |
| `write_file` | Write content to file | `file_path`, `content` |
| `run_command` | Execute shell commands | `command` |

---

## 📦 Installation

### Prerequisites
- Python 3.10+  
- OpenRouter / OpenAI compatible API key  

### Setup

```bash
git clone https://github.com/yourusername/claude-code-python.git](https://github.com/AnsariSaad83299/claude-code-python.git)
cd claude-code-python

pip install -r requirements.txt

export OPENROUTER_API_KEY="your-api-key"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1
```
## ▶️ Usage

### Basic Example
```bash
python main.py "Create a file hello.txt with Hello World"
```

### Real-World Tasks

### Refactor code
```bash
python main.py "Refactor main.py to add proper error handling"
```


### Static analysis
```bash
python main.py "Find all .py files and remove unused imports"
```

### Multi-step workflow
```bash
python main.py "Create a utils module, add a reverse_string function, write tests, and run them"
```

## 🧠 Architecture
Agent Loop

1. The system runs an infinite reasoning loop:

2. Send conversation to LLM

3. Receive tool calls

4. Execute tools

5. Append results to memory

Repeat

The loop exits only when the model stops requesting tools.

## Tool Execution Flow
```bash
while True:
    response = llm(messages, tools)
    tool_calls = response.tool_calls

    if not tool_calls:
        break

    for call in tool_calls:
        result = execute_tool(call)
        messages.append(result)
```

## Conversation Management

The agent stores:

User prompts

Assistant messages

Tool calls

Tool results

This gives the LLM full situational awareness across steps.



## 🧪 What I Learned

- How LLM tool calling works in practice

- How to build non-stuck agent loops

- Managing long reasoning chains

- Safe file and shell execution

- Designing extensible tool systems

## 🧱 Built With

Python 3

OpenAI / OpenRouter compatible APIs

Claude / GPT tool-calling models

🎯 Inspired By

Built as part of the CodeCrafters AI Agent challenge, which breaks down how tools like Claude Code and Copilot Workspace work internally.
