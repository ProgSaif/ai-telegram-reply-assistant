# 🤖 AI Telegram Reply Assistant (Gemma + Ollama)

A local AI-powered Telegram bot that automatically generates human-like replies using **Gemma (via Ollama)**.

---

## 🚀 Features

- 📩 Reads Telegram messages in real-time
- 🧠 Uses local AI (Gemma 4 via Ollama)
- 💬 Generates human-like replies
- 🇧🇩 Supports Bangla-English mixed style
- ⚡ Runs fully offline on Mac M1 (no cloud API)

---

## 🏗️ Architecture

Telegram → Telethon → Python Bot → Ollama (Gemma) → Reply → Telegram

---

## 📦 Installation

### 1. Clone repo

```bash
git clone https://github.com/ProgSaif/ai-telegram-reply-assistant.git
cd ai-telegram-reply-assistant


### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download:

https://ollama.com

Run model:

```bash
ollama run gemma4:latest
```

---

## 🔑 Telegram Setup

Create API credentials:

https://my.telegram.org

Get:

- API_ID
- API_HASH

Add them in `config.py`

---

## ⚙️ Configuration

Edit `config.py`:

```python
API_ID = your_api_id
API_HASH = "your_api_hash"
WATCH_CHAT_ID = girlfriend_chat_id
```

---

## ▶️ Run Bot

```bash
python main.py
```

---

## 🧠 How It Works

1. Telegram message received
2. Message sent to Gemma
3. AI generates reply
4. Reply sent automatically

---

## ⚠️ Important Notes

- This bot uses **local AI only (no internet API required)**
- Works best with good persona + examples
- Do not use for spam or harmful automation
- Always test before real use

---

## 📈 Improvements (Future Ideas)

- Add reply delay simulation
- Add emotion detection (happy/sad/angry)
- Add memory database (SQLite)
- Add manual approval mode
- Add multi-chat support

---

## 👨‍💻 Tech Stack

- Python
- Telethon
- Ollama
- Gemma 4
- Mac M1 optimized





