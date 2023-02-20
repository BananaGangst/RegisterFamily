from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user,add_user_name,add_user_numb,add_user_klass


bot = Bot("5994926717:AAFbk-wRNv3C75Xw69ose1PxC5oxJmGBmAc")
dp = Dispatcher(bot,storage=MemoryStorage())

class user_reg(StatesGroup):
	name = State()
	numb = State()
	klass = State()

urlne = InlineKeyboardMarkup(row_width=1)
urlButtom = InlineKeyboardButton(text="➡ Перейти в ГРУППУ ⬅💲", url='https://prizes.gamee.com/game-bot/neonblast2-8b4d803a20090f438b6ba0fbcceb630d0eb8e76b#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D1kjkUtETi7uFhqc1JIvWkfXC_xOVj6rt_GQC30NnhTMqCcUVP_y7c95ewlA7xven')
urlne.add(urlButtom)

print("Бот запущен!")

@dp.message_handler(state=user_reg.name)
async def add_name_(message:types.Message,state=FSMContext):
	chat_id = message.chat.id
	await state.finish()
	add_user_name(message)
	await bot.send_message(chat_id, 'Введите свой номер :\nВ Формате - "+79123456789"')
	await user_reg.numb.set()

@dp.message_handler(state=user_reg.numb)
async def add_numb_(message:types.Message,state=FSMContext):
	chat_id = message.chat.id
	await state.finish()
	add_user_numb(message)
	await bot.send_message(chat_id, 'Введите свой Класс :\nВ Формате - "Класс" + "Цифра"\nПример - "7 4"')
	await user_reg.klass.set()

@dp.message_handler(state=user_reg.klass)
async def add_klass_(message:types.Message,state=FSMContext):
	chat_id = message.chat.id
	await state.finish()
	add_user_klass(message)
	await bot.send_message(chat_id, "Регистрация Прошла Успешна ❗")
	await bot.send_message(chat_id, "t.me/+bYzdC5aGOm9kOTVi")


@dp.message_handler(commands=['reg'])#???commands=['start']
async def start_message(message:types.Message,state=FSMContext):
	chat_id = message.chat.id
	add_user(message)
	await bot.send_message(chat_id, f"Привет {message.chat.first_name} !\n"									f"Введите своё имя :")
	await user_reg.name.set()

@dp.message_handler(commands=['start'])
async def echo_send(message : types.Message):
	await bot.send_message(message.chat.id, "💢💢💢💢💢 ПРЕДУПРЕЖДЕНИЕ 💢💢💢💢💢\n\nПеред тем как пройти регистрацию, вам стоит принять некоторые условия:\nМы собираем данные об участнике группы, но не распространяем их за пределы группы❗\nВ случаи ложных информаций вы будете изнаны из неё❗\nКак только вы прочитали условия\n🔽🔽🔽🔻🔻🔽🔽🔽\n🔰Напишите /reg и вы НАЧНЁТЕ РЕГИСТРАЦИЮ🔰")


if __name__ == '__main__':
	executor.start_polling(dp)	