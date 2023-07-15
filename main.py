import logging

from telegram import __version__ as TG_VER

from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    ConversationHandler,
    filters,
)
import routeMan as rr

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
MAX_LEVEL = 2


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Enter Your Group Name: ")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    msg = ""
    for k, v in groups.items():
        msg += f"{k} is at {v} level\n"
    await update.message.reply_text(msg)


async def grpName(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data:
        return

    global groups
    name = update.message.text
    groups[name] = 0

    rr.getRoute(name)

    context.user_data["name"] = name
    context.user_data["selfie_pending"] = False
    logger.info("Group: %s user_data: %s", groups, context.user_data)
    await update.message.reply_text(f"Your Group name is {name}")


async def qr(update: Update, cxt: ContextTypes.DEFAULT_TYPE) -> None:
    if not cxt.user_data:
        await update.message.reply_text("Enter Your Group Name: ")
        return

    name = cxt.user_data["name"]
    user = update.message.from_user
    print(user)
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive(f"qr_{name}_{groups[name]}.jpg")
    logger.info("Grp: %s upload QR: %s", name, f"qr_{name}_{groups[name]}.jpg")

    cxt.user_data["selfie_pending"] = True
    await update.message.reply_text("Verfied send selfie")


async def photo(update: Update, cxt: ContextTypes.DEFAULT_TYPE) -> None:
    global groups

    name = cxt.user_data["name"]
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive(f"selfie_{name}_{groups[name]}.jpg")
    groups[name] += 1
    cxt.user_data["selfie_pending"] = False

    logger.info("Grp: %s upload Selfie: %s", name, f"selfie_{name}_{groups[name]}.jpg")
    logger.info("Group: %s user_data: %s", groups, cxt.user_data)
    if groups[name] >= MAX_LEVEL:
        await update.message.reply_text("Done")
    else:
        await update.message.reply_text(
            "Next riddle" + rr.getRiddle(name, groups[name])
        )


def main() -> None:
    application = (
        Application.builder()
        .token("6058419192:AAG9n9POKFYC7XPi15Tsr-I_LVFBBfr4M2g")
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", stats))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, grpName))
    application.add_handler(
        MessageHandler(
            filters.PHOTO,
            lambda u, c: photo(u, c)
            if c.user_data and c.user_data["selfie_pending"]
            else qr(u, c),
        )
    )

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    # for i in range(7):
    #     rr.getRouteRand("GRP_" + str(i))
    main()

# TODO: QR code stop after done
# TODO: QR code verfication
