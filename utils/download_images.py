import os
import logging
import aiofiles
from aiohttp import ClientSession
from utils.moon_calc import MOON_PHOTOS


def check_files():
    return all(os.path.exists("images/"+photo+".jpg") for photo in MOON_PHOTOS.keys())


async def download_all_images():
    if check_files():
        logging.debug("Images downloaded!")
        return
    # check images folder and if not exists create folder
    if not os.path.exists('images/'):
        os.mkdir('images')
    async with ClientSession() as session:
        for photo, url in MOON_PHOTOS.items():
            async with session.get(url) as resp:
                async with aiofiles.open("images/"+photo+".jpg", "wb") as f:
                    await f.write(await resp.read())
                logging.info("Download %s from URL -> %s" % (photo, url))

