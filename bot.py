import telebot

# ရရှိထားသော Token နှင့် Chat ID များ
TOKEN = '8745766599:AAHFC38Zza-YC56neTJj--9wByQieCd4QFk'
ADMIN_CHAT_ID = '6868820956'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ Boss ရဲ့ Solo Genius Musical School (YGLC) မှ ကြိုဆိုပါတယ်။ သင်တန်းအပ်နှံရန်နှင့် ငွေလွှဲအတည်ပြုရန် ဤ Bot ကို အသုံးပြုနိုင်ပါသည်။ ကျေးဇူးပြု၍ ငွေလွှဲ Screenshot ပုံကို ပို့ပေးပါ။")

# ကျောင်းသားများ ပို့လိုက်သော ငွေလွှဲ Screenshot ပုံများကို Admin (Boss) ဆီသို့ တိုက်ရိုက် Forward လုပ်ပေးခြင်း
@bot.message_handler(content_types=['photo'])
def handle_payment_screenshot(message):
    # Boss ဆီသို့ ပုံနှင့်တကွ ပို့ပေးမည်
    bot.forward_message(chat_id=ADMIN_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.reply_to(message, "✔ ငွေလွှဲ Screenshot ကို Boss ဆီသို့ အောင်မြင်စွာ ပို့ပြီးပါပြီ။ Admin မှ စစ်ဆေးအတည်ပြုပြီးပါက 24 နာရီအတွင်း သင်တန်းစတက်နိုင်ပါပြီ။")

# စာသားများ ပို့လာပါက တုံ့ပြန်ရန်
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, "ကျေးဇူးပြု၍ ငွေလွှဲ Screenshot (ပုံ) ကို ပို့ပေးပါရန်။ အသေးစိတ်သိလိုပါက Admin သို့ ဆက်သွယ်ပါ။")

if __name__ == '__main__':
    print("Solo Genius Bot is running successfully...")
    bot.infinity_polling()