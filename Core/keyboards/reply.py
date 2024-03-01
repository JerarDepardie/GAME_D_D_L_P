from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Первый способ создания кнопок через списки
reply_keybord = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Row 1, Button 1'
        ),
        KeyboardButton(
            text='Row 1, Button 2'
        ),
        KeyboardButton(
            text='Row 1, Button 3'
        )
    ],
    [
        KeyboardButton(
            text='Row 2, Button 1'
        ),
        KeyboardButton(
            text='Row 2, Button 2'
        )
    ],
    [
        KeyboardButton(
            text='Row 3, Button 1'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='↧↧↧ Hit button ↧↧↧')


request_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='request location',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='request contact',
            request_contact=True
        ),
        KeyboardButton(
            text='Quiz',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='What are you want send me?')


# ВТОРОЙ СПОСОБ СОЗДАНИЯ КНОПОК ЧЕРЕЗ ФУНКЦИЮ
def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Row 1, Button 1')
    keyboard_builder.button(text='Row 1, Button 2')
    keyboard_builder.button(text='Row 1, Button 3')
    keyboard_builder.button(text='Row 2, Button 1')
    keyboard_builder.button(text='Row 2, Button 2')
    keyboard_builder.button(text='request contact', request_contact=True)
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='↧↧↧ Hit button ↧↧↧')
