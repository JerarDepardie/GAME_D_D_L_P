from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def get_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Start Bot'),

        BotCommand(command='help',
                   description='Help'),

        BotCommand(
            command='cancel',
            description='stop it'
        ),
        BotCommand(
            command='button',
            description='Send location, your contact or quiz'
        ),
        BotCommand(
            command='inline',
            description='Look inline keyboard'
        ),
        BotCommand(
            command='pay',
            description='My Market'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())