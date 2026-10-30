# Model-selection worksheet

Use this worksheet to choose your first local LLM. Print it out, fill it in, and keep it next to your computer.

You can also find an interactive version in the static site (`static/worksheet.html`) that prints on one sheet.

## Step 1: Check your computer

1. How much RAM does your computer have? ________ GB

   *(Mac: Apple menu → About This Mac → Memory | Windows: Settings → System → About | Linux: `free -h`)*

2. How much free disk space do you have? ________ GB

   *(Allow 5–10 GB per model)*

3. Do you have a GPU? (NVIDIA, AMD, or Apple Silicon M1/M2/M3/M4) □ Yes □ No

## Step 2: What will you use it for?

Check all that apply:

□ Learning about AI  
□ Simple questions and answers  
□ Writing emails or messages  
□ Summarizing text  
□ Coding help  
□ Creative writing  
□ Other: _______________

## Step 3: Choose a model size

Based on your RAM, pick a starting point:

| Your RAM | Suggested first model |
|----------|----------------------|
| 4–8 GB | `llama3.2:3b` |
| 8–16 GB | `qwen2.5:7b-instruct-q4_K_M` |
| 16–32 GB | `llama3.1:8b` or `deepseek-r1:14b` |
| 32 GB+ | `llama3.1:70b` (advanced) |

My chosen model: ________________________

## Step 4: Download and test

Run this in your terminal:

```
ollama run <your-model>
```

Replace `<your-model>` with your chosen model name.

Did it download successfully? □ Yes □ No  
Did it respond to a message? □ Yes □ No  
Was it fast enough? □ Yes □ No

## Step 5: Notes

What worked well:

________________________________________________

What to try next time:

________________________________________________

---

Print this page and keep it as your local AI quick reference.

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
