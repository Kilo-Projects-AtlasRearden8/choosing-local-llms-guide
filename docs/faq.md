# FAQ

## Do I need to know how to code?

No. Everything in this guide uses simple commands you copy and paste into your terminal.

## Does Ollama cost money?

No. Ollama is free and open source. The models in its library are also free to use.

## Do I need an internet connection?

Only to download Ollama and the models the first time. After that, everything works offline.

## Will this make my computer slow?

While a model is running, it uses RAM and some CPU/GPU. Close other heavy apps if your computer feels slow. When you're done, type `/bye` to stop the model.

## Can I run multiple models?

You can download several models, but only one runs at a time in a chat session. Remove models you're not using to free disk space with `ollama rm <model>`.

## Is my data private?

Yes — your chats stay on your computer. See [Privacy](07-privacy.md) for details.

## What if a model is too slow?

Try a smaller model (fewer billion parameters) or a heavier quantization trade-off (e.g., q4 instead of q8). See [Model sizes](03-model-sizes.md).

## Where do I find more models?

Visit https://ollama.com/library

## Can I build apps that use Ollama?

Yes. Ollama runs a local server at `http://localhost:11434` with a simple HTTP API. You can connect programs, scripts, and other tools to it.

## Is this medical advice?

No. If you're a healthcare worker exploring AI, this is educational only — never medical advice. Consult a qualified professional for medical decisions.

## Who made this?

Published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Dylan Asdale is a registered nurse turned AI author and founder of Asdale Dynamics, LLC. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a friend would": plain English, step by step, never condescending.

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
