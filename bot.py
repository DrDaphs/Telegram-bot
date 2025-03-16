import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Replace this with your token from BotFather
API_TOKEN = "7881055278:AAHPCfeoyvC5q51pmCyJ4-Momh5PbOGKOxA"

# Initialize the bot application
app = Application.builder().token(API_TOKEN).build()

# Define a menu keyboard
menu_keyboard = [
    ["📖 Content Creation", "📍 Where to Post"],
    ["🏆 Brand Representation", "🌍 Community Building"],
    ["📜 Rules", "🛡 Stonbassadorship"]
]
reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

# Function to get total users
def get_total_users():
    if not os.path.exists("users.txt"):
        return 0
    with open("users.txt", "r") as file:
        users = file.readlines()
    return len(set(users))  # Avoid duplicate users

# Define the /start command handler
async def start(update: Update, context):
    user = update.message.from_user
    user_id = str(user.id)

    # Save user data (avoid duplicates)
    if not os.path.exists("users.txt"):
        open("users.txt", "w").close()

    with open("users.txt", "r+") as file:
        users = file.readlines()
        if user_id + "\n" not in users:
            file.write(user_id + "\n")

    total_users = get_total_users()

    await update.message.reply_text(
        f"👋 Hello, this is Web3 Ambassador Mastery! 🚀\n\n"
        f"Unlock the secret to successfully representing Web3 projects as a brand ambassador, "
        f"empowering you to authentically promote innovative technologies and foster a loyal community.\n\n"
        f"👥 Total users: {total_users}",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Define the /stats command handler (Admin feature)
async def stats(update: Update, context):
    total_users = get_total_users()
    await update.message.reply_text(f"📊 Total users: {total_users}")

# Define responses for menu buttons
async def menu_response(update: Update, context):
    text = update.message.text

    responses = {
        "📖 Content Creation": (
            "📖 CHARACTERISTICS OF CONTENTS\n\n"
            "🔹 A) Introduction\n🔹 B) Body\n🔹 C) Conclusion\n🔹 D) CTA (Call TO Actions)\n\n"
            "Introduction: Use a hook to grab attention!\n"
            "For example: 'How to make $10,000 from Crypto' is more engaging than 'Let's talk about making money from crypto.'\n\n"
            "Body: The main content, structured like a narrative essay.\n\n"
            "Conclusion: Your final thoughts and how people should react.\n\n"
            "CTA: Tell readers what to do (like, comment, follow, share, etc.)."
        ),
        "📍 Where to Post": (
            "📝 TYPES OF CONTENTS & WHERE TO POST\n\n"
            "We focus on written content first, as the same strategy applies to audio/video.\n\n"
            "🔹 Posts: Facebook, Instagram, LinkedIn, Twitter.\n"
            "🔹 Articles: Medium, Quora, CoinMarketCap, Binance.\n"
            "🔹 Threads: Twitter, Threads App (Instagram)."
        ),
        "🏆 Brand Representation": (
            "🏆 Brand Representation\n\n"
            "Do it your way, be visible, and let the brand be seen through you!"
        ),
        "🌍 Community Building": (
            "🌍 How to Build a Web3 Community\n\n"
            "🔹 Host AMAs (Ask Me Anything) to engage with the community.\n"
            "🔹 Collaborate with other ambassadors to expand reach.\n"
            "🔹 Use Telegram, Discord, or Facebook Groups to manage communities.\n\n"
            "These strategies will help promote the brand, foster loyalty, and drive engagement!"
        ),
        "📜 Rules": (
            "📜 Rules to Follow as an Ambassador\n\n"
            "🔹 Follow the brand colors and check the Brandbook.\n"
            "🔹 Don't shill! Some platforms have strict rules.\n"
            "🔹 Talk from personal experience for authenticity.\n"
            "🔹 Always check the official website and guides before posting."
        ),
        "🛡 Stonbassadorship": (
            "🛡 STONBASSADORSHIP REWARDS\n\n"
            "Unlock a 10% bonus on your first reward with referral code 111416 when you join the STON.fi Ambassador Program!\n\n"
            "Earn up to 10,000 $STON monthly by:\n"
            "🔹 Creating content 🎨\n"
            "🔹 Hosting events 🎤\n"
            "🔹 Engaging with the community 💬\n\n"
            "Submit your work here: [STON.fi Stonbassadors](https://ston.fi/stonbassadors)"
        )
    }

    response = responses.get(text, "I didn't understand that. Please use the menu.")
    await update.message.reply_text(response, parse_mode="Markdown")

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stats", stats))  # Show total users with /stats
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_response))

# Start the bot
print("Bot is running with a custom menu and user tracking...")
app.run_polling()