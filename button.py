from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp.client import request

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍱Menu"), KeyboardButton(text="Malumot❔")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)
ovqat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍟Fast-Food"), KeyboardButton(text="🍾Ichimliklar")],

    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)
kochataomi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍕Pitsa"), KeyboardButton(text="🌮Lavash")],
        [KeyboardButton(text="🌭Hot-dog"), KeyboardButton(text="🥟Shaverma")],
        [KeyboardButton(text="🥟Somsa"), KeyboardButton(text="🍔Gamburger")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
ichimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍻Coca-cola"), KeyboardButton(text="🍷Pepsi")],
        [KeyboardButton(text="🍸Fanta"), KeyboardButton(text="🍹Sprite")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
zakaz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍Manzilimni yuborish",request_location=True), KeyboardButton(text="Bekor qilish")]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
    
)
raqam = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Raqamimni ulashish",request_contact=True)],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)