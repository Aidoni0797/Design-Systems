# Чтобы указать какое количество кнопок должно быть в каждом ряду - нужно передать в метод adjust целые числа (от 1 до 8),
# начиная с первого ряда. Причем данный метод будет игнорировать параметр width, если кнопки были добавлены в билдер методом row.
#
# Можно указывать количество кнопок не для всех рядов. Тогда последующие ряды будут заполняться кнопками по значению последнего
# переданного аргумента. То есть, если у нас 7 кнопок, а мы в adjust добавили 2 и 1, то в первом ряду будет 2 кнопки,
# а во втором и последующих по одной.

# В отличие от метода row() метод add() добавляет кнопки с нового ряда только если
# в предыдущем ряду для новых кнопок уже нет места. Причем, методу add все равно
# какой там у вас был параметр width до этого. Кнопки будут добавляться в ряд пока
# их там не станет 8 и только потом начнут заполнять новый ряд. Тоже до 8 штук.

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7216240691:AAGQus0Z0NqcbLy5USkpAFDkm3R5V1cTD68'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(8)
]
# Распаковываем список с кнопками методом add
kb_builder.add(*buttons_1)

# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах
kb_builder.adjust(1, 3)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая получается клавиатура',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )

if __name__ == '__main__':
    dp.run_polling(bot)