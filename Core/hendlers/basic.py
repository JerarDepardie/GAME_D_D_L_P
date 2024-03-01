from aiogram import Bot
from aiogram.types import Message
from Core.keyboards.reply import reply_keybord, request_keyboard, get_reply_keyboard
from Core.keyboards.inline import select_macbook, get_inline_keyboard
import json


# async def get_inline(message: Message, bot: Bot):
#     await message.answer(f"It's inline keyboard, test it",
#                          reply_markup=select_macbook)

async def get_inline(message: Message, bot: Bot):
    await message.answer(f"It's inline keyboard, test it",
                         reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Hi {message.from_user.first_name}, you cute!</b>')
    await message.answer(f'<s>Hi {message.from_user.first_name}, you cute!</s>')
    await message.reply(f'<tg-spoiler>Hi {message.from_user.first_name}, you cute!</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Good! you send photo, I save it.")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo1.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Hi, my homie. Glad to see you!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


async def get_help(message: Message, bot: Bot):
    await message.answer(f"It's button no worked",
                         reply_markup=get_reply_keyboard())


async def get_button(message: Message, bot: Bot):
    await message.answer(f"<b>Give me ALL</b>",
                         reply_markup=request_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f'You send location!\r\a'
                         f'{message.location.latitude}\r\a{message.location.longitude}')
