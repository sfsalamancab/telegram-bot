import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Cargar token de Telegram desde variable de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")

# --- Función de bienvenida ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["ℹ️ Información General", "📄 Formatos"],
        ["👨🏼‍⚖️ Consultorio Jurídico", "🤝 Apóyanos"],
        ["📞 Contáctanos"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🤖 Bienvenido al Bot de *Un Abogado Contra el Cáncer*\n"
        "Este espacio fue creado para apoyarte en la defensa de tus derechos fundamentales de manera sencilla, gratuita y didáctica.\n\n"
        "Aquí podrás encontrar:\n"
        "📚 Información clara sobre mecanismos legales que te protegen.\n"
        "📄 Formatos listos para ejercer tus derechos.\n"
        "👨🏼‍⚖️ Un canal de orientación para remitir tu caso a un consultorio jurídico universitario.\n\n"
        "🤔 Cuando conoces y reclamas tus derechos, conviertes la dignidad en acción y la justicia en realidad.\n\n"
        "Elige una de las siguientes opciones para comenzar 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- Información General ---
async def informacion_general(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📘 ¿Qué es el Derecho de Petición?"],
        ["⚖️ ¿Qué es la Acción de Tutela?"],
        ["❓ Preguntas frecuentes"],
        ["🔙 Volver al Menú Principal"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Selecciona un tema para conocer más 👇", reply_markup=reply_markup)

async def derecho_peticion_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 *Derecho de Petición*\n\n"
        "Es un derecho fundamental (art. 23 C.P.) que permite a cualquier persona solicitar información, documentos o respuestas a entidades públicas "
        "y en ciertos casos a privadas. En salud es clave para medicamentos, procedimientos o tratamientos.\n\n"
        "📌 *Datos clave:*\n"
        "💸 Gratuito y sin necesidad de abogado.\n"
        "🔍 Respuesta obligatoria, clara y completa.\n"
        "👨🏼‍⚖️ Si no hay respuesta o es incompleta, procede la Acción de Tutela.\n"
        "⏰ Plazos: 15 días (información), 10 días (copias), 30 días (consultas).\n"
        "⚡ En casos urgentes pueden decretarse *medidas cautelares*.\n\n"
        "📝 *Nota aclarativa:*\n"
        "Este formato está enfocado en solicitudes de medicamentos, procedimientos, exámenes médicos y/o tratamientos. "
        "Si necesitas otro tipo de formato, ve al menú 📞 *Contáctanos*.",
        parse_mode="Markdown"
    )

async def accion_tutela_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚖️ *Acción de Tutela*\n\n"
        "Mecanismo constitucional para proteger derechos fundamentales cuando estos resultan vulnerados o amenazados. "
        "En salud es clave cuando la vida o integridad están en riesgo.\n\n"
        "📌 *Datos clave:*\n"
        "⚡ Respuesta máxima: 10 días hábiles.\n"
        "⚠️ Pueden decretarse *medidas provisionales* si existe riesgo inminente.\n\n"
        "🖥️ Radica tu tutela en línea (días hábiles, 8:00 a.m. a 5:00 p.m.):\n"
        "👉 [Radicar Tutela en Línea](https://procesojudicial.ramajudicial.gov.co/tutelaenlinea)\n\n"
        "📝 *Nota aclarativa:*\n"
        "Formato enfocado en casos de *diagnóstico médico*. Para otros enfoques (tratamiento o servicios complementarios), solicita orientación en 📞 *Contáctanos*.",
        parse_mode="Markdown"
    )

async def preguntas_frecuentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *Preguntas Frecuentes*\n\n"
        "🔹 ¿Necesito abogado para presentar un Derecho de Petición? → No, es gratuito y no requiere abogado.\n"
        "🔹 ¿Qué hago si no me responden un Derecho de Petición? → Puedes acudir a la Acción de Tutela.\n"
        "🔹 ¿Cuánto tarda la respuesta de una tutela? → Máximo 10 días hábiles.\n"
        "🔹 ¿Dónde puedo presentar una tutela? → De manera presencial o virtual en: "
        "[Radicar Tutela en Línea](https://procesojudicial.ramajudicial.gov.co/tutelaenlinea)",
        parse_mode="Markdown"
    )

# --- Formatos ---
async def formatos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 Derecho de Petición"],
        ["⚖️ Acción de Tutela"],
        ["🔙 Volver al Menú Principal"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Selecciona el formato que necesitas 👇", reply_markup=reply_markup)

async def derecho_peticion_doc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(open("derecho_peticion.docx", "rb"))
    await derecho_peticion_info(update, context)

async def accion_tutela_doc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(open("accion_tutela.docx", "rb"))
    await accion_tutela_info(update, context)

# --- Consultorio Jurídico ---
async def consultorio_juridico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👨🏼‍⚖️ *Consultorio Jurídico*\n\n"
        "Este espacio es tu **primer punto de orientación legal** para los retos que afectan tu salud y bienestar.\n\n"
        "Durante una *entrevista virtual de 30 minutos*:\n"
        "✅ Escucharemos y analizaremos tu caso de forma preliminar.\n"
        "✅ Evaluaremos si cumple con los criterios para remitirlo a un **consultorio jurídico universitario** que brinde asesoría gratuita y especializada.\n\n"
        "📝 *Nota aclarativa:*\n"
        "Orientación con énfasis en temas civiles, administrativos y laborales vinculados a personas con cáncer o sospecha de cáncer.\n\n"
        "📅 Agenda tu entrevista aquí:\n"
        "👉 [Reservar cita en Calendly](https://calendly.com/sfsalamancab/30min)",
        parse_mode="Markdown"
    )

# --- Apóyanos ---
async def apoyanos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🌐 Donar con Nequi (QR y Llave)"],
        ["📲 Síguenos en redes"],
        ["🔙 Volver al Menú Principal"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Tu apoyo nos ayuda a seguir defendiendo derechos 💜", reply_markup=reply_markup)

async def donar_nequi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_photo(
            open("qr_nequi.jpeg", "rb"),
            caption=(
                "🌐 *Donar con Nequi (QR y Llave)*\n\n"
                "Escanea este QR con tu app de Nequi para realizar tu donación.\n\n"
                "🔑 También puedes hacer tu donativo usando la **Llave Nequi – Bre-B**: *0090702453*"
            ),
            parse_mode="Markdown"
        )
    except FileNotFoundError:
        await update.message.reply_text("❌ No encontré el archivo del QR. Verifica que `qr_nequi.jpeg` esté en el repositorio.")

async def redes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📲 *Síguenos en redes*\n\n"
        "Encuéntranos como *Un Abogado Contra el Cáncer* en:\n"
        "🎵 TikTok\n"
        "📸 Instagram\n"
        "💼 LinkedIn",
        parse_mode="Markdown"
    )

# --- Contáctanos ---
async def contactanos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Contáctanos*\n\n"
        "Si necesitas un formato diferente o una orientación especial:\n"
        "📅 Agenda tu cita en Calendly → [Haz clic aquí](https://calendly.com/sfsalamancab/30min)\n\n"
        "📱 También puedes escribirnos al WhatsApp oficial:\n"
        "👉 [3202484520](https://wa.me/573202484520)",
        parse_mode="Markdown"
    )

# --- Volver al Menú Principal ---
async def volver_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

# --- Manejo de mensajes ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    mapping = {
        "ℹ️ Información General": informacion_general,
        "📘 ¿Qué es el Derecho de Petición?": derecho_peticion_info,
        "⚖️ ¿Qué es la Acción de Tutela?": accion_tutela_info,
        "❓ Preguntas frecuentes": preguntas_frecuentes,
        "📄 Formatos": formatos,
        "📄 Derecho de Petición": derecho_peticion_doc,
        "⚖️ Acción de Tutela": accion_tutela_doc,
        "👨🏼‍⚖️ Consultorio Jurídico": consultorio_juridico,
        "🤝 Apóyanos": apoyanos,
        "🌐 Donar con Nequi (QR y Llave)": donar_nequi,
        "📲 Síguenos en redes": redes,
        "📞 Contáctanos": contactanos,
        "🔙 Volver al Menú Principal": volver_menu
    }
    if text in mapping:
        await mapping[text](update, context)
    else:
        await update.message.reply_text("Por favor selecciona una opción válida del menú.")

# --- Función principal ---
def main():
    if not TOKEN:
        raise ValueError("❌ No se encontró TELEGRAM_TOKEN en las variables de entorno.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
