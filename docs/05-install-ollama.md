# Installing Ollama

Ollama is free and works on Mac, Windows, and Linux. Pick your operating system below and follow the steps.

## Mac

1. Go to https://ollama.com/download
2. Download the Ollama app for macOS
3. Open the downloaded file and drag Ollama into your Applications folder
4. Open Ollama from your Applications folder
5. Ollama will show a small icon in your menu bar — that means it's running

To verify, open Terminal and type:

```
ollama --version
```

You should see a version number.

## Windows

1. Go to https://ollama.com/download
2. Download the Ollama installer for Windows
3. Run the installer and follow the prompts
4. Ollama runs in the background with an icon in your system tray

To verify, open PowerShell or Command Prompt and type:

```
ollama --version
```

You should see a version number.

## Linux

1. Open a terminal
2. Run the install script:

```
curl -fsSL https://ollama.com/install.sh | sh
```

3. The script installs Ollama and starts it as a background service

To verify:

```
ollama --version
```

You should see a version number.

## What the install does

- Installs the Ollama application
- Starts a local server on your computer (usually at `http://localhost:11434`)
- Sets up the `ollama` command in your terminal

Nothing is sent to any cloud service during installation other than downloading the Ollama program itself.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `ollama: command not found` | Restart your terminal after installing, or reinstall |
| Ollama won't start | Make sure you have at least 4 GB of RAM available |
| Port already in use | Another program is using port 11434; close it and retry |

## Next step

Ollama is installed. Now let's [run your first model](06-running-models.md).

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
