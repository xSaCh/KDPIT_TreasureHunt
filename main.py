import logging
import time
import routeMan as rr
import recover
from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    ConversationHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("a.log")
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

logging.getLogger("httpx").setLevel(logging.WARNING)

logging.getLogger("routeMan").addHandler(fh)
logging.getLogger("routeMan").addHandler(ch)
logger = logging.getLogger(__name__)
logger.addHandler(fh)
logger.addHandler(ch)

groups = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        "For any technical difficulties please contact any of this cooridinator:\nSamarth: https://t.me/sam_ch_7"
    )
    await update.message.reply_text("Enter Your Group Name: ")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    msg = ""
    for k, v in groups.items():
        msg += f"{k} is completed {v-1} riddles\n"
    await update.message.reply_text(msg)


async def begin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = context.user_data["name"]
    i = rr.teams.index(name) + 1
    print(f"Riddles\\{i}0.jpg")
    await update.message.reply_text("Your First riddle")
    await update.message.reply_photo(open(f"Riddles\\{i}0.jpg", "rb"))


async def grpName(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data:
        return

    global groups
    name = update.message.text
    groups[name] = 1
    # IDS.append([update.effective_chat.id, name])
    rr.setRoute(name)

    context.user_data["name"] = name
    context.user_data["selfie_pending"] = False

    recover.backup("groups", groups)
    recover.backup(f"ctx_{name}", context.user_data)
    logger.info("Group: %s", groups)
    logger.info("Group: %s user_data: %s", name, context.user_data)

    await update.message.reply_text(f"Your Group name is {name}")


async def qr(update: Update, cxt: ContextTypes.DEFAULT_TYPE) -> None:
    if not cxt.user_data:
        await update.message.reply_text("Enter Your Group Name: ")
        return

    name = cxt.user_data["name"]
    user = update.message.from_user
    print(user)

    data = update.message.text

    logger.info(
        "Grp: %s add QR code: %s",
        name,
        data,
    )
    # Final Treasure Verification
    if groups[name] == rr.TOTAL_RIDDLES:
        cxt.user_data["selfie_pending"] = True
        cxt.user_data["Riddle"] = -1
        await update.message.reply_text("Verfied! send selfie")
        return

    # Code Verification
    riddle = rr.getRiddle(name, groups[name], data)
    if riddle != -1:
        cxt.user_data["selfie_pending"] = True
        cxt.user_data["Riddle"] = riddle
        await update.message.reply_text("Verfied send selfie")
        return

    await update.message.reply_text("Invalid Qr Code or resend it clear")


async def photo(update: Update, cxt: ContextTypes.DEFAULT_TYPE) -> None:
    global groups

    if not (cxt.user_data and cxt.user_data["selfie_pending"]):
        await update.message.reply_text("Upload code first")
        return

    name = cxt.user_data["name"]

    # Download selfie
    _fileName = f"Imgs\\selfie_{time.strftime('(%H-%M-%S)')}_{name}_{groups[name]}.jpg"

    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        await photo_file.download_to_drive(_fileName)

    cxt.user_data["selfie_pending"] = False

    logger.info(
        "Grp: %s upload Selfie: %s",
        name,
        _fileName,
    )
    recover.backup("groups", groups)
    recover.backup(f"ctx_{name}", cxt.user_data)
    logger.info("Group: %s", groups)
    logger.info(
        "Group: %s user_data: %s riddle: %s",
        name,
        cxt.user_data,
        cxt.user_data["Riddle"],
    )

    # next riddle
    if groups[name] == rr.TOTAL_RIDDLES:
        await update.message.reply_text("Congrats for winning our TreasureHunt 🎉🥂🎊🎁")
    else:
        await update.message.reply_text("Your Next riddle")
        await update.message.reply_photo(
            open(f"Riddles\\{cxt.user_data['Riddle']}.jpg", "rb")
        )
    groups[name] += 1


def main() -> None:
    application = (
        Application.builder()
        .token("6058419192:AAG9n9POKFYC7XPi15Tsr-I_LVFBBfr4M2g")
        .build()
    )
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("begin", begin))

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            lambda u, c: qr(u, c) if c.user_data else grpName(u, c),
        )
    )
    application.add_handler(CommandHandler("p", photo))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

# TODO: QR code stop after done
# TODO: QR code verfication
