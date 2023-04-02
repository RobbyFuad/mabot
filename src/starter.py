from telegram import Update, Dice, constants
from telegram.ext import CallbackContext, ContextTypes

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("How May I Help You? \U0001F60A")
    
async def evilbot(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Give bot for admin, and miracle will come \U0001F608 \U0001F608 \U0001F608")

async def userinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''
id: {update.effective_user.id}
first name: {update.effective_user.first_name}
username: @{update.effective_user.username}
''')

async def game(update: Update, context: CallbackContext) -> None:
    games = Dice(64, constants.DiceEmoji.SLOT_MACHINE)
    await update.message.reply_text(reply_markup=games)
