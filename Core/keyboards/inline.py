from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Core.utils.callbackdata import MacInfo


select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2013',
            callback_data='apple_air_13_m1_2013'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14" M1 2021',
            callback_data='apple_pro_14_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 16" i7 2019',
            callback_data='apple_pro_16_i7_2019'
        )
    ],
    [
        InlineKeyboardButton(
            text='YouTube',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
        ),
        InlineKeyboardButton(
            text='Jerar Depardie',
            url='tg://user?id=473515014'
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13" M1 2013', callback_data=MacInfo(model='Air', size=13, chip='m1', year=2013))
    keyboard_builder.button(text='Macbook Pro 14" M1 2021', callback_data=MacInfo(model='Pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='Macbook Pro 16" i7 2019', callback_data=MacInfo(model='Pro', size=16, chip='i7', year=2019))
    keyboard_builder.button(text='YouTube', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
    keyboard_builder.button(text='Jerar Depardie', url='tg://user?id=473515014')

    keyboard_builder.adjust(1, 1, 1, 2)
    return keyboard_builder.as_markup()