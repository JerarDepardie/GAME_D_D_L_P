from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        #     Куда отправится счет
        chat_id=message.chat.id,

        #     Название продукта (до 32 символов)
        title='My home video',

        #     Описание продукта (до 255 символов)
        description="It's my video, how i worked, and go party",

        #     Внутренняя информация которая не отображается пользователю, можно использовать для сбора информации
        payload='I don no what i writ there',

        #     Токен провайдера
        provider_token='381764678:TEST:70818',

        #     Валюта платежа
        currency='rub',

        #     Цена пишется в копейках, то есть нужно обычнкую сумму умножить на 100
        prices=[
            LabeledPrice(
                label='Доступ к секретному видео',
                amount=90000
            ),
            LabeledPrice(
                label='НДС',
                amount=-20000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-40000
            )
        ],

        #     Максимальная сумма чаевых
        max_tip_amount=50000,

        #     Список предлогаемых выборов чаевых
        suggested_tip_amounts=[5000, 15000, 30000],

        #     Для перессылки на оплату (если поле пустое отпроется оплата, иначе будет ссылка на бота)
        start_parameter='',

        #     Не понял
        provider_data=None,

        #     Ссылка на кортинку, которая будет отображатся в счете
        photo_url='https://i1.sndcdn.com/artworks-XJdVplPCbvDvJlH7-jF9c4A-t500x500.jpg',

        #     Размер картинки
        photo_size=100,

        #     Ширина картинки
        photo_width=800,

        #     Высота картинки
        photo_height=450,

        #     Если нужно полное имя пользователя то 'True'
        need_name=True,

        #     Если нужен е-мейл
        need_email=True,

        #     Если нужен номер телефона
        need_phone_number=False,

        #     Если нужен адрес, для доставки
        need_shipping_address=False,

        #     Если платежный провайдер просит номер телефона то 'True'
        send_phone_number_to_provider=False,

        #     Если платежный провайдер просит е-мейл
        send_email_to_provider=False,

        #     Если цена зависит от доставки
        is_flexible=False,

        #     'True' если хотите что бы сообщение было доставлено без звука
        disable_notification=False,

        #     'True' что бы нельзя было переслать, скопировать пост (защитить пост)
        protect_content=False,

        #     Что бы переслать счет цитируя сообщение (указать id сообщения)
        reply_to_message_id=None,

        #     Отправить счет на оплату, даже если цитируемое сообщение не найдено
        allow_sending_without_reply=True,

        #     Добавить клавиатуру (первая кнопка должна быть "оплатить")
        reply_markup=None,

        #     Не понял
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def sussessful_payment(message: Message):
    msg = f'Спасибо за покупку {message.successful_payment.total_amount // 100} {message.successful_payment.currency}' \
          f'\r\nВот ссылка на мое хоум видио https://www.youtube.com/results?search_query=never+gonna+give+you+up'
    await message.answer(msg)
