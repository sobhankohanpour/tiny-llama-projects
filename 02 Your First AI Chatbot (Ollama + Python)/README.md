# Your First AI Chatbot (Ollama + Python)

A minimal Python chatbot that uses **Ollama** to run a local large language model and respond to user prompts.


## Requirements

- Python 3.13+
- Ollama installed
- At least one Ollama model installed (e.g. `qwen3:0.6b`)


## Setup & Run

### 1. Start the Ollama server

Open a terminal and run:
```bash
ollama serve
````

Keep this terminal running.


### 2. Run the chatbot

Open another terminal and make sure you are inside the project folder:

```text
02 Your First AI Chatbot (Ollama + Python)
```

Then run:

```bash
python src/bot.py
```


## Example Output

The chatbot sends a prompt to the model:

> *Why is the sky blue?*

And prints the model’s response directly to the terminal.


## Project Structure

```text
.
├── src/
│   └── bot.py
└── README.md
```


## Model Used

* `qwen3:0.6b` (configurable in `bot.py`)
