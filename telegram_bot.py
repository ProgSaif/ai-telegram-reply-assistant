#Handles Telegram connection.

from telethon import TelegramClient, events
import asyncio
from config import API_ID, API_HASH, WATCH_CHAT_ID, SESSION_NAME
from ai_engine import generate_reply

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):

    print("\n📩 New Message:", event.raw_text)

    if event.chat_id != WATCH_CHAT_ID:
        return

    print("🧠 Sending to AI...")

    reply = generate_reply(event.raw_text)

    print("📤 Reply:", reply)

    await asyncio.sleep(2)

    await event.reply(reply)

def start_bot():
    print("🚀 Starting Telegram Bot...")
    client.start()

    me = client.loop.run_until_complete(client.get_me())
    print(f"Logged in as: {me.first_name}")

    client.run_until_disconnected()
