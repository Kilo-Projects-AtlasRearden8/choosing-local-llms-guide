# What is Ollama?

**Ollama** is a free, open-source tool that lets you run large language models (LLMs) on your own computer.

Think of an LLM as a program that reads and writes text — like a very advanced autocomplete. Normally, these models run on giant servers owned by big tech companies. When you chat with one, your messages travel over the internet to their servers and back. Ollama flips that: it downloads a model to your computer and runs it there, locally.

## Why use Ollama?

- **Privacy.** Your chats never leave your machine. No company reads them.
- **No account.** No email, no credit card, no sign-up.
- **No monthly fee.** Ollama and most models are free to use.
- **Works offline.** Once a model is downloaded, you don't need the internet.
- **Simple.** One command downloads and runs a model. No complex setup.

## What Ollama does

Ollama handles three things for you:

1. **Downloading models** — It fetches the model files from the internet the first time you use one.
2. **Running models** — It starts the model on your computer's CPU or GPU.
3. **Chatting** — It gives you a simple way to send messages and get replies, either in your terminal or through apps that connect to it.

## What Ollama is not

- Ollama is not a model itself. It's the *runner* — the software that loads and executes models.
- Ollama is not a website. It runs on your computer.
- Ollama does not require an API key.

## The client-server model

When Ollama is running, it acts as a small server on your computer (usually at `http://localhost:11434`). You can talk to it:

- Directly in your terminal with `ollama run <model>`
- Through other apps and tools that connect to that local address
- Through your own simple programs (Ollama has a straightforward HTTP API)

Everything stays on your machine unless *you* choose to connect to something else.

## Is it safe?

Ollama is open source and widely used. Models are downloaded from Ollama's library, and you choose which ones to run. As with any software, only download models you trust, and keep Ollama updated.

## Next step

Now that you know what Ollama is, let's look at [model sizes](03-model-sizes.md) so you can pick one that fits your computer.

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
