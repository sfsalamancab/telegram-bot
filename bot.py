from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Tu token
TOKEN = "8324581126:AAE5TnIQSxqIkKm7DJ9nV2Kq--lLcjbjYNY"

# Función de bienvenida con menú
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 Derecho de Petición"],
        ["⚖️ Acción de Tutela"]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,  # <- botones siempre visibles
        is_persistent=True        # <- corrección aquí
    )

    await update.message.reply_text(
        "Hola, soy el Bot de Un Abogado Contra el Cáncer y estoy para ayudarte en la defensa de tus derechos fundamentales.\n\n"
        "Selecciona una de las siguientes opciones:",
        reply_markup=reply_markup
    )

# Enviar documentos según la opción seleccionada
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📄 Derecho de Petición":
        await update.message.reply_document(open("derecho_peticion.docx", "rb"))
        await update.message.reply_text("Aquí tienes tu formato de Derecho de Petición ✅")

    elif text == "⚖️ Acción de Tutela":
        await update.message.reply_document(open("accion_tutela.docx", "rb"))
        await update.message.reply_text("Aquí tienes tu formato de Acción de Tutela ✅")

    else:
        await update.message.reply_text("Por favor selecciona una opción válida del menú.")

# Función principal
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
    