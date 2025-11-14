# AI Tools with Command Line Interface Support

**Research Date:** November 14, 2025  
**Audience:** All users - from complete beginners to advanced CLI users

## 📚 Table of Contents
- [Beginner's Guide - Start Here!](#beginners-guide---start-here)
- [Overview](#overview)
- [AI Tools with Official CLI Support](#ai-tools-with-official-cli-support)
- [Installation Quick Start](#installation-quick-start)
- [Platform-Specific Installation Tips](#platform-specific-installation-tips)

---

## 🎓 Beginner's Guide - Start Here!

**New to command line tools? No problem! This section is for you.**

### What is a CLI (Command Line Interface)?

A CLI is a text-based way to interact with software by typing commands instead of clicking buttons. It might look intimidating, but it's actually very powerful once you learn the basics.

**Why use AI CLI tools?**
- ⚡ Faster than opening a browser
- 🔧 Can integrate with scripts and workflows
- 🎯 More focused, no distractions
- 💻 Works on any computer, even without a GUI
- 🔒 Some tools work completely offline

---

### Prerequisites Check - Do You Have These?

Before installing AI CLI tools, you'll need some basic software. Don't worry, we'll show you how to install everything!

#### ✅ Check What You Already Have

**On Windows (PowerShell):**
```powershell
# Open PowerShell (search "PowerShell" in Start menu)
# Type these commands one at a time:

python --version      # Should show Python 3.x
pip --version        # Should show pip version
node --version       # Should show Node.js version
git --version        # Should show git version
```

**On macOS/Linux (Terminal):**
```bash
# Open Terminal (search "Terminal" in Spotlight on Mac)
# Type these commands one at a time:

python3 --version    # Should show Python 3.x
pip3 --version       # Should show pip version
node --version       # Should show Node.js version
git --version        # Should show git version
```

**What do the results mean?**
- ✅ If you see version numbers (like "Python 3.12.0"), you're good!
- ❌ If you see "command not found" or "not recognized", you need to install that tool

---

### Step-by-Step: Installing Prerequisites

Choose your operating system and follow the steps:

#### 🪟 **Windows - Complete Setup Guide**

**Step 1: Install Python**
```powershell
# Option A: Using Microsoft Store (Easiest!)
# 1. Open Microsoft Store
# 2. Search for "Python 3.12"
# 3. Click "Get" or "Install"
# 4. Wait for installation to complete

# Option B: Using Winget (Command line)
winget install Python.Python.3.12

# Verify installation
python --version
```

**Step 2: Install Node.js (for some CLI tools)**
```powershell
# Download from https://nodejs.org
# Or use Winget
winget install OpenJS.NodeJS

# Verify
node --version
npm --version
```

**Step 3: Install Git (optional, but recommended)**
```powershell
winget install Git.Git

# Verify
git --version
```

**Step 4: Install a Package Manager (Recommended)**
```powershell
# Scoop - Great for CLI tools
# Run this in PowerShell:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Now you can easily install tools like:
scoop install ollama
```

---

#### 🍎 **macOS - Complete Setup Guide**

**Step 1: Install Homebrew (Package Manager - Essential!)**
```bash
# Open Terminal (press Cmd+Space, type "Terminal")
# Copy and paste this entire command:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Follow the prompts and enter your password when asked
# Wait for installation (5-10 minutes)

# Verify Homebrew is installed
brew --version
```

**Step 2: Install Python, Node.js, and Git**
```bash
# Install all at once with Homebrew
brew install python node git

# Verify installations
python3 --version
node --version
git --version
```

**You're done! macOS users are now ready to install AI CLI tools.**

---

#### 🐧 **Linux - Complete Setup Guide**

**For Ubuntu/Debian:**
```bash
# Update package list first
sudo apt update

# Install Python, pip, Node.js, npm, and git
sudo apt install python3 python3-pip nodejs npm git curl

# Verify installations
python3 --version
pip3 --version
node --version
npm --version
git --version
```

**For Arch Linux:**
```bash
# Install essential packages
sudo pacman -S python python-pip nodejs npm git curl base-devel

# Install yay (AUR helper) for easier package installation
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

# Verify installations
python --version
pip --version
node --version
yay --version
```

**For Fedora:**
```bash
sudo dnf install python3 python3-pip nodejs npm git curl

# Verify
python3 --version
node --version
```

---

### 🚀 Your First AI CLI Tool - Easiest Option!

Now that prerequisites are installed, let's install your first AI tool. We'll use **Ollama** because:
- ✅ Works 100% locally (no internet needed after setup)
- ✅ Completely free
- ✅ No API keys or accounts required
- ✅ Easy to install
- ✅ Works on all platforms

#### Installing Ollama - Step by Step

**Windows:**
```powershell
# Method 1: Download installer (Easiest!)
# 1. Go to https://ollama.com/download/windows
# 2. Download OllamaSetup.exe
# 3. Double-click to install
# 4. Follow the installer prompts

# Method 2: Using Winget
winget install Ollama.Ollama

# Verify it's installed
ollama --version
```

**macOS:**
```bash
# Method 1: Using Homebrew (Recommended)
brew install ollama

# Method 2: Download from website
# Go to https://ollama.com and click Download

# Verify
ollama --version
```

**Linux (All distributions):**
```bash
# One-line installer
curl -fsSL https://ollama.com/install.sh | sh

# Verify
ollama --version
```

**Arch Linux (Alternative):**
```bash
# Using AUR
yay -S ollama

# Enable and start the service
sudo systemctl enable --now ollama

# Verify
ollama --version
```

---

### 🎯 Using Ollama - Your First AI Conversation

**Step 1: Download an AI Model**
```bash
# Download Llama 3 (recommended, ~4.7GB)
ollama pull llama3

# This will take 5-15 minutes depending on your internet speed
# You only need to do this once!
```

**Other models you can try:**
```bash
ollama pull mistral        # Smaller, faster (~4.1GB)
ollama pull codellama      # Good for coding (~3.8GB)
ollama pull llama3.2       # Latest version (~2GB)
```

**Step 2: Start Chatting!**
```bash
# Start interactive chat
ollama run llama3

# You'll see a prompt like: >>> 
# Type your question and press Enter
```

**Example conversation:**
```
>>> Hello! Can you help me learn about AI?
AI will respond here...

>>> What are some good programming languages for beginners?
AI will respond here...

>>> exit
# Type 'exit' or '/bye' to quit
```

**Step 3: One-Shot Questions (No Chat Mode)**
```bash
# Ask a single question
ollama run llama3 "What is the capital of France?"

# Use in scripts
ollama run llama3 "Explain quantum computing in simple terms"

# Get help with commands
ollama run llama3 "How do I list files in a directory on Linux?"
```

---

### 🆘 Common Beginner Issues & Solutions

#### Problem: "Command not found" or "Not recognized"

**Solution:**
```bash
# On Windows - Make sure you opened a NEW terminal after installation
# Close PowerShell and open it again

# On macOS/Linux - Check if the tool is in your PATH
echo $PATH

# If Python/pip shows "not found", you may need to use python3/pip3
python3 --version
pip3 --version
```

---

#### Problem: "Permission denied" on Linux/macOS

**Solution:**
```bash
# You need administrator privileges
# Add 'sudo' before the command:
sudo apt install python3

# You'll be asked for your password
```

---

#### Problem: Ollama is slow or not responding

**Solution:**
```bash
# Check if Ollama service is running

# Windows: Check Task Manager for "ollama" process

# macOS/Linux:
ps aux | grep ollama

# Restart Ollama
# Windows: Restart the Ollama application
# Linux/macOS:
sudo systemctl restart ollama  # Arch/systemd
# OR
pkill ollama && ollama serve
```

---

#### Problem: Model download is taking forever

**Solution:**
- Models are large (2-8GB) - this is normal!
- Use a smaller model if needed: `ollama pull llama3.2` (2GB)
- Download during off-peak hours
- Check your internet connection

---

#### Problem: "Not enough disk space"

**Solution:**
```bash
# Check available space
# Windows:
Get-PSDrive C

# macOS/Linux:
df -h

# Each model needs 2-8GB
# Delete unused models to free space:
ollama rm mistral
ollama list  # See what's installed
```

---

### 📖 Basic Terminal Commands You Should Know

Before using CLI tools, learn these essential commands:

**Navigation:**
```bash
# Windows (PowerShell)
pwd                 # Print Working Directory - where am I?
cd C:\Users         # Change directory
cd ..               # Go up one level
dir                 # List files (Windows)
cls                 # Clear screen

# macOS/Linux (Bash/Zsh)
pwd                 # Print Working Directory
cd /home/user       # Change directory
cd ..               # Go up one level
ls                  # List files
ls -la              # List with details
clear               # Clear screen
```

**File Operations:**
```bash
# Create a file
# Windows:
New-Item test.txt

# macOS/Linux:
touch test.txt

# View file contents
# Windows:
type file.txt

# macOS/Linux:
cat file.txt

# Edit a file
# Windows:
notepad file.txt

# macOS/Linux:
nano file.txt       # Simple editor
```

**Getting Help:**
```bash
# Most commands have built-in help
ollama --help
python --help
pip --help

# Or use 'man' on Linux/macOS
man ls
```

---

### 🎓 Learning Path for Beginners

**Week 1: Get Comfortable**
1. ✅ Install prerequisites (Python, Node.js)
2. ✅ Install Ollama
3. ✅ Download one model (`ollama pull llama3`)
4. ✅ Have 10 conversations with the AI
5. ✅ Practice basic terminal commands

**Week 2: Explore More**
1. Try different Ollama models
2. Install one more CLI tool (try `shell-gpt`)
3. Learn about API keys (for cloud tools)
4. Try using AI to help with code or writing

**Week 3: Advanced Usage**
1. Create simple scripts that use AI
2. Try integrating AI into your workflow
3. Explore GitHub Copilot CLI (if eligible)
4. Join online communities (Reddit, Discord)

---

### 📚 Helpful Resources for Beginners

**Terminal Basics:**
- [Learn the Command Line (Codecademy)](https://www.codecademy.com/learn/learn-the-command-line) - Free
- [Command Line Crash Course](https://www.youtube.com/watch?v=yz7nYlnXLfE) - YouTube

**Python Basics (if you want to use Python CLI tools):**
- [Python for Beginners (Python.org)](https://www.python.org/about/gettingstarted/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/) - Free book

**Ollama Documentation:**
- [Official Ollama Docs](https://github.com/ollama/ollama/blob/main/README.md)
- [Ollama Model Library](https://ollama.com/library)

**Community Help:**
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) - Reddit community for local AI
- [r/ollama](https://reddit.com/r/ollama) - Ollama-specific help
- [Ollama Discord](https://discord.gg/ollama) - Real-time chat support

---

### ✅ Beginner's Checklist

Before moving on to the advanced sections, make sure you can:

- [ ] Open a terminal/command prompt
- [ ] Navigate directories (cd, ls/dir, pwd)
- [ ] Check if software is installed (--version commands)
- [ ] Install software using a package manager
- [ ] Run Ollama and have a conversation
- [ ] Use basic terminal commands
- [ ] Ask for help (--help flag)

**Once you've checked all these boxes, you're ready to explore the full guide below!**

---

## Overview
This document identifies which popular AI tools offer command-line utilities for terminal-based interaction.

---

## AI Tools with Official CLI Support

### 1. **OpenAI (ChatGPT) - Via API CLI Tools**

**Official CLI:** None (API-based interaction only)

**Third-Party CLI Tools:**

#### A. **`shell_gpt`** (sgpt) - Recommended ⭐

**Installation:**

**Linux / macOS:**
```bash
pip install shell-gpt
```

**Arch Linux:**
```bash
# Via pacman (AUR)
yay -S shell-gpt

# Or via pip
sudo pacman -S python-pip
pip install shell-gpt
```

**Windows:**
```powershell
# Install Python first from python.org or Microsoft Store
pip install shell-gpt

# Or via Scoop
scoop install shell-gpt
```

**Usage:**
```bash
sgpt "what is recursion"
sgpt --shell "find large files in current directory"
sgpt --code "python function to reverse a string"
```

#### B. **`chatgpt-cli`** (Node.js wrapper)

**Installation:**

**Linux / macOS:**
```bash
npm install -g chatgpt-cli
```

**Arch Linux:**
```bash
sudo pacman -S nodejs npm
npm install -g chatgpt-cli
```

**Windows:**
```powershell
# Install Node.js from nodejs.org first
npm install -g chatgpt-cli
```

**Usage:** `chatgpt "your prompt here"`

#### C. **`openai-cli`** (Python official SDK)

**Installation:**

**All Platforms:**
```bash
pip install openai
```

**Arch Linux:**
```bash
sudo pacman -S python-pip
pip install openai
```

**Windows:**
```powershell
pip install openai
```

**Usage:** Via Python scripts with API key

#### D. **`gpt-cli`** (Go-based)

**Installation:**

**Linux / macOS:**
```bash
go install github.com/manno/gpt-cli@latest
```

**Arch Linux:**
```bash
sudo pacman -S go
go install github.com/manno/gpt-cli@latest
# Add ~/go/bin to PATH if not already
```

**Windows:**
```powershell
# Install Go from go.dev first
go install github.com/manno/gpt-cli@latest
# Add %USERPROFILE%\go\bin to PATH
```

**API Access Required:** Yes (paid - $5+ per month typical usage)
**Free Tier:** $5 initial credit (expires after 3 months)

---

### 2. **Anthropic Claude - Official CLI**

**Official CLI:** `claude-cli` (limited availability)

**Third-Party CLI Tools:**

#### A. **`claude-cli`** (Node.js wrapper)

**Installation:**

**Linux / macOS:**
```bash
npm install -g claude-cli
```

**Arch Linux:**
```bash
sudo pacman -S nodejs npm
npm install -g claude-cli
```

**Windows:**
```powershell
# Install Node.js from nodejs.org
npm install -g claude-cli
```

**Usage:** Requires Anthropic API key

#### B. **`claudecli`** (Python)

**Installation:**

**Linux / macOS:**
```bash
pip install claudecli
```

**Arch Linux:**
```bash
sudo pacman -S python-pip
pip install claudecli
```

**Windows:**
```powershell
pip install claudecli
```

**Usage:** `claude "your prompt"`

**API Access Required:** Yes (paid - $5 initial credit)
**Free Tier:** $5 credit (expires after 3 months)

---

### 3. **Google Gemini - Official CLI via SDK**

**Official CLI:** Via `google-generativeai` Python SDK

**Installation:**

**Linux / macOS:**
```bash
pip install google-generativeai
```

**Arch Linux:**
```bash
sudo pacman -S python-pip
pip install google-generativeai
```

**Windows:**
```powershell
# Install Python from python.org or Microsoft Store
pip install google-generativeai
```

**Usage (Python script):**
```python
import google.generativeai as genai
genai.configure(api_key='YOUR_API_KEY')
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Your prompt")
print(response.text)
```

**Third-Party CLI Tools:**
- **`gemini-cli`** (community wrapper)
  - Various implementations on GitHub
  
**API Access Required:** Yes (free tier available)
**Free Tier:** Generous - 60 requests per minute

---

### 4. **Microsoft Copilot - No Direct CLI**

**Official CLI:** None
**Terminal Access:** Not available
**Notes:** Designed for web/app interface only

---

### 5. **Perplexity AI - API Only**

**Official CLI:** None
**API Access:** Beta API available (paid)
**CLI Support:** Community tools only

---

### 6. **HuggingChat - Via Hugging Face CLI**

**Official CLI:** `huggingface-cli`

**Installation:**

**Linux / macOS:**
```bash
pip install -U huggingface_hub
huggingface-cli login
```

**Arch Linux:**
```bash
sudo pacman -S python-pip
pip install -U huggingface_hub
huggingface-cli login
```

**Windows:**
```powershell
pip install -U huggingface_hub
huggingface-cli login
```

**Python Inference:**
```python
from huggingface_hub import InferenceClient
client = InferenceClient()
response = client.text_generation("Prompt", model="HuggingFaceH4/zephyr-7b-beta")
```

**API Access Required:** Free with Hugging Face account
**Free Tier:** Generous inference API limits

---

### 7. **Ollama - Full Local CLI (Recommended for CLI Users)**

**Official CLI:** ✅ YES - Full local CLI support

**Installation:**

**Linux (General):**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Arch Linux:**
```bash
# Via AUR
yay -S ollama

# Or via pacman (if in official repos)
sudo pacman -S ollama

# Start the service
sudo systemctl enable --now ollama
```

**macOS:**
```bash
# Via Homebrew
brew install ollama

# Or download from ollama.com
```

**Windows:**
```powershell
# Download installer from https://ollama.com/download/windows
# Or via Winget
winget install Ollama.Ollama

# Or via Scoop
scoop bucket add main
scoop install ollama
```

**Docker (All Platforms):**
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull llama3
docker exec -it ollama ollama run llama3
```

**Usage:**
```bash
# Install models
ollama pull llama3
ollama pull codellama
ollama pull mistral

# Interactive chat
ollama run llama3

# One-shot queries
ollama run llama3 "Explain quantum computing"

# List installed models
ollama list

# API mode (automatic on start)
ollama serve  # Usually runs automatically as service
```

**Features:**
- ✅ Fully offline/local
- ✅ No API keys required
- ✅ Free unlimited usage
- ✅ Multiple model support (Llama 3, Mistral, CodeLlama, etc.)
- ✅ Shell integration possible
- ✅ Docker support
- ✅ GPU acceleration (NVIDIA, AMD, Apple Silicon)

**Requirements:** 
- 8GB+ RAM recommended (4GB minimum)
- 4-8GB disk space per model
- CPU/GPU (GPU optional but significantly faster)

**System Service:**
```bash
# Linux/macOS - Check if running
ollama --version

# Arch Linux - Manage service
sudo systemctl status ollama
sudo systemctl start ollama
sudo systemctl stop ollama

# Windows - Runs as background service automatically
```

**Free Tier:** 100% free, runs locally

---

### 8. **GitHub Copilot CLI - Official**

**Official CLI:** ✅ YES - `github-copilot-cli`

**Installation:**

**Prerequisites:**
- GitHub account
- GitHub CLI (`gh`) installed
- GitHub Copilot subscription OR free for students/OSS maintainers

**Linux / macOS:**
```bash
# Install GitHub CLI first
# macOS
brew install gh

# Arch Linux
sudo pacman -S github-cli

# Debian/Ubuntu
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Then install Copilot CLI extension
gh extension install github/gh-copilot
```

**Windows:**
```powershell
# Via Winget
winget install GitHub.cli

# Or via Scoop
scoop install gh

# Or download from https://cli.github.com

# Then install Copilot extension
gh extension install github/gh-copilot
```

**Setup:**
```bash
# Authenticate with GitHub
gh auth login

# Verify Copilot access
gh copilot --version
```

**Usage:**
```bash
# Explain shell commands
gh copilot explain "git rebase -i HEAD~3"

# Suggest commands
gh copilot suggest "find large files"

# Interactive mode
gh copilot
```

**Requirements:**
- GitHub account
- GitHub Copilot subscription OR free for students/OSS maintainers

**Free Tier:** Free for verified students and open-source maintainers

---

### 9. **LM Studio - GUI + CLI API**

**Official Tool:** ✅ Desktop app with local API

**Installation:**

**Windows:**
```powershell
# Download from https://lmstudio.ai/
# Run the installer (.exe)
# Or via Winget (if available)
winget install LMStudio.LMStudio
```

**macOS:**
```bash
# Download from https://lmstudio.ai/
# Drag to Applications folder
# Or via Homebrew Cask
brew install --cask lm-studio
```

**Linux / Arch Linux:**
```bash
# Download AppImage from https://lmstudio.ai/
wget https://releases.lmstudio.ai/linux/latest/LM-Studio-x86_64.AppImage
chmod +x LM-Studio-x86_64.AppImage
./LM-Studio-x86_64.AppImage

# Or on Arch via AUR
yay -S lm-studio-bin
```

**Features:**
- Download and run local LLMs (GUI for model management)
- OpenAI-compatible API server
- CLI access via curl/scripts once server is running
- No internet required after model download
- Supports GGUF model format

**CLI Usage (After starting LM Studio server):**
```bash
# Default server runs on http://localhost:1234
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Hello"}],
    "temperature": 0.7,
    "max_tokens": 100
  }'

# Or use with OpenAI Python client
pip install openai
python -c "
from openai import OpenAI
client = OpenAI(base_url='http://localhost:1234/v1', api_key='not-needed')
response = client.chat.completions.create(
  model='local-model',
  messages=[{'role': 'user', 'content': 'Hello'}]
)
print(response.choices[0].message.content)
"
```

**Free Tier:** 100% free

---

### 10. **LocalAI - Self-Hosted CLI**

**Official CLI:** ✅ YES - Docker-based

**Installation:**

**All Platforms (via Docker):**
```bash
# Pull and run LocalAI
docker run -p 8080:8080 --name local-ai -ti localai/localai:latest

# With GPU support (NVIDIA)
docker run -p 8080:8080 --gpus all --name local-ai localai/localai:latest-gpu-nvidia-cuda-12

# Persistent storage
docker run -p 8080:8080 \
  -v $HOME/.local-ai/models:/models \
  --name local-ai \
  localai/localai:latest
```

**Linux / Arch Linux (Binary Installation):**
```bash
# Download binary
wget https://github.com/go-skynet/LocalAI/releases/latest/download/local-ai-Linux-x86_64
chmod +x local-ai-Linux-x86_64
./local-ai-Linux-x86_64

# Or via AUR (Arch Linux)
yay -S localai-bin
systemctl --user enable --now localai
```

**Windows:**
```powershell
# Install Docker Desktop first from docker.com
# Then run in PowerShell
docker run -p 8080:8080 --name local-ai localai/localai:latest

# Or download Windows binary from GitHub releases
# https://github.com/go-skynet/LocalAI/releases
```

**macOS:**
```bash
# Via Docker
docker run -p 8080:8080 --name local-ai localai/localai:latest

# Or download binary from releases
wget https://github.com/go-skynet/LocalAI/releases/latest/download/local-ai-Darwin-arm64
chmod +x local-ai-Darwin-arm64
./local-ai-Darwin-arm64
```

**Usage:**
```bash
# OpenAI-compatible API
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}]
  }'

# List available models
curl http://localhost:8080/v1/models

# Generate text
curl http://localhost:8080/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "prompt": "Write a haiku about coding",
    "max_tokens": 50
  }'
```

**Free Tier:** 100% free, self-hosted

---

## Popular CLI Wrapper Projects

### Shell-GPT (sgpt) ⭐
**Best for:** Shell command generation and quick queries

**Installation:**

**Linux / macOS:**
```bash
pip install shell-gpt
```

**Arch Linux:**
```bash
yay -S shell-gpt
# Or via pip
sudo pacman -S python-pip
pip install shell-gpt
```

**Windows:**
```powershell
pip install shell-gpt
# Or via Scoop
scoop install shell-gpt
```

**Usage:**
```bash
sgpt "list all docker containers"
sgpt --shell "find large files in home directory"
sgpt --code "python function to calculate fibonacci"
```

---

### aichat
**Best for:** Multi-provider CLI (Rust-based, fast)

**Installation:**

**Linux / macOS:**
```bash
cargo install aichat
```

**Arch Linux:**
```bash
# Via AUR
yay -S aichat

# Or via cargo
sudo pacman -S rust
cargo install aichat
```

**Windows:**
```powershell
# Install Rust first from rustup.rs
# Then install aichat
cargo install aichat

# Or via Scoop
scoop install aichat
```

**Usage:**
```bash
# Supports: OpenAI, Claude, Gemini, LocalAI, Ollama
aichat "What is Rust?"
aichat -m claude "Explain async programming"
aichat -m gemini "Latest AI news"
```

---

### mods
**Best for:** AI in Unix pipes

**Installation:**

**macOS:**
```bash
brew install charmbracelet/tap/mods
```

**Linux / Arch Linux:**
```bash
# Download binary from releases
wget https://github.com/charmbracelet/mods/releases/latest/download/mods_Linux_x86_64.tar.gz
tar -xzf mods_Linux_x86_64.tar.gz
sudo mv mods /usr/local/bin/

# Arch Linux via AUR
yay -S mods-bin
```

**Windows:**
```powershell
# Via Scoop
scoop install mods
```

**Usage:**
```bash
# Use in pipes
cat file.txt | mods "summarize this"
git diff | mods "explain these changes"
ls -la | mods "what are the largest files here?"
```

---

### ChatGPT CLI (Node.js)
**Best for:** Conversational interaction

**Installation:**

**All Platforms:**
```bash
npm install -g chatgpt-cli
```

**Arch Linux:**
```bash
sudo pacman -S nodejs npm
npm install -g chatgpt-cli
```

**Windows:**
```powershell
# Install Node.js from nodejs.org first
npm install -g chatgpt-cli
```

**Usage:**
```bash
chatgpt
# Interactive mode
```

---

## Comparison Table: CLI Support

| Tool | Official CLI | Third-Party CLI | Local/Offline | Free Tier | API Key Required |
|:-----|:------------|:---------------|:--------------|:----------|:-----------------|
| **ChatGPT** | ❌ | ✅ Many | ❌ | Limited ($5 credit) | ✅ Yes |
| **Claude** | ❌ | ✅ Several | ❌ | Limited ($5 credit) | ✅ Yes |
| **Gemini** | ⚠️ SDK only | ✅ Some | ❌ | ✅ Generous | ✅ Yes |
| **Copilot** | ❌ | ❌ | ❌ | ❌ No | N/A |
| **Perplexity** | ❌ | ⚠️ Limited | ❌ | ❌ No | ✅ Yes |
| **HuggingChat** | ⚠️ SDK | ✅ Some | ❌ | ✅ Yes | ⚠️ Optional |
| **Ollama** | ✅ Full | N/A | ✅ Yes | ✅ 100% Free | ❌ No |
| **GitHub Copilot CLI** | ✅ Official | N/A | ❌ | ⚠️ Students only | ✅ Yes |
| **LM Studio** | ⚠️ API | Via API | ✅ Yes | ✅ 100% Free | ❌ No |
| **LocalAI** | ✅ Docker | N/A | ✅ Yes | ✅ 100% Free | ❌ No |

---

## Best CLI Options by Use Case

### 🏆 Best Overall CLI Experience
**Winner: Ollama**
- Native CLI interface
- Fully local and free
- Easy model management
- No API keys needed
- Fast and reliable

### 💰 Best Free Cloud CLI
**Winner: Gemini via SDK**
- Generous free tier
- Official Google support
- Good API limits
- Easy Python integration

### 🔧 Best for Shell Integration
**Winner: shell-gpt (sgpt)**
- Designed for shell workflows
- Command generation
- Pipe-friendly
- Works with OpenAI API

### 👨‍💻 Best for Developers
**Winner: GitHub Copilot CLI**
- Command explanations
- Git integration
- GitHub ecosystem
- Free for students

### 🔒 Best for Privacy/Offline
**Winner: Ollama or LM Studio**
- 100% local
- No internet after setup
- No data collection
- Full control

### 🚀 Best Multi-Provider CLI
**Winner: aichat**
- Supports multiple providers
- Fast (Rust-based)
- Single tool for many APIs
- Great UX

---

## Installation Quick Start

### Option 1: Ollama (Recommended for Beginners) ⭐

**Linux:**
```bash
# General Linux
curl -fsSL https://ollama.com/install.sh | sh

# Arch Linux
yay -S ollama
sudo systemctl enable --now ollama

# Get a model
ollama pull llama3

# Start chatting
ollama run llama3
```

**Windows:**
```powershell
# Download installer from https://ollama.com/download/windows
# Or via Winget
winget install Ollama.Ollama

# Then in terminal
ollama pull llama3
ollama run llama3
```

**macOS:**
```bash
# Via Homebrew
brew install ollama

# Or download from ollama.com

ollama pull llama3
ollama run llama3
```

---

### Option 2: Shell-GPT (For OpenAI/Cloud Users)

**Linux / macOS:**
```bash
# Install
pip install shell-gpt

# Configure (will prompt for API key)
sgpt --chat test "Hello"

# Use
sgpt "Explain Docker"
sgpt --shell "list all processes using more than 100MB RAM"
```

**Arch Linux:**
```bash
# Via AUR
yay -S shell-gpt

# Or via pip
sudo pacman -S python-pip
pip install shell-gpt

sgpt "Explain Docker"
```

**Windows:**
```powershell
# Install Python from python.org first
pip install shell-gpt

# Configure
sgpt --chat test "Hello"

# Use
sgpt "Explain Docker"
```

---

### Option 3: Gemini (Free Cloud API)

**All Platforms:**
```bash
# Install SDK
pip install google-generativeai

# Get API key from https://makersuite.google.com/app/apikey

# Create helper script
cat > gemini.py << 'SCRIPT'
import google.generativeai as genai
import sys
genai.configure(api_key='YOUR_API_KEY_HERE')
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(sys.argv[1])
print(response.text)
SCRIPT

# Make executable (Linux/macOS)
chmod +x gemini.py

# Usage
python gemini.py "Your question"
```

**Windows PowerShell Script:**
```powershell
# Create gemini.ps1
@"
import google.generativeai as genai
import sys
genai.configure(api_key='YOUR_API_KEY_HERE')
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(' '.join(sys.argv[1:]))
print(response.text)
"@ | Out-File -FilePath gemini.py -Encoding UTF8

# Usage
python gemini.py "Your question"
```

---

### Option 4: aichat (Multi-Provider, Fast)

**Linux / macOS:**
```bash
# Install Rust if not already installed
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install aichat
cargo install aichat

# Configure (interactive setup)
aichat --setup

# Use
aichat "What is Rust?"
```

**Arch Linux:**
```bash
# Via AUR (pre-compiled)
yay -S aichat

# Configure
aichat --setup

# Use with different providers
aichat -m openai "Question for OpenAI"
aichat -m claude "Question for Claude"
aichat -m ollama:llama3 "Question for local Ollama"
```

**Windows:**
```powershell
# Install Rust from https://rustup.rs
# Follow the installer instructions

# Then in terminal
cargo install aichat

# Configure
aichat --setup

# Use
aichat "What is Rust?"
```

---

## Recommendations

### For Command Line Power Users:
1. **Primary:** Ollama (local, free, unlimited)
2. **Backup:** Gemini API (cloud, free tier)
3. **Shell Integration:** shell-gpt or mods

### For Students/Developers:
1. **Primary:** GitHub Copilot CLI (if eligible)
2. **Secondary:** Ollama (free, local)
3. **Learning:** HuggingChat API (free, no limits)

### For Privacy-Conscious Users:
1. **Primary:** Ollama (fully local)
2. **Alternative:** LM Studio (GUI + local API)
3. **Advanced:** LocalAI (self-hosted)

### For API Developers:
1. **Testing:** Ollama (OpenAI-compatible)
2. **Production:** OpenAI or Claude API
3. **Budget:** Gemini (generous free tier)

---

## Platform-Specific Installation Tips

### 🐧 **Arch Linux Users**

**Essential Packages:**
```bash
# Core dependencies
sudo pacman -S python python-pip nodejs npm rust cargo docker git github-cli

# AUR helper (if not installed)
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay && makepkg -si
```

**Recommended AUR Packages:**
```bash
yay -S ollama              # Local AI - HIGHLY RECOMMENDED
yay -S shell-gpt           # OpenAI CLI wrapper
yay -S aichat              # Multi-provider CLI
yay -S lm-studio-bin       # Local model GUI + API
yay -S mods-bin            # AI in Unix pipes
```

**System Services:**
```bash
# Enable Ollama service
sudo systemctl enable --now ollama

# Check status
systemctl status ollama
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
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Then install tools
scoop install ollama
scoop install gh
scoop install python
scoop install nodejs
scoop install shell-gpt
scoop install mods
```

**WSL2 (Windows Subsystem for Linux):**
```powershell
# Install WSL2 for best Linux tool compatibility
wsl --install

# Then use Linux installation methods inside WSL2
wsl
curl -fsSL https://ollama.com/install.sh | sh
pip install shell-gpt
```

**Docker Desktop:**
```powershell
# Required for LocalAI
winget install Docker.DockerDesktop
# Restart required after installation
```

**Tips:**
- Use Windows Terminal for better CLI experience
- Add Python and Node.js to PATH during installation
- Consider using WSL2 for tools with limited Windows support

---

### 🍎 **macOS Users**

**Homebrew (Essential):**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install AI CLI tools
brew install ollama              # Local AI
brew install gh                  # GitHub CLI (for Copilot)
brew install python              # Python
brew install node                # Node.js
brew install charmbracelet/tap/mods  # AI in pipes

# Install via pip
pip3 install shell-gpt
pip3 install google-generativeai
```

**GUI Applications:**
```bash
# Via Homebrew Cask
brew install --cask lm-studio    # Local model GUI
```

**Apple Silicon (M1/M2/M3) Tips:**
- Ollama has excellent Apple Silicon support
- Metal acceleration works out of the box
- Models run significantly faster on Apple Silicon
- Recommended for best local AI performance

---

### 🐧 **General Linux Distribution Commands**

**Debian/Ubuntu:**
```bash
# Update package list
sudo apt update

# Install dependencies
sudo apt install python3 python3-pip nodejs npm curl git

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Install via pip
pip3 install shell-gpt google-generativeai
```

**Fedora/RHEL:**
```bash
# Install dependencies
sudo dnf install python3 python3-pip nodejs npm curl git

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Install via pip
pip3 install shell-gpt google-generativeai
```

**openSUSE:**
```bash
# Install dependencies
sudo zypper install python3 python3-pip nodejs npm curl git

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Install via pip
pip3 install shell-gpt google-generativeai
```

---

## Cost Comparison for CLI Usage

| Tool | Free Tier | Cost After Free | Notes |
|:-----|:----------|:---------------|:------|
| **Ollama** | Unlimited | $0 | 100% free, local compute |
| **Gemini API** | 60 req/min | Pay-as-go | Very generous free tier |
| **OpenAI API** | $5 credit | ~$0.002/1K tokens | Credit expires in 3 months |
| **Claude API** | $5 credit | ~$0.003/1K tokens | Credit expires in 3 months |
| **GitHub Copilot CLI** | Free (students) | $10/month | Included with Copilot |
| **HuggingChat** | Unlimited | $0 | Free inference API |

---

## Conclusion

**Best CLI-First AI Tool: Ollama**
- Native command-line interface
- No API keys or accounts required
- Completely free and unlimited
- Works offline
- Multiple model support

**Best Cloud CLI Option: Gemini API**
- Generous free tier
- Official support
- Easy integration
- Good performance

**Most Powerful Combination:**
```bash
# Install both
curl -fsSL https://ollama.com/install.sh | sh  # Local
pip install google-generativeai                # Cloud backup

# Use Ollama for daily tasks (free, fast)
ollama run llama3 "your prompt"

# Use Gemini for tasks requiring latest data
python gemini_script.py "current events query"
```

This gives you unlimited local AI + cloud backup for research/current info.

---

**Next Steps:**
1. Choose your primary CLI tool based on use case
2. Install and configure
3. Add shell aliases for convenience
4. Consider combining local + cloud for best experience

