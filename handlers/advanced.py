from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart

from utils.keyboards import main_keyb


router = Router()

@router.message(CommandStart())
async def cmd_start(msg: types.Message):
    await msg.answer(
        text=f"Salom {msg.from_user.mention_html()}.\n"
            f"Boshlash uchun Moon tugamasini bosing",
        reply_markup=main_keyb
    )


@router.message(F.text == "Help Me")
@router.message(Command('help'))
async def cmd_help(msg: types.Message):
    await msg.answer(
        text="Yordam uchun @coderjon_a",
        reply_markup=main_keyb
    )


@router.message()
async def unknown(msg: types.Message):
    await msg.answer(
        text=f"Boshlash uchun Moon tugamasini bosing",
        reply_markup=main_keyb
    )
