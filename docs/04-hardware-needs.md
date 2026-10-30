# Hardware needs

You don't need a top-of-the-line computer to run a local LLM. What matters most is **RAM** (memory), and to a lesser extent, your **GPU** (graphics chip) and **CPU** (processor).

## The one number that matters: RAM

A model needs to fit in memory to run. As a rule of thumb:

```
RAM needed ≈ (parameter count in billions) + 2 GB overhead
```

So a 7B model needs roughly 9 GB of free RAM. A 3B model needs about 5 GB.

## How to check your RAM

- **Mac:** Apple menu → About This Mac → Memory
- **Windows:** Settings → System → About → Device specifications → Installed RAM
- **Linux:** Open a terminal and run `free -h`

## Matching models to your computer

| Total RAM | Comfortable models | Notes |
|-----------|-------------------|-------|
| 4–8 GB | `llama3.2:1b`, `llama3.2:3b` | Close other apps while running |
| 8–16 GB | `llama3.2:3b`, `qwen2.5:7b`, `llama3.1:8b` | Sweet spot for beginners |
| 16–32 GB | `qwen2.5:7b`, `llama3.1:8b`, `deepseek-r1:14b` | Can run larger or multiple models |
| 32 GB+ | `llama3.1:70b`, `deepseek-r1:32b` | Serious local AI workstation |

## GPU vs CPU

Ollama can run models on your CPU alone, but it's much faster with a GPU.

- **CPU only:** Works everywhere, slower. Fine for small models and learning.
- **GPU (NVIDIA, AMD, Apple Silicon):** Much faster, especially for larger models.
- **Apple Silicon Macs (M1/M2/M3/M4):** The unified memory architecture makes these excellent for local LLMs — the GPU shares the system RAM.

If you're unsure, just install Ollama and try. It will use whatever hardware is available.

## Disk space

Models are large files. A 7B model is roughly 4–5 GB. A 14B model is about 8–9 GB. Make sure you have at least 20–30 GB of free disk space before downloading several models.

## Quick hardware checklist

Before you install Ollama:

- [ ] I know how much RAM my computer has
- [ ] I have at least 20 GB of free disk space
- [ ] I've picked a first model that fits my RAM (see [Model sizes](03-model-sizes.md))

If your computer is on the smaller side, start with a 1B or 3B model. You can upgrade later.

## Next step

Ready to install? Go to [Installing Ollama](05-install-ollama.md).

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
