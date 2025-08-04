# Local AI CPU Project 🤖

Welcome to my first project using the Ollama library! This project is a simple demonstration of how to get started with local Large Language Models (LLMs) in Python.

### What is Ollama?

Ollama is a fantastic tool that allows you to run open-source large language models locally on your machine. This means you can have a powerful AI assistant without needing an internet connection or paying for cloud services.

---

## 🚀 Getting Started

Follow these steps to set up the project and run your first LLM.

### 1. Ollama Installation

First, you need to download and install Ollama for your operating system.

💻 **For Windows:** Download the installer from the official website.

* **Download Link:** [https://ollama.com/download/windows](https://ollama.com/download/windows)

Once installed, Ollama will run in the background.

### 2. Python Installation & Environment Setup

If you don't have Python installed, you can get it from the Microsoft Store or the official website. You can also use the following command in PowerShell:

```shell
winget install Python.Python.3.11
```
Once Python is installed, you can install the ollama Python library with pip.
```Shell
pip install ollama
```

3. Downloading the Mistral Model
Next, you need to download a model to run. We will use the Mistral model, a powerful and efficient model for a variety of tasks.

Mistral Model Page: https://ollama.com/library/mistral

You can download the model directly from your terminal using Ollama's CLI.

```Shell
ollama run mistral
```
This command will automatically download the Mistral model and start a chat session.

To run this code, simply open your terminal, navigate to the project directory, and execute:

```Shell
python localAI.py
```

