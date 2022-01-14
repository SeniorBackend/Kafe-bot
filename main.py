
from email import message
import logging
from os import replace, stat
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import state
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from button import menu,ichimliklar,kochataomi,ovqat,zakaz,raqam
from statelar import Translate
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\nBizning kafe botga xush kelibsiz😄\nBu bot hozircha test rejimida😄", reply_markup=menu)
@dp.message_handler(Text(equals="🍱Menu"))
async def jjj(message):
    await message.answer('🍱Menu',reply_markup=ovqat)

@dp.message_handler(Text(equals="Malumot❔"))
async def www(message):
    await message.answer('Agar xaridiz 30000 so\'mdan o\'tsa shahar ichi bo\'ylab yetkazib berish tekin\nBot yaratuvchi @deSeniorcoder')

@dp.message_handler(Text(equals="🍟Fast-Food"))
async def ff(message):
    await message.answer('Nechta buyurtma qilasiz?😃',reply_markup=kochataomi)
@dp.message_handler(Text(equals="🍕Pitsa"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.pitsaset.set()
@dp.message_handler(Text(equals="🌮Lavash"))
async def wwwww(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.lavashset.set()
@dp.message_handler(Text(equals="🍔Gamburger"))
async def wwwww(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.gamburgerset.set()
@dp.message_handler(Text(equals="🥟Shaverma"))
async def www(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.shavermaset.set()
@dp.message_handler(Text(equals="🌭Hot-dog"))
async def ffwww(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.hotdogset.set()
@dp.message_handler(Text(equals="🥟Somsa"))
async def fwf(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.somsaset.set()
@dp.message_handler(state=Translate.gamburgerset)
async def sss(message,state:FSMContext):

    await message.answer(f'{message.text} 🍔{int(message.text)*12000}so\'m💴',reply_markup=raqam)

    await state.finish()
@dp.message_handler(state=Translate.pitsaset)
async def ss(message,state:FSMContext):
    await message.answer(f'{message.text} 🍕 {int(message.text)*16000}so\'m💴',reply_markup=raqam)

    await state.finish()
@dp.message_handler(state=Translate.hotdogset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🌭 {int(message.text)*9000}so\'m💴',reply_markup=raqam)
    await state.finish()

    



@dp.message_handler(state=Translate.somsaset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🥟 {int(message.text)*8000}so\'m💴',reply_markup=raqam)
    await state.finish()
@dp.message_handler(state=Translate.shavermaset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🥟 {int(message.text)*10000}so\'m💴',reply_markup=raqam)

    await state.finish()
@dp.message_handler(state=Translate.lavashset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🌮 {int(message.text)*17000}so\'m💴',reply_markup=raqam)

    await state.finish()



@dp.message_handler(Text(equals="🍾Ichimliklar"))
async def ff(message):
    await message.answer('Yaxna ichimliklar🍷',reply_markup=ichimliklar)
@dp.message_handler(Text(equals="🍻Coca-cola"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.colaset.set()
@dp.message_handler(Text(equals="🍸Fanta"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.fantaset.set()
@dp.message_handler(Text(equals="🍹Sprite"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.spriteset.set()

@dp.message_handler(Text(equals="🍷Pepsi"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?😃')
    await Translate.pepsiset.set()

@dp.message_handler(state=Translate.colaset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🍻 {int(message.text)*9000}so\'m💴',reply_markup=raqam)
    await state.finish()

@dp.message_handler(state=Translate.pepsiset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🍷 {message.text}{int(message.text)*8000}so\'m💴',reply_markup=raqam)
    await state.finish()
@dp.message_handler(state=Translate.fantaset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🍸 {int(message.text)*9000}so\'m💴',reply_markup=raqam)
    await state.finish()

@dp.message_handler(state=Translate.spriteset)
async def ssk(message,state:FSMContext):
    await message.answer(f'{message.text} 🍹 {int(message.text)*10000}so\'m💴',reply_markup=raqam)
    await state.finish()
@dp.message_handler(Text(equals=['Raqamimni ulashish']))
async def ddd(message):
    await message.answer('Telefon raqamingizni kiriting')
    await message.delete()
    await Translate.raqam.set()
@dp.message_handler(state=Translate.raqam)
async def ffg(message,state:FSMContext):
    if message.text[0:4]=='+998' and len(message.text)==13:
        await message.answer('Iltimos joylashuvingizni yuboring M-n:Urganch sh,Abulg`oziy Bahodirxon,110A uy',reply_markup=zakaz)
        await Translate.manzil.set()
    else:
        await message.answer('Iltimos raqamni to`g`ri kiriting(+998)')

@dp.message_handler(state=Translate.manzil)
async def ggg(message,state:FSMContext):
    if str(message.text[0:7])=='Urganch':
        await message.answer('Buyurtma qabul qilindi😃 Tez orada yetkazib beriladi🚴‍♂️')
        await message.answer('Murojaat uchun @deSeniorcoder',reply_markup=menu)
if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



