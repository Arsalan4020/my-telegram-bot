import telebot

# توکن ربات خودت رو اینجا بذار
BOT_TOKEN = '7937056748:AAHLlC50a7SB1m3AwqZ0F9So7QPDsKLlVyY'

bot = telebot.TeleBot(BOT_TOKEN)

# دیکشنری برای ذخیره آدرس‌های هر کاربر
user_addresses = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! آدرس‌های کیف پول Solana رو با دستور /add بفرست.")

@bot.message_handler(commands=['add'])
def add_address(message):
    try:
        address = message.text.split()[1]
        user_id = message.chat.id

        if user_id not in user_addresses:

            user_addresses[user_id] = []

        if address not in user_addresses[user_id]:
            user_addresses[user_id].append(address)
            bot.reply_to(message, f"✅ آدرس ذخیره شد: {address}")
        else:
            bot.reply_to(message, "این آدرس قبلاً اضافه شده.")

    except IndexError:
        bot.reply_to(message, "فرمت درست نیست. به شکل زیر بنویس:\n/add آدرس")

@bot.message_handler(commands=['list'])
def list_addresses(message):
    user_id = message.chat.id
    addresses = user_addresses.get(user_id, [])
    if addresses:
        bot.reply_to(message, "آدرس‌های ثبت‌شده:\n" + "\n".join(addresses))
    else:
        bot.reply_to(message, "هنوز هیچ آدرسی ثبت نکردی.")

print("ربات با موفقیت اجرا شد و منتظر پیام‌هاست...")
bot.infinity_polling()