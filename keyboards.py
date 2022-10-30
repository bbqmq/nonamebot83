from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(types.InlineKeyboardButton(text='📢 Рассылка', callback_data='rass'))
apanel.add(types.InlineKeyboardButton(text='📊 Статистика', callback_data='stats'))
apanel.add(types.InlineKeyboardButton(text='💎 Восстановить роль "Владельца"', callback_data='owner'))
apanel.add(types.InlineKeyboardButton(text='👑 Скачать базу данных', callback_data='getdb'))

button2 = InlineKeyboardButton(text="🎲 Игры", callback_data="button2")
button4 = InlineKeyboardButton(text="💥 Развлекательное", callback_data="button4")
button1 = InlineKeyboardButton(text="💡 Основные", callback_data="button1")
button6 = InlineKeyboardButton(text="🏰 Кланы", callback_data="button6")
button11 = InlineKeyboardButton(text="⚒ Хочу такого же бота", callback_data="button11")
kk = InlineKeyboardMarkup()
kk.row(button1, button4)
kk.row(button2, button6)
kk.row(button11)

button_marry = types.InlineKeyboardMarkup(row_width=3)
button_marry.add(types.InlineKeyboardButton(text='❤️ Согласиться', callback_data='button_marry_y'), types.InlineKeyboardButton(text='💔 Отказаться', callback_data='button_marry_n'))
button_divorce = types.InlineKeyboardMarkup(row_width=3)
button_divorce.add(types.InlineKeyboardButton(text='💔 Согласиться', callback_data='button_divorce_y'), types.InlineKeyboardButton(text='❤ Отказаться', callback_data='button_divorce_n'))


button10 = InlineKeyboardButton(text="Добавить бота 😄", url="https://t.me/diamondgamebot?startgroup=true")
nk2 = InlineKeyboardMarkup().add(button10)


kit_b1 = InlineKeyboardButton(text="  💚ВИП  ", callback_data="kit_b1")
kit_b2 = InlineKeyboardButton(text="  💙ЛЕГЕНДА  ", callback_data="kit_b2")
kit_b3 = InlineKeyboardButton(text="  💜СПОНСОР  ", callback_data="kit_b3")
kit_b4 = InlineKeyboardButton(text="  🖤ВЛАСТЕЛИН  ", callback_data="kit_b4")
kit_kb = InlineKeyboardMarkup()
kit_kb = (kit_b1, kit_b2)
kit_kb = (kit_b3, kit_b4)

don1 = InlineKeyboardButton(text="   📝Привилегии   ", callback_data="don1")
don2 = InlineKeyboardButton(text="   🆘Администрация   ", callback_data="don2")
don = InlineKeyboardMarkup().add(don1, don2)

game1 = InlineKeyboardButton(text="🕹️Играть", callback_data="game1")
gm = InlineKeyboardMarkup().add(game1)

menub = InlineKeyboardButton(text="🔙 Назад", callback_data="menub")
nn = InlineKeyboardMarkup()
nn.row(menub)

me = InlineKeyboardButton(text="🔙 Назад", callback_data="me")
menk = InlineKeyboardMarkup()
menk.row(me)

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))

