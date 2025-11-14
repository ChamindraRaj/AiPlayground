# AI Tools with Command Line Interface Support

**Research Date:** November 14, 2025

---

## 📖 Table of Contents
- [⭐ Beginner's Guide: Start Here!](#-beginners-guide-start-here)
- [🔑 Getting API Keys](#-getting-api-keys)
- [🌏 Local AI Tools (Offline & Free)](#-local-ai-tools-offline--free)
- [☁️ Cloud AI Tools (API Key Required)](#️-cloud-ai-tools-api-key-required)
- [🚀 Multi-Provider CLI Tools](#-multi-provider-cli-tools)
- [📊 Comparison Table](#-comparison-table)
- [🏆 Best CLI Options by Use Case](#-best-cli-options-by-use-case)
- [⚙️ Platform-Specific Installation Tips](#️-platform-specific-installation-tips)

---

## ⭐ Beginner's Guide: Start Here!

Welcome! This guide makes it easy to get started with AI in your terminal.

### What is a CLI?
A Command-Line Interface (CLI) is a text-based way to interact with programs. Instead of clicking buttons, you type commands. It's powerful, fast, and a core skill for developers.

### Why Use a CLI for AI?
*   **Speed:** Much faster than opening a browser.
*   **Automation:** Easily add AI to your scripts and workflows.
*   **Integration:** Works well with other command-line tools like `git`, `grep`, and `cat`.
*   **Privacy:** Local tools work offline and never send your data to the cloud.

### Key Concepts

*   **Local vs. Cloud Models:**
    *   🌏 **Local:** Runs 100% on your computer (`Ollama`, `LM Studio`). They are free, private, and work offline. You need a decent amount of RAM (8GB+).
    *   ☁️ **Cloud:** Runs on a company's servers (`ChatGPT`, `Gemini`). Requires an internet connection and an API key. Usually has a free tier, then you pay for what you use.

*   **SDK vs. CLI:**
    *   **SDK (Software Development Kit):** A library of code you use in your own programs (e.g., Python, Node.js).
    *   **CLI (Command-Line Interface):** A ready-to-use program you run directly from your terminal.

---

## 🔑 Getting API Keys

For Cloud AI tools, you need an API key. Think of it like a password for your code. **Keep it secret!**

Sign up on the provider's website and find the "API Keys" section in your account settings.

*   **OpenAI (ChatGPT):** [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
*   **Google (Gemini):** [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
*   **Anthropic (Claude):** [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

---

## 🌏 Local AI Tools (Offline & Free)

These tools run on your own machine, offering privacy and offline access.

### 1. Ollama (Recommended)

**The best choice for most users.** A complete, easy-to-use system for running local models.

*   **Installation (macOS):** `brew install ollama`
*   **Installation (Linux/WSL):** `curl -fsSL https://ollama.com/install.sh | sh`
*   **Installation (Windows):** Download from [ollama.com](https://ollama.com) or `winget install Ollama.Ollama`

*   **Usage:**
    ```bash
    # Download a model (do this once)
    ollama pull llama3

    # Start an interactive chat
    ollama run llama3

    # Ask a single question
    ollama run llama3 "Explain quantum computing in one sentence"
    ```

### 2. LM Studio

A desktop app with a graphical interface for downloading models. It also provides a local server that other tools can connect to.

*   **Installation:** Download from [lmstudio.ai](https://lmstudio.ai/)
*   **How it Works:**
    1.  Use the app to download models.
    2.  Go to the "Local Server" tab and click "Start Server".
    3.  You now have an OpenAI-compatible API running at `http://localhost:1234`.

*   **Usage (with another tool like `aichat`):**
    ```bash
    # Tell aichat to use your local LM Studio server
    aichat --model local-model --api-base http://localhost:1234/v1 "Hello!"
    ```

### 3. LocalAI

A powerful, self-hosted option for developers. It's more complex but highly customizable.

*   **Installation (Docker):** `docker run -p 8080:8080 --name local-ai localai/localai:latest`
*   **How it Works:** Starts an OpenAI-compatible API server at `http://localhost:8080`.
*   **Usage (with `curl`):**
    ```bash
    curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{
      "model": "gpt-3.5-turbo",
      "messages": [{"role": "user", "content": "Hello"}]
    }'
    ```

---

## ☁️ Cloud AI Tools (API Key Required)

These tools use powerful models hosted by companies like OpenAI, Google, and GitHub.

### 1. OpenAI (ChatGPT)

While there's no official CLI, the community has built excellent tools.

*   **Recommended Tool: `shell-gpt` (sgpt)**
    *   **Installation:** `pip install shell-gpt`
    *   **Setup:** Run `sgpt --chat test "Hello"` to configure your API key.
    *   **Usage:**
        ```bash
        # Quick question
        sgpt "what is recursion"

        # Generate a shell command
        sgpt --shell "find large files in current directory"

        # Generate code
        sgpt --code "python function to reverse a string"
        ```

*   **Official SDK: `openai` (for Python scripts)**
    *   **Installation:** `pip install openai`
    *   **Usage (in a Python file):**
        ```python
        from openai import OpenAI
        client = OpenAI(api_key="YOUR_API_KEY") # Reads from OPENAI_API_KEY env var by default
        response = client.chat.completions.create(
          model="gpt-4o",
          messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.choices[0].message.content)
        ```

### 2. Google Gemini

Google provides an official SDK with a generous free tier.

*   **Official SDK: `google-generativeai`**
    *   **Installation:** `pip install google-generativeai`
    *   **Usage (in a Python file):**
        ```python
        import google.generativeai as genai
        genai.configure(api_key='YOUR_API_KEY')
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Your prompt")
        print(response.text)
        ```

### 3. GitHub Copilot CLI

An official tool for developers that integrates with `git` and explains commands. Requires a Copilot subscription (free for students/educators).

*   **Installation:**
    1.  Install the GitHub CLI: `brew install gh` (macOS) or `winget install GitHub.cli` (Windows)
    2.  Install the Copilot extension: `gh extension install github/gh-copilot`
*   **Setup:** `gh auth login`
*   **Usage:**
    ```bash
    # Explain a shell command
    gh copilot explain "git rebase -i HEAD~3"

    # Suggest a command
    gh copilot suggest "list all docker containers"
    ```

### 4. Anthropic (Claude)

Similar to OpenAI, Claude is accessed via an API and third-party tools.

*   **Recommended Tool: `aichat`** (See Multi-Provider Tools section)
    *   `aichat` has excellent support for Claude models.
*   **Official SDK: `anthropic`**
    *   **Installation:** `pip install anthropic`

---

## 🚀 Multi-Provider CLI Tools

These powerful tools can connect to multiple AI backends, both local and cloud.

### 1. aichat (Recommended)

A fast, feature-rich CLI written in Rust. It can talk to Ollama, OpenAI, Gemini, Claude, and more.

*   **Installation (macOS/Linux):** `cargo install aichat`
*   **Installation (Windows):** `scoop install aichat`
*   **Setup:** Run `aichat --setup` for an interactive configuration.
*   **Usage:**
    ```bash
    # Default provider (e.g., OpenAI)
    aichat "What is Rust?"

    # Specify a model/provider
    aichat -m gemini "Latest AI news"
    aichat -m ollama:llama3 "Explain this code..."
    aichat -m claude-3-opus "Write a poem about terminals"
    ```

### 2. mods

A simple, elegant tool designed to work with Unix pipes, perfect for summarizing or transforming text.

*   **Installation (macOS):** `brew install charmbracelet/tap/mods`
*   **Installation (Linux):** Download binary from GitHub releases.
*   **Installation (Windows):** `scoop install mods`
*   **Usage:**
    ```bash
    # Use in pipes
    cat file.txt | mods "summarize this"
    git diff | mods "explain these changes"
    ls -la | mods "what are the largest files here?"
    ```

---

## 📊 Comparison Table

| Tool | Official CLI | Third-Party CLI | Local/Offline | Free Tier | API Key Required |
|:-----|:------------|:---------------|:--------------|:----------|:-----------------|
| **Ollama** | ✅ **Yes** | N/A | ✅ **Yes** | ✅ **100% Free** | ❌ **No** |
| **LM Studio** | ⚠️ API Only | ✅ Via API | ✅ **Yes** | ✅ **100% Free** | ❌ **No** |
| **ChatGPT** | ❌ No | ✅ **Many** | ❌ No | Limited ($5 credit) | ✅ Yes |
| **Gemini** | ⚠️ SDK only | ✅ Some | ❌ No | ✅ **Generous** | ✅ Yes |
| **Claude** | ⚠️ SDK only | ✅ Some | ❌ No | Limited ($5 credit) | ✅ Yes |
| **GitHub Copilot**| ✅ **Yes** | N/A | ❌ No | ⚠️ Students only | ✅ Yes |
| **aichat** | ✅ **Yes** | N/A | ✅ (via Ollama) | Depends on backend | ✅ Yes |

---

## 🏆 Best CLI Options by Use Case

### 🥇 Best Overall & For Beginners
**Winner: Ollama**
- Native, simple CLI. Fully local, free, and private. The perfect starting point.

### 💰 Best Free Cloud Option
**Winner: Gemini via SDK**
- The most generous free tier for a powerful cloud model.

### 🔧 Best for Shell Integration
**Winner: `shell-gpt` (sgpt)**
- Perfectly designed for generating and explaining shell commands.

### 👨‍💻 Best for Developers
**Winner: GitHub Copilot CLI**
- Seamless `git` integration and command explanation is invaluable.

### 🔒 Best for Privacy/Offline
**Winner: Ollama** or **LM Studio**
- Your data never leaves your machine.

### 🚀 Best Multi-Provider Tool
**Winner: `aichat`**
- A single, fast interface to access all your models, both local and cloud.

---

## ⚙️ Platform-Specific Installation Tips

### 🐧 **Arch Linux Users**

**Essential Packages:**
```bash
# Core dependencies
sudo pacman -S python python-pip nodejs npm rust cargo docker git github-cli

# AUR helper (if not installed)
sudo pacman -S --needed base-devel git && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```

**Recommended AUR Packages:**
```bash
yay -S ollama              # Local AI - HIGHLY RECOMMENDED
yay -S shell-gpt           # OpenAI CLI wrapper
yay -S aichat              # Multi-provider CLI
yay -S lm-studio-bin       # Local model GUI + API
yay -S mods-bin            # AI in Unix pipes
```

---

### 🪟 **Windows Users**

**Package Managers (Choose One):**
```powershell
# Winget (Built-in to Windows 11)
winget install Ollama.Ollama
winget install GitHub.cli
winget install Python.Python.3.12

# Scoop (Recommended for CLI tools)
# Install Scoop first
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; irm get.scoop.sh | iex
# Then install tools
scoop install ollama gh python nodejs shell-gpt mods aichat
```

**WSL2 (Windows Subsystem for Linux):**
For the best Linux tool compatibility, run `wsl --install` and then use the Linux installation methods inside the WSL2 terminal.

---

### 🍎 **macOS Users**

**Homebrew (Essential):**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install AI CLI tools
brew install ollama gh python node mods

# Install via pip/cargo
pip3 install shell-gpt google-generativeai
cargo install aichat

# GUI Applications via Homebrew Cask
brew install --cask lm-studio
```

---

## Cost Comparison for CLI Usage

| Tool | Free Tier | Cost After Free | Notes |
|:-----|:----------|:---------------|:------|
| **Ollama** | **Unlimited** | $0 | 100% free, uses your local compute |
| **Gemini API** | 60 req/min | Pay-as-you-go | Very generous free tier |
| **OpenAI API** | $5 credit | ~$0.002/1K tokens | Credit expires after 3 months |
| **Claude API** | $5 credit | ~$0.003/1K tokens | Credit expires after 3 months |
| **GitHub Copilot**| Free (students) | $10/month | Included with Copilot subscription |
| **HuggingChat** | Unlimited | $0 | Free inference API for many models |

---

## Conclusion

**Most Powerful Combination:**
1.  **Install `Ollama`** for daily, free, and private tasks.
2.  **Install `aichat`** to seamlessly switch between your local `Ollama` models and powerful cloud models like Gemini or Claude when needed.

```bash
# Use Ollama for local tasks (free, fast)
aichat -m ollama:llama3 "Refactor this Python code"

# Use a cloud model for tasks requiring real-time data
aichat -m gemini "What were the top 5 news stories today?"
```
This combination gives you the best of both worlds: unlimited local AI for privacy and development, and powerful cloud AI for knowledge-intensive tasks.
