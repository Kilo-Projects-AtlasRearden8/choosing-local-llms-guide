# Running your first model

Ollama is installed. Let's download and chat with a model.

## Step 1: Pick a model

If you have 8–16 GB of RAM, a great first model is:

```
qwen2.5:7b-instruct-q4_K_M
```

If you have less RAM, try:

```
llama3.2:3b
```

See [Model sizes](03-model-sizes.md) and [Hardware needs](04-hardware-needs.md) for help choosing.

## Step 2: Download and run the model

Open your terminal and type:

```
ollama run qwen2.5:7b-instruct-q4_K_M
```

The first time, Ollama will download the model (this may take a few minutes depending on your internet speed). After that, you'll see a prompt like:

```
>>> 
```

## Step 3: Chat with the model

Type a message and press Enter:

```
>>> Hello! Can you tell me a short joke?
```

The model will reply. Keep typing to continue the conversation.

To end the session, type:

```
/bye
```

Or press `Ctrl+D` or `Ctrl+C`.

## Step 4: See what you've downloaded

```
ollama list
```

This shows all models on your computer and how much space they use.

## Step 5: Remove a model you don't need

```
ollama rm qwen2.5:7b-instruct-q4_K_M
```

This frees up disk space.

## Other useful commands

| Command | What it does |
|---------|-------------|
| `ollama pull <model>` | Download a model without starting a chat |
| `ollama run <model>` | Download (if needed) and start chatting |
| `ollama list` | Show downloaded models |
| `ollama rm <model>` | Delete a model |
| `ollama serve` | Start the Ollama server manually |
| `ollama --version` | Show Ollama version |

## Running in the background

If you want Ollama to keep running so other apps can connect to it, start it with:

```
ollama serve
```

Then leave that terminal window open. Ollama will listen at `http://localhost:11434`.

## Tips for beginners

- The first download is the slowest. Subsequent models share files, so later downloads are faster.
- If a model feels slow, try a smaller one (fewer billion parameters).
- You can have multiple models downloaded and switch between them.
- Everything happens on your computer — your chat history is stored locally.

## Next step

Now that you can run a model, read [Privacy](07-privacy.md) to understand why your data stays on your machine, then use the [model-selection worksheet](08-model-selection-worksheet.md) to choose your first model thoughtfully.

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
