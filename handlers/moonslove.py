import asyncio
import datetime
from io import BytesIO
from aiogram import types, html, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.router import Router 
from aiogram.utils.chat_action import ChatActionSender

from utils.states import Moon
from utils.keyboards import main_keyb, cool_keyb
from utils.download_images import download_all_images
from utils.moon_calc import combine_images, get_moon_phase_image, get_moon_image_url


router = Router()
router.my_chat_member.filter(F.chat.type == "private")
router.message.filter(F.chat.type == "private")

@router.startup()
async def moons_router_startapp():
    await download_all_images()


@router.message(F.text == "Moon")
async def start_moon(msg: types.Message, state: FSMContext):
    await msg.answer(
        text=html.italic(
            f"Yaxshi tug'ilgan kuningizni kiriting\n"
            f"Misol uchun: {html.code('13-11-2003')}"
        )
    )
    await state.set_state(Moon.day1)


@router.message(Moon.day1)
async def moon1(msg: types.Message, state: FSMContext):
    try:
        d1 = datetime.datetime.strptime(msg.text, "%d-%m-%Y")
        await state.set_data({
            'd1' : {
                "day": d1.day,
                "month": d1.month,
                "year": d1.year
            }
        })
        await msg.answer(
            text=f"Sizning tug'ilgan kuningiz {html.code(msg.text)}❤️\n"
                f"❤️ {html.italic('Juftingizning tug`ilgan kunini kiriting')}\n"
                f"Masalan: {html.code('01-01-2021')}"
        )
        await state.set_state(Moon.day2)
    except ValueError as e:
        await msg.answer("To'g'irlab kirita olmisanmi gapga tushin inson")


@router.message(Moon.day2)
async def moon2(msg: types.Message, state: FSMContext):
    try:
        d2 = datetime.datetime.strptime(msg.text, "%d-%m-%Y")
        data = await state.get_data()
        data['d2'] = {
            "day": d2.day,
            "month": d2.month,
            "year": d2.year
        }
        await state.set_data(data)
        
        await msg.answer(
            text=html.italic(
                f"Juftingizni  tug'ilgan kuni {html.code(msg.text)}\n"
                f"Cool tugmasini bosing va rasmlarni yuklab oling"
            ),
            reply_markup=cool_keyb
        )
        await state.set_state(Moon.cool )
    except ValueError as e:
        await msg.answer("To'g'irlab kirita olmisanmi gapga tushin inson")


@router.message(Moon.cool)
async def cool_state_handler(msg: types.Message, state: FSMContext):
    if msg.text == 'Cool':
        data = await state.get_data()
        d1 = data['d1']
        d2 = data['d2']
        bot = Bot.get_current()
        
        async with ChatActionSender.upload_photo(chat_id=msg.chat.id, bot=bot):
            await msg.answer(text="Yuklab olinmoqda...")
            img1, phase1 = get_moon_phase_image(d1['year'], d1['month'], d1['day'])
            img2, phase2 = get_moon_phase_image(d2['year'], d2['month'], d2['day'])
            day1 = f"{d1['day']}-{d1['month']}-{d1['year']}"
            await msg.answer_photo(
                photo=get_moon_image_url(img1),
                caption=html.italic(
                    f"Sizning tug'ilgan kuningiz {html.code(day1)}\n"
                    f"Oy fazasi: {round(phase1, 3)}"
                )
            )
            day2 = f"{d2['day']}-{d2['month']}-{d2['year']}"
            await msg.answer_photo(
                photo=get_moon_image_url(img2),
                caption=html.italic(
                    f"Juftingizning tug'ilgan kuni {html.code(day2)}\n"
                    f"Oy fazasi: {round(phase2, 3)}"
                )
            )
            m = await msg.answer("Birlashgan rasm tayyorlanmoqda...")
            await asyncio.sleep(1)
            try:
                img3 = combine_images(img1, img2, msg.from_user.id)
                await msg.answer_photo(
                    photo=types.BufferedInputFile(img3.read(), "image.jpg"),
                    caption=html.italic("Sizning va juftingizning tug'ilgan kunlari")
                )
            except Exception as e:
                print(e)
                await msg.answer("Nimadir xato ketti")
            await m.delete()
        
        await state.clear()
        await msg.answer(
            text=f"Yana davom ettirish uchun Moon tugmasini bosing",
            reply_markup=main_keyb
        )
        
    else:
        await msg.answer("To'g'irlab kirita olmisanmi gapga tushun inson")
    
