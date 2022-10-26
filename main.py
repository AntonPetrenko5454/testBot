

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram.utils import executor
from config import TOKEN
from testState import TestState

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard1=types.InlineKeyboardMarkup(row_width=1)
keyboard2=types.InlineKeyboardMarkup(row_width=1)
keyboard3=types.InlineKeyboardMarkup(row_width=1)
keyboard4=types.InlineKeyboardMarkup(row_width=1)
keyboard5=types.InlineKeyboardMarkup(row_width=1)

button1 = types.InlineKeyboardButton(text='Введите А', callback_data='button1_click')
button2 = types.InlineKeyboardButton(text='Введите B', callback_data='button2_click')
button3 = types.InlineKeyboardButton(text='Введите C', callback_data='button3_click')
button4 = types.InlineKeyboardButton(text='Введите D', callback_data='button4_click')

backTo1 = types.InlineKeyboardButton(text='Назад', callback_data='backTo1_click')
backTo2 = types.InlineKeyboardButton(text='Назад', callback_data='backTo2_click')
backTo3 = types.InlineKeyboardButton(text='Назад', callback_data='backTo3_click')
backTo4 = types.InlineKeyboardButton(text='Назад', callback_data='backTo4_click')


keyboard1.add(button1)
keyboard2.add(button2,backTo1)
keyboard3.add(button3,backTo2)
keyboard4.add(button4,backTo3)
keyboard5.add(backTo4)

@dp.callback_query_handler(text='button1_click',state=TestState.A)
async def button1Click(call: types.CallbackQuery,state: FSMContext):
    await state.update_data(A=call.message.text)
    await call.message.edit_text('B',reply_markup=keyboard2)

    await TestState.next()
    await call.answer()

@dp.callback_query_handler(text='button2_click',state=TestState.B)
async def button2Click(call: types.CallbackQuery,state: FSMContext):
    await state.update_data(B=call.message.text)
    await call.message.edit_text('C',reply_markup=keyboard3)
    await TestState.next()
    await call.answer()

@dp.callback_query_handler(text='button3_click',state=TestState.C)
async def button3Click(call: types.CallbackQuery,state: FSMContext):
    await state.update_data(C=call.message.text)
    await call.message.edit_text('D',reply_markup=keyboard4)
    await TestState.next()
    await call.answer()

@dp.callback_query_handler(text='button4_click',state=TestState.D)
async def button4Click(call: types.CallbackQuery,state: FSMContext):
    await state.update_data(D=call.message.text)
    await call.message.edit_text('Финишь')
    await TestState.next()
    await call.answer()

@dp.callback_query_handler(text='backTo1_click')
async def backTo1Click(call: types.CallbackQuery):
    await call.message.edit_text('A',reply_markup=keyboard1)
    await call.answer()

@dp.callback_query_handler(text='backTo2_click')
async def backTo2Click(call: types.CallbackQuery):
    await call.message.edit_text('B',reply_markup=keyboard2)
    await call.answer()

@dp.callback_query_handler(text='backTo3_click')
async def backTo3Click(call: types.CallbackQuery):
    await call.message.edit_text('C',reply_markup=keyboard3)
    await call.answer()

@dp.callback_query_handler(text='backTo4_click')
async def backTo4Click(call: types.CallbackQuery):
    await call.message.edit_text('D',reply_markup=keyboard4)
    await call.answer()

@dp.message_handler(commands=['start'])
async def startCommands(message: types.Message):

    await message.answer('A',reply_markup=keyboard1)
    await TestState.A.set()

if __name__ == '__main__':
    executor.start_polling(dp)


