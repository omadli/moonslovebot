from aiogram import types


main_keyb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [types.KeyboardButton(text="Moon")],
        [types.KeyboardButton(text="Help Me"), types.KeyboardButton(text="Statistics")]                
    ]
)

cool_keyb = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [types.KeyboardButton(text="Cool")]
    ]
)

