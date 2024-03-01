from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ContentType
from Core.hendlers.basic import get_start, get_photo, get_hello, get_help, get_button, get_location
from Core.filters.iscontact import IsTrueContact
from Core.hendlers.contact import get_true_contact, get_fake_contact
from Core.settings import settings
from aiogram.filters import Command
from Core.utils.commands import get_commands
from Core.hendlers.basic import get_inline
from Core.hendlers.callback import select_macbook
from Core.utils.callbackdata import MacInfo
import asyncio
import logging
from Core.hendlers.pay import order, pre_checkout_query, sussessful_payment


async def start_bot(bot: Bot):
    await get_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot started!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stopped!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(sussessful_payment, F.pre_checkout_query)
    dp.message.register(get_inline, Command(commands=['inline']))
    # dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
    # dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'Pro')) фильтр который позволяет пройти только моделям 'Pro'
    dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_hello, F.text == 'Hello')
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_button, Command(commands=['button']))
    dp.message.register(get_location, F.location)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

