from telegram import Update
from telegram.ext import ContextTypes
import json
import os

DATA_FILE = "budget_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Добро пожаловать в Финансовый Планировщик!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/config <категория> <бюджет>\n/log <категория> <+/-сумма>\n/summary\n/notifyon\n/notifyoff"
    )

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        category = context.args[0]
        amount = float(context.args[1])
        user_id = str(update.message.from_user.id)
        data = load_data()
        data.setdefault(user_id, {"budget": {}, "log": []})
        data[user_id]["budget"][category] = amount
        save_data(data)
        await update.message.reply_text(f"✅ Бюджет для '{category}' установлен: {amount}")
    except:
        await update.message.reply_text("❌ Используй: /config <категория> <сумма>")

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        category = context.args[0]
        amount = float(context.args[1])
        user_id = str(update.message.from_user.id)
        data = load_data()
        data.setdefault(user_id, {"budget": {}, "log": []})
        data[user_id]["log"].append({"category": category, "amount": amount})
        save_data(data)
        await update.message.reply_text(f"📌 Записано: {amount} в категорию '{category}'")
    except:
        await update.message.reply_text("❌ Используй: /log <категория> <+/-сумма>")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    data = load_data()
    user_data = data.get(user_id, {"budget": {}, "log": []})
    summary_text = "📊 Финансовая сводка:\n"
    total = 0
    for entry in user_data["log"]:
        total += entry["amount"]
    summary_text += f"💰 Общий баланс: {total}\n\n"
    summary_text += "🎯 Бюджеты:\n"
    for cat, val in user_data["budget"].items():
        summary_text += f"- {cat}: {val}\n"
    await update.message.reply_text(summary_text)

async def notify_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 Уведомления включены (в демо не реализовано).")

async def notify_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔕 Уведомления отключены.")
