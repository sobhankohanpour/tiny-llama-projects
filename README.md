# Tiny LLaMA Projects

This repository contains a collection of beginner-friendly projects demonstrating how to build applications with **LLaMA models**, **LlamaIndex**, and **Ollama**, primarily using **JupyterLab** notebooks.


## Prerequisites

* Python 3.9+
* JupyterLab or Jupyter Notebook
* A supported operating system for Ollama (Linux, macOS, or Windows via WSL)


## Installing Required Python Packages

If you have an unstable or slow internet connection, it is recommended to use the following command to reduce the likelihood of installation failures by increasing timeout and retry limits:

```bash
pip install \
  llama-index-readers-file \
  llama-index-llms-ollama \
  llama-index-embeddings-huggingface \
  --timeout 120 \
  --retries 20
````

### Additional Packages for PDF and Embeddings

For reading PDFs and using a dedicated embedding model, install:

```bash
pip install llama-index-embeddings-ollama
```

> 🔹 Use a dedicated embedding model
> Keep **Qwen** for answering questions
> Use **Nomic** (or similar) for embeddings

## Installing Ollama

### Step 1: Download Ollama

First, install **Ollama** by visiting the official releases page:

```
https://github.com/ollama/ollama/releases
```

Download the appropriate file for your operating system.
For example, on Linux (AMD64):

```
https://github.com/ollama/ollama/releases/download/v0.13.5/ollama-linux-amd64.tgz
```

### Step 2: Install Ollama from `ollama-linux-amd64.tgz` (WSL/Linux)

#### 1. Navigate to the Downloads directory from within WSL

```bash
cd /mnt/c/Users/sobhan/Downloads
```

Verify the file exists:

```bash
ls | grep ollama
```

#### 2. Extract the archive

```bash
tar -xzf ollama-linux-amd64.tgz
```

#### 3. Make the Ollama binary executable

```bash
chmod +x bin/ollama
```

#### 4. Move the binary to your system PATH

```bash
sudo mv bin/ollama /usr/local/bin/
```

#### 5. Move the library files

```bash
sudo mkdir -p /usr/share/ollama
sudo mv lib /usr/share/ollama/
```

#### 6. Verify the installation

```bash
ollama --version
```

If a version number is displayed, the installation was successful 🎉

## Running Ollama

### Start the Ollama server

In one terminal window, run:

```bash
ollama serve
```

### Download or Run Models

For lightweight local inference, you can also pull:

```bash
ollama pull qwen3:1.7b
```

Alternatively, run a model directly:

```
ollama run qwen3:1.7b
```

To verify that the models have been installed successfully, run:

```
ollama list
```

Example output:

```
NAME          ID              SIZE      MODIFIED
qwen3:1.7b    8f68893c685c    1.4 GB    5 minutes ago
```

Also, pull the required models:

```bash
ollama pull nomic-embed-text
ollama pull qwen3:0.6b
```

## Additional Python Dependencies

Install the Hugging Face LLM integration:

```bash
pip install llama-index-llms-huggingface
```

Then install all remaining project dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
tiny-llama-projects/
│
├── README.md
├── requirements.txt
├── 01 Your First LlamaIndex Project/
│   ├── ask_your_pdf.ipynb
│   └── data/
│       └── Smarter-SCADA-Alarming.pdf
```

## Getting Started

1. Ensure Ollama is running (`ollama serve`).
2. Open JupyterLab or Jupyter Notebook.
3. Navigate to `01 Your First LlamaIndex Project`.
4. Open `ask_your_pdf.ipynb`.
5. Follow the notebook instructions to interact with your PDF using a LLaMA-based LLM.

## License

This project is provided for educational and experimental purposes. Please review individual dependencies for their respective licenses.
