from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.misc import messages


commands_router = Router(name='commands')


@commands_router.message(CommandStart())
async def command_start(message: Message):
    await message.reply(messages.hello.format(username=message.from_user.username))
