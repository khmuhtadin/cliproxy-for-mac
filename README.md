# CLIProxy Installer for macOS, Linux & Windows

Automated installer for **CLIProxyAPIPlus**. This script simplifies the process of setting up custom AI models (Claude, Gemini, etc.) for use in Droid, Cursor, or other AI-powered editors.

It handles everything from installing dependencies (Go, Git), configuring the local proxy server, to managing updates.

## Features

* **Cross-Platform**: Works on **macOS**, **Linux**, and **Windows**.
* **Auto-Detect OS**: Automatically detects your operating system and runs the appropriate installation steps with a single command.
* **Smart Config Merge**: Intelligently adds new models to your `config.json` without overwriting your existing custom configurations.
* **Auto-Update**: Built-in self-updater keeps both the installer and the core CLIProxy binary up to date.
* **Auto-Build**: Clones the latest `CLIProxyAPIPlus` repository and builds the binary for your specific architecture.
* **Helper Scripts & Shortcuts**: Generates easy-to-use aliases (`cp-login`, `cp-start`, `cp-update`, `cp-claude`) for your terminal.
* **Droid Integration**: Automatically injects configurations for models like **Gemini 2.5 Pro**, **Qwen3**, **GLM 4.6**, **Kiro**, and more into `~/.factory/config.json`.

## Dashboard

The installer now includes a **dashboard** for monitoring and managing your CLIProxy server.

### Accessing the Dashboard:

After installation, use the `cp-db` command:

```bash
# Smart launcher - auto-starts server if needed, then opens dashboard
cp-db
```

Or access directly in your browser:
`http://localhost:8317/dashboard.html`

## Quick Install (macOS & Linux)

Open your Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/khmuhtadin/cliproxy-installer/main/install)"
```

*This single command automatically detects your OS and installs the necessary components.*

## Quick Install for Windows

Open **PowerShell** (Run as Administrator recommended) and execute:

```powershell
irm https://raw.githubusercontent.com/khmuhtadin/cliproxy-installer/main/install.ps1 | iex
```

## Menu Options

The installer provides an interactive menu:

1.  **Install Dependencies**: Installs Git and Go (via Homebrew on macOS, or package manager on Linux).
2.  **Install / Update CLIProxy Core**: Builds and installs the core binary.
3.  **FULL INSTALL** (Recommended): Does everything.

## How to Use

After installation, **restart your terminal** to load the shortcuts.

### 1. Login to Providers

Run the login script to authenticate with providers (Antigravity, Copilot, Gemini, etc.):

```bash
cp-login
```

*Select your preferred provider from the menu and follow the browser instructions.*

### 2. Start the Proxy

Start the local server. Keep this terminal window open while using Droid/Cursor:

```bash
cp-start
```

### 3. Stop the Proxy

To stop the running proxy server:

```bash
cp-stop
```

### 4. Update Everything

To update the installer script, the core binary, and add new models to your config:

```bash
cp-update
```

### 5. Claude Code Integration

Use the `cp-claude` command to run Claude Code with the proxy automatically configured.

```bash
# Interactive mode (select model from menu)
cp-claude

# Direct mode (specify model)
cp-claude --model "gpt-oss-120b-medium"
```

*Note: The server will auto-start if it is not already running.*

### 6. Usage in Droid/Cursor

1.  Open Droid.
2.  Go to Model selection.
3.  You will see new models like **"Claude Opus 4.5 Thinking [Antigravity]"**, **"Gemini 2.5 Pro"**, or **"Qwen3 Coder Plus"**.
4.  Select one and start chatting.

## Shortcuts Reference

* `cp-login` : Open the login menu.
* `cp-start` : Start the proxy server.
* `cp-stop`  : Stop the proxy server.
* `cp-update`: Auto-update the installer and core binary.
* `cp-db`    : Open the monitoring dashboard.
* `cp-claude`: Run Claude Code with proxy configuration.

## File Locations

| Platform | Binary | Config | Scripts | Droid Config |
| :--- | :--- | :--- | :--- | :--- |
| **macOS/Linux** | `~/bin/cliproxyapi-plus` | `~/.cli-proxy-api/config.yaml` | `~/.cli-proxy-api/scripts/` | `~/.factory/config.json` |
| **Windows** | `$HOME\bin\cliproxyapi-plus.exe` | `$HOME\.cli-proxy-api\config.yaml` | `$HOME\.cli-proxy-api\scripts\` | `$HOME\.factory\config.json` |

## Credits

  * Installer script ported and maintained by [khmuhtadin](https://github.com/khmuhtadin).
  * Core application by [router-for-me/CLIProxyAPIPlus](https://github.com/router-for-me/CLIProxyAPIPlus).

-----

*Disclaimer: This project is for educational purposes only. Please ensure you comply with the terms of service of the respective AI providers.*
