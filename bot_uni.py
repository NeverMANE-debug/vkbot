#!/usr/bin/env python3.8
import sqlite3

import random
import config_uni
from vkbottle import *
from vkbottle.bot import *
from vkbottle.dispatch.rules.bot import VBMLRule
from vkbottle_types import BaseStateGroup

bot = Bot(config_uni.TOKEN)


# -------------------------KEYBOARDS------------------------------
start_kb = Keyboard(one_time=False, inline=False)
start_kb.add(Text("Главное меню"), color=KeyboardButtonColor.PRIMARY)

menu_kb = Keyboard(one_time=False, inline=False)
menu_kb.add(Text("Посмотреть мои успехи"), color=KeyboardButtonColor.PRIMARY)
menu_kb.row()
menu_kb.add(Text("Посмотреть все задания"), color=KeyboardButtonColor.PRIMARY)
menu_kb.row()
menu_kb.add(Text("Кнопка"), color=KeyboardButtonColor.POSITIVE)

r_cases1 = Keyboard(one_time=False, inline=False)
r_cases1.add(Text("Философия"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Языки программирования"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Иностранные языки"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Политология и социология"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Мат. логика и теория алгоритмов"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Основы инф. безопасности"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Русский язык"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Физика"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Следующая страница"), color=KeyboardButtonColor.PRIMARY)
r_cases1.row()
r_cases1.add(Text("Вернуться в главное меню"), color=KeyboardButtonColor.NEGATIVE)

r_cases2 = Keyboard(one_time=False, inline=False)
r_cases2.add(Text("Математический анализ"), color=KeyboardButtonColor.PRIMARY)
r_cases2.row()
r_cases2.add(Text("Экология"), color=KeyboardButtonColor.PRIMARY)
r_cases2.row()
r_cases2.add(Text("Практика"), color=KeyboardButtonColor.PRIMARY)
r_cases2.row()
r_cases2.add(Text("Предыдущая страница"), color=KeyboardButtonColor.PRIMARY)
r_cases2.row()
r_cases2.add(Text("Вернуться в главное меню"), color=KeyboardButtonColor.NEGATIVE)

YN_kb = Keyboard(one_time=False, inline=False)
YN_kb.add(Text("Да, сделал"), color=KeyboardButtonColor.POSITIVE)
YN_kb.add(Text("Нет, не сделал"), color=KeyboardButtonColor.NEGATIVE)

CP_kb = Keyboard(one_time=False, inline=False)
CP_kb.add(Text("Нынешнее"), color=KeyboardButtonColor.PRIMARY)
CP_kb.add(Text("Предыдущее"), color=KeyboardButtonColor.PRIMARY)

r_information = Keyboard(one_time=False, inline=False)
r_information.add(Text("Редактировать выполненные"), color=KeyboardButtonColor.PRIMARY)
r_information.row()
r_information.add(Text("Вернуться в главное меню"), color=KeyboardButtonColor.NEGATIVE)


#-----------------------------------------MESSAGES----------------------------
def changes_completed(m: Message):
    return m.answer(message=f"Изменения внесены!{random.choice(config_uni.love_emoji)}\nВ главном меню ты можешь", keyboard = menu_kb.get_json())


def did_it(m: Message):
    return m.answer(message=f"Сделал? {random.choice(config_uni.confusion_emoji)}", keyboard = YN_kb.get_json())
# -----------------------------STATES------------------------------
class Branch(BaseStateGroup):

    button = -1
    menu = 0
    succeed = 1
    succeed_1 = 90
    refresh_information = 2
    r_cases1 = 3
    r_cases2 = 4

    CP_PHIL = 27
    CP_PL = 28
    CP_FL = 29
    CP_PaS = 30
    CP_MLaAT = 31
    CP_BIS = 32
    CP_RL = 33
    CP_PHYS = 34
    CP_MA = 35
    CP_ECO = 36
    CP_PRAC = 37

    r_PHIL_1 = 5
    r_PL_1 = 6
    r_FL_1 = 7
    r_PaS_1 = 8
    r_MLaAT_1 = 9
    r_BIS_1 = 10
    r_RL_1 = 11
    r_PHYS_1 = 12
    r_MA_1 = 13
    r_ECO_1 = 14
    r_PRAC_1 = 15
    r_PHIL_2 = 16
    r_PL_2 = 17
    r_FL_2 = 18
    r_PaS_2 = 19
    r_MLaAT_2 = 20
    r_BIS_2 = 21
    r_RL_2 = 22
    r_PHYS_2 = 23
    r_MA_2 = 24
    r_ECO_2 = 25
    r_PRAC_2 = 26

    chex = 73

    jabbah_1 = 38
    jabbah_2 = 50

    jb_PHIL = 39
    jb_PL = 40
    jb_FL = 41
    jb_PaS = 41
    jb_MLaAT = 43
    jb_BIS = 44
    jb_RL = 45
    jb_PHYS = 46
    jb_MA = 47
    jb_ECO = 48
    jb_PRAC = 49

    jb_PHIL_1 = 51
    jb_PL_1 = 52
    jb_FL_1 = 53
    jb_PaS_1 = 54
    jb_MLaAT_1 = 55
    jb_BIS_1 = 56
    jb_RL_1 = 57
    jb_PHYS_1 = 58
    jb_MA_1 = 59
    jb_ECO_1 = 60
    jb_PRAC_1 = 61
    jb_PHIL_2 = 62
    jb_PL_2 = 63
    jb_FL_2 = 64
    jb_PaS_2 = 65
    jb_MLaAT_2 = 66
    jb_BIS_2 = 67
    jb_RL_2 = 68
    jb_PHYS_2 = 69
    jb_MA_2 = 70
    jb_ECO_2 = 71
    jb_PRAC_2 = 72


# ------------------------------DATABASE------------------------------
conn = sqlite3.connect('data_uni.db')
cursor = conn.cursor()


# -------------------------------START------------------------------
@bot.on.message(text=['Начать', 'Start'], state=None)
async def reassign(m: Message):
    cursor.execute(f"insert or replace into PHIL values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into PL values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into FL values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into PaS values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into MLaAT values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into BIS values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into RL values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into PHYS values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into MA values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into ECO values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    cursor.execute(f"insert or replace into PRAC values('{m.from_id}', '&#10060;', '&#10060;')")
    conn.commit()
    await m.answer(message="Привет! В следующем бранче тебе предложат", keyboard=start_kb.get_json())
    await bot.state_dispenser.set(m.peer_id, Branch.menu)


# ------------------------------MENU------------------------------
@bot.on.message(text=['123'], state=None)
async def menu(m: Message):
    await bot.state_dispenser.set(m.peer_id, Branch.menu)


@bot.on.message(text=["123", 'Главное меню', 'Вернуться в главное меню', 'Отмена'], state=[Branch.menu, Branch.chex, Branch.succeed, Branch.button])
async def menu(m: Message):
    await bot.state_dispenser.set(m.from_id, Branch.menu)
    await m.answer(message="В главном меню ты можешь", keyboard=menu_kb.get_json())


@bot.on.message(text=['Кнопка'], state=Branch.menu)
async def kakaru(m: Message):
    await bot.state_dispenser.set(m.from_id, Branch.button)
    await m.answer(message="Упс, тут ничего:( Возвращайся", keyboard=start_kb.get_json())


# --------------------------SHOW_SUCCEEDS------------------------------
@bot.on.message(text=['Посмотреть мои успехи'], state=Branch.menu)
async def die_handler(m: Message):
    cursor.execute(f"SELECT PHIL1, PHIL2 from PHIL WHERE vk_id = {m.from_id}")
    PHIL = list(cursor.fetchone())
    cursor.execute(f"SELECT PL1, PL2 from PL WHERE vk_id = {m.from_id}")
    PL = list(cursor.fetchone())
    cursor.execute(f"SELECT FL1, FL2 from FL WHERE vk_id = {m.from_id}")
    FL = list(cursor.fetchone())
    cursor.execute(f"SELECT PaS1, PaS2 from PaS WHERE vk_id = {m.from_id}")
    PaS = list(cursor.fetchone())
    cursor.execute(f"SELECT MLaAT1, MLaAT2 from MLaAT WHERE vk_id = {m.from_id}")
    MLaAT = list(cursor.fetchone())
    cursor.execute(f"SELECT BIS1, BIS2 from BIS WHERE vk_id = {m.from_id}")
    BIS = list(cursor.fetchone())
    cursor.execute(f"SELECT RL1, RL2 from RL WHERE vk_id = {m.from_id}")
    RL = list(cursor.fetchone())
    cursor.execute(f"SELECT PHYS1, PHYS2 from PHYS WHERE vk_id = {m.from_id}")
    PHYS = list(cursor.fetchone())
    cursor.execute(f"SELECT MA1, MA2 from MA WHERE vk_id = {m.from_id}")
    MA = list(cursor.fetchone())
    cursor.execute(f"SELECT ECO1, ECO2 from ECO WHERE vk_id = {m.from_id}")
    ECO = list(cursor.fetchone())
    cursor.execute(f"SELECT PRAC1, PRAC2 from PRAC WHERE vk_id = {m.from_id}")
    PRAC = list(cursor.fetchone())
    await bot.state_dispenser.set(m.peer_id, Branch.succeed_1)
    await m.answer(f'Вот твоя нынешняя ситуация.\n\n'
                   f'Философия: \nНынешнее -> {PHIL[0]}\nПредыдущее -> {PHIL[1]}\n\n'
                   f'Языки программирования: \nНынешнее -> {PL[0]}\nПредыдущее -> {PL[1]}\n\n'
                   f'Иностранные языки: \nНынешнее -> {FL[0]}\nПредыдущее -> {FL[1]}\n\n'
                   f'Политология и социология: \nНынешнее -> {PaS[0]}\nПредыдущее -> {PaS[1]}\n\n'
                   f'Мат. логика и теория алгоритмов: \nНынешнее -> {MLaAT[0]}\nПредыдущее -> {MLaAT[1]}\n\n'
                   f'Основы инф. безопасности: \nНынешнее -> {BIS[0]}\nПредыдущее -> {BIS[1]}\n\n'
                   f'Русский язык: \nНынешнее -> {RL[0]}\nПредыдущее -> {RL[1]}\n\n'
                   f'Физика: \nНынешнее -> {PHYS[0]}\nПредыдущее -> {PHYS[1]}\n\n'
                   f'Математический анализ: \nНынешнее -> {MA[0]}\nПредыдущее -> {MA[1]}\n\n'
                   f'Экология: \nНынешнее -> {ECO[0]}\nПредыдущее -> {ECO[1]}\n\n'
                   f'Практика: \nНынешнее -> {PRAC[0]}\nПредыдущее -> {PRAC[1]}\n\n', keyboard=r_information.get_json())


@bot.on.message(VBMLRule("<text>"), state=[Branch.succeed_1, Branch.chex])
async def asd(m: Message, text):
    if text == "Редактировать выполненные":
        await m.answer("Выбери, что хочешь изменить:", keyboard=r_cases1.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.r_cases1)
    elif text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.r_cases1)
async def asd(m: Message, text):
    if text == 'Философия':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_PHIL)
    elif text == 'Языки программирования':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_PL)
    elif text == 'Иностранные языки':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_FL)
    elif text == 'Политология и социология':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_PaS)
    elif text == 'Мат. логика и теория алгоритмов':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_MLaAT)
    elif text == 'Основы инф. безопасности':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_BIS)
    elif text == 'Русский язык':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_RL)
    elif text == 'Физика':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_PHYS)
    elif text == "Следующая страница":
        await m.answer("Выбери, что хочешь изменить:", keyboard=r_cases2.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.r_cases2)
    elif text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.r_cases2)
async def asd(m: Message, text):
    if text == 'Математический Анализ':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_MA)
    elif text == 'Экология':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_ECO)
    elif text == 'Практика':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.CP_PRAC)
    elif text == "Предыдущая страница":
        await m.answer("Выбери, что хочешь изменить:", keyboard=r_cases1.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.r_cases1)
    elif text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())


# ----------------------------------CP--------------------------------
@bot.on.message(VBMLRule("<text>"), state=Branch.CP_PHIL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PHIL_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PHIL_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_PL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PL_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PL_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_FL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_FL_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_FL_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_PaS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PaS_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PaS_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_MLaAT)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_MLaAT_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_MLaAT_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_BIS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_BIS_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_BIS_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_RL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_RL_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_RL_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_PHYS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PHYS_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PHYS_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_MA)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_MA_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_MA_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_ECO)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_ECO_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_ECO_2)
        await did_it(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.CP_PRAC)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PRAC_1)
        await did_it(m)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.r_PRAC_2)
        await did_it(m)


