# Privacy

One of the best reasons to run a local LLM with Ollama: **nothing leaves your computer.**

## What "local" means

When you chat with a model through Ollama:

- Your messages stay on your machine
- The model runs on your CPU or GPU
- Responses are generated locally
- No data is sent to Ollama's servers (after the initial model download)
- No company reads your conversations

The only thing that leaves your computer is the initial download of the model file itself. After that, you can unplug your internet and Ollama keeps working.

## What Ollama does not do

- Ollama does not require an account
- Ollama does not ask for your email
- Ollama does not sell your data
- Ollama does not train on your conversations
- Ollama does not phone home with your chat content

## Where your data lives

Ollama stores models and chat data on your computer, typically in:

- **Mac:** `~/.ollama`
- **Linux:** `~/.ollama`
- **Windows:** `C:\Users\<yourname>\.ollama`

You can back up, move, or delete this folder at any time.

## Comparison: local vs cloud

| | Local (Ollama) | Cloud AI service |
|---|---------------|------------------|
| Data leaves your computer | No | Yes |
| Account required | No | Usually |
| Monthly fee | No | Often |
| Works offline | Yes | No |
| Company reads your chats | No | Possibly |

## Good privacy habits

- Only download models from sources you trust (Ollama's official library is a good default)
- Don't paste passwords, API keys, or other secrets into any AI — local or cloud
- Keep Ollama updated
- If you're sharing your computer, remember that anyone with access to your user account can read the local chat data

## A reminder

This guide is educational. If you're handling sensitive personal information, consider talking to a professional about your specific privacy needs.

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
