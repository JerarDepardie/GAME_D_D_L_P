from aiogram.types import Message
from aiogram import Bot


async def get_true_contact(message: Message, bot: Bot, phone: str):
    await message.answer(f"Good it's your <b>contact</b> =) {phone}")


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f"No no no,  it's not your <b>contact</b>, stop it, send <b>YOUR</b> contact.")