# -------------------------------R_CASES------------------------------
@bot.on.message(VBMLRule("<text>"), state=Branch.r_PHIL_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PHIL SET PHIL1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PHIL SET PHIL1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PHIL_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PHIL SET PHIL2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PHIL SET PHIL2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PL_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PL SET PL1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PL SET PL1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PL_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PL SET PL2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PL SET PL2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_FL_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE FL SET FL1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE FL SET FL1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_FL_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE FL SET FL2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE FL SET FL2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PaS_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PaS SET PaS1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PaS SET PaS1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PaS_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PaS SET PaS2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PaS SET PaS2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_MLaAT_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE MLaAT SET MLaAT1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE MLaAT SET MLaAT1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_MLaAT_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE MLaAT SET MLaAT2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE MLaAT SET MLaAT2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_BIS_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE BIS SET BIS1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE BIS SET BIS1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_BIS_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE BIS SET BIS2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE BIS SET BIS2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_RL_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE RL SET RL1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE RL SET RL1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_RL_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE RL SET RL2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE RL SET RL2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PHYS_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PHYS SET PHYS1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PHYS SET PHYS1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PHYS_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PHYS SET PHYS2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PHYS SET PHYS2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_MA_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE MA SET MA1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE MA SET MA1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_MA_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE MA SET MA2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE MA SET MA2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_ECO_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE ECO SET ECO1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE ECO SET ECO1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_ECO_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE ECO SET ECO2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE ECO SET ECO2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PRAC_1)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PRAC SET PRAC1 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PRAC SET PRAC1 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


@bot.on.message(VBMLRule("<text>"), state=Branch.r_PRAC_2)
async def asd(m: Message, text):
    if text == 'Да, сделал':
        text_1 = str('&#10004;')
        cursor.execute(f"UPDATE PRAC SET PRAC2 = '{text_1}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)
    elif text == 'Нет, не сделал':
        text_2 = str('&#10060;')
        cursor.execute(f"UPDATE PRAC SET PRAC2 = '{text_2}' WHERE vk_id = {m.from_id}")
        conn.commit()
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await changes_completed(m)


# ----------------------------------------------CHEX------------------------------------------


@bot.on.message(text=["Посмотреть все задания"], state=Branch.menu)
async def search2(m: Message):
    cursor.execute(f"SELECT PHIL1, PHIL2, PL1, PL2, FL1, FL2, PaS1, PaS2, MLaAT1, MLaAT2, BIS1, BIS2, RL1, RL2, PHYS1, PHYS2, MA1, MA2, ECO1, ECO2, PRAC1, PRAC2 from EX WHERE vk_id = {597776932}")
    chex = list(cursor.fetchone())
    await bot.state_dispenser.set(m.from_id, Branch.chex)
    await m.answer(f'Философия: \nНынешнее -> {chex[0]}\nПредыдущее -> {chex[1]}\n\n'
                   f'Языки программирования: \nНынешнее -> {chex[2]}\nПредыдущее -> {chex[3]}\n\n'
                   f'Иностранные языки: \nНынешнее -> {chex[4]}\nПредыдущее -> {chex[5]}\n\n'
                   f'Политология и социология: \nНынешнее -> {chex[6]}\nПредыдущее -> {chex[7]}\n\n'
                   f'Мат. логика и теория алгоритмов: \nНынешнее -> {chex[8]}\nПредыдущее -> {chex[9]}\n\n'
                   f'Основы инф. безопасности: \nНынешнее -> {chex[10]}\nПредыдущее -> {chex[11]}\n\n'
                   f'Русский язык: \nНынешнее -> {chex[12]}\nПредыдущее -> {chex[13]}\n\n'
                   f'Физика: \nНынешнее -> {chex[14]}\nПредыдущее -> {chex[15]}\n\n'
                   f'Математический анализ: \nНынешнее -> {chex[16]}\nПредыдущее -> {chex[17]}\n\n'
                   f'Экология: \nНынешнее -> {chex[18]}\nПредыдущее -> {chex[19]}\n\n'
                   f'Практика: \nНынешнее -> {chex[20]}\nПредыдущее -> {chex[21]}\n\n', keyboard=r_information.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.chex)
async def search2(m: Message, text):
    if text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())
    elif text == "Редактировать выполненные":
        await m.answer("Выбери, что хочешь изменить:", keyboard=r_cases1.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.r_cases1)
# ----------------------------------------JABBAH------------------------------


