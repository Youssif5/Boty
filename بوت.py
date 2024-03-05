from telethon import TelegramClient, events
from telethon.tl.custom import Button

# Replace these values with your own API credentials and user token
api_id = '26957529'
api_hash = 'ffe7d862b0a31893682a62bbc0654ced'
user_token = '7085830411:AAFGljA6ra15aMhLYsurJ2r32qpCSOZEPqk'

# Create a TelegramClient instance
client = TelegramClient('user_session', api_id, api_hash)

# Define a function to block users who haven't set a username
async def block_user(event):
    """
    Check if the message sender has a username set.
    If not, delete the message and send a notification.
    """
    while True:
        if not event.sender.username:
            await event.delete()
            await event.respond(
                "تم المنع 👍\n\nشكرًا لاستخدامك هذا البوت! لو أعجبك، لا تتردد في إضافتي إلى مجموعاتك باستخدام الأمر /addme",
                buttons=[[Button.inline("ضفني لمجموعتك", b"add_to_group")]]
            )
        else:
            break

# Define a function to respond to the /start command
async def start_command(event):
    """
    Respond to the /start command with a welcome message.
    """
    await event.respond(
        "مرحباً بك! هذا البوت يقوم بعمل معين، يمكنك الضغط على الزر أو إرسال /help للحصول على قائمة بالأوامر المتاحة."
    )

# Define a function to respond to the /help command
async def help_command(event):
    """
    Respond to the /help command with a list of available commands.
    """
    await event.respond(
        "قائمة الأوامر المتاحة:\n/start - لبدء استخدام البوت\n/help - لعرض قائمة الأوامر\n/addme - لدعوة البوت لمجموعتك"
    )

# Register functions to handle incoming messages
@client.on(events.NewMessage(incoming=True))
async def handle_message(event):
    """
    Handle incoming messages.
    """
    if event.message.message.startswith("/start"):
        await start_command(event)
    elif event.message.message.startswith("/help"):
        await help_command(event)
    elif event.message.message.startswith("/logout"):
        await client.log_out()
    else:
        await block_user(event)

# Run the client indefinitely
client.start(user_token=user_token)
client.run_until_disconnected()