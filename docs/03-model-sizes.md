# Model sizes

When you browse Ollama's model library, you'll see names like `llama3.2:3b`, `qwen2.5:7b-instruct-q4_K_M`, and `deepseek-r1:14b`. These names tell you three things:

1. **The model family** (e.g., llama3.2, qwen2.5, deepseek-r1)
2. **The parameter count** (e.g., 3b, 7b, 14b — the "b" means billion)
3. **The quantization** (e.g., q4_K_M, q8_0 — how much the model is compressed)

Let's break each part down.

## Parameters: the "b" number

Parameters are the internal connections a model learns during training. More parameters generally mean a smarter, more capable model — but also more memory and a slower computer to run it.

| Size | Rough parameters | What it's good for | Typical RAM needed |
|------|-----------------|--------------------|-------------------|
| Small | 1B–3B | Simple Q&A, drafting emails, summarization | 4–8 GB |
| Medium | 7B–8B | General chat, writing, coding help | 8–16 GB |
| Large | 13B–14B | Stronger reasoning, coding, analysis | 16–32 GB |
| Extra large | 32B–70B+ | Complex tasks, but needs serious hardware | 32–80+ GB |

**Rule of thumb:** A model needs roughly 1 GB of RAM per billion parameters, plus a little overhead for your operating system and other apps. A 7B model needs about 8 GB of free RAM to run comfortably.

## Quantization: the q4_K_M part

Full-precision models are huge. Quantization compresses them so they use less memory and run faster, with a small trade-off in quality.

Common quantization levels you'll see:

| Quantization | Meaning | Quality | Size |
|-------------|---------|---------|------|
| q4_K_M | 4-bit, medium | Good for most uses | ~40–50% of full size |
| q5_K_M | 5-bit, medium | Better quality | ~50–60% |
| q8_0 | 8-bit | Near full quality | ~80–90% |
| f16 | 16-bit (full precision) | Best quality | Largest |

**For beginners:** Start with a `q4_K_M` or `q5_K_M` model. They're small, fast, and perfectly good for learning.

## Putting it together: reading a model name

`llama3.2:3b` — Llama 3.2, 3 billion parameters, default quantization

`qwen2.5:7b-instruct-q4_K_M` — Qwen 2.5, 7B parameters, instruction-tuned, 4-bit quantization

`deepseek-r1:14b` — DeepSeek R1, 14B parameters

The `instruct` or `chat` suffix means the model is fine-tuned to follow instructions and converse — good for general use.

## Recommended first models

If you're new to local LLMs, start here:

| Your RAM | Suggested model | Why |
|----------|----------------|-----|
| 8 GB | `llama3.2:3b` | Tiny, fast, great for learning |
| 16 GB | `qwen2.5:7b-instruct-q4_K_M` | Strong general model, comfortable fit |
| 32 GB+ | `llama3.1:8b` or `deepseek-r1:14b` | More capable, still runs well |

You can always try a model and remove it if it's too slow. There's no cost to experiment.

## How to see available models

After installing Ollama, run:

```
ollama list
```

To see what's in the Ollama library, visit https://ollama.com/library

## Next step

Now that you know how to read model sizes, let's check whether your computer has the hardware to run one: [Hardware needs](04-hardware-needs.md).

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