@bot.on.message(text=['Жабыч'], state=Branch.menu)
async def die_handler(m: Message):
#cursor.execute(f"insert or replace into EX values('{597776932}', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было', 'Задания ещё не было')")
#conn.commit()
    await m.answer("Ну, выбери чё хотел поправить...", keyboard=r_cases1.get_json())
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)


@bot.on.message(VBMLRule("<text>"), state=Branch.jabbah_1)
async def asd(m: Message, text):
    if text == 'Философия':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHIL)
    elif text == 'Языки программирования':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PL)
    elif text == 'Иностранные языки':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_FL)
    elif text == 'Политология и социология':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PaS)
    elif text == 'Мат. логика и теория алгоритмов':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MLaAT)
    elif text == 'Основы инф. безопасности':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_BIS)
    elif text == 'Русский язык':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_RL)
    elif text == 'Физика':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHYS)
    elif text == "Следующая страница":
        await m.answer("Ну, выбери чё хотел поправить...", keyboard=r_cases2.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    elif text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jabbah_2)
async def asd(m: Message, text):
    if text == 'Математический Анализ':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MA)
    elif text == 'Экология':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_ECO)
    elif text == 'Практика':
        await m.answer("Какое?", keyboard=CP_kb.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PRAC)
    elif text == "Предыдущая страница":
        await m.answer("Ну, выбери чё хотел поправить...", keyboard=r_cases1.get_json())
        await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    elif text == 'Вернуться в главное меню':
        await bot.state_dispenser.set(m.peer_id, Branch.menu)
        await m.answer(message="Изменения отменены!\nВ главном меню ты можешь", keyboard=menu_kb.get_json())


# ---------------------------------JB-----------------------------------
@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHIL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHIL_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHIL_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PL_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PL_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_FL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_FL_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_FL_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PaS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PaS_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PaS_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MLaAT)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MLaAT_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MLaAT_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_BIS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_BIS_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_BIS_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_RL)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_RL_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_RL_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHYS)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHYS_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PHYS_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MA)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MA_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_MA_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_ECO)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_ECO_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_ECO_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PRAC)
async def asd(m: Message, text):
    if text == 'Нынешнее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PRAC_1)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)
    elif text == 'Предыдущее':
        await bot.state_dispenser.set(m.peer_id, Branch.jb_PRAC_2)
        await m.answer(message="Пиши задание, братишка", keyboard=EMPTY_KEYBOARD)


# --------------------------------------------JB_CASES--------------------------------------------


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHIL_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT PHIL1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET PHIL2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET PHIL1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHIL_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET PHIL2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PL_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT PL1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET PL2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET PL1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PL_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET PL2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_FL_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT FL1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET FL2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET FL1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_FL_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET FL2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PaS_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT PaS1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET PaS2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET PaS1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PaS_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET PaS2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MLaAT_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT MLaAT1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET MLaAT2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET MLaAT1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MLaAT_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET MLaAT2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_BIS_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT BIS1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET BIS2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET BIS1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_BIS_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET BIS2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_RL_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT RL1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET RL2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET RL1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_RL_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET RL2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHYS_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT PHYS1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET PHYS2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET PHYS1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PHYS_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET PHYS2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_1)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases1.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MA_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT MA1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET MA2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET MA1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_MA_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET MA2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_ECO_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT ECO1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET ECO2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET ECO1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_ECO_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET ECO2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PRAC_1)
async def asd(m: Message, text):
    cursor.execute(f"SELECT PRAC1 from EX WHERE vk_id = {597776932}")
    ex_data = cursor.fetchone()[0]
    cursor.execute(f"UPDATE EX SET PRAC2 = '{ex_data}' WHERE vk_id = {597776932}")
    conn.commit()
    cursor.execute(f"UPDATE EX SET PRAC1 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


@bot.on.message(VBMLRule("<text>"), state=Branch.jb_PRAC_2)
async def asd(m: Message, text):
    cursor.execute(f"UPDATE EX SET PRAC2 = '{text}' WHERE vk_id = {597776932}")
    conn.commit()
    await bot.state_dispenser.set(m.peer_id, Branch.jabbah_2)
    await m.answer(message="Изменения внесены!\nМожешь ещё чё-нить добавить", keyboard=r_cases2.get_json())


bot.run_forever()
