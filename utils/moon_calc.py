import os
import ephem
import datetime
from PIL import Image
from io import BytesIO

MOON_PHOTOS = {
    'new_moon': "https://moon.nasa.gov/internal_resources/366/",
    'waxing_crescent': "https://moon.nasa.gov/internal_resources/368/",
    'first_quarter': "https://moon.nasa.gov/internal_resources/367/",
    "waxing_gibbous": "https://moon.nasa.gov/internal_resources/365/",
    "full_moon": "https://moon.nasa.gov/internal_resources/364/",
    "waning_gibbous": "https://moon.nasa.gov/internal_resources/363/",
    "last_quarter": "https://moon.nasa.gov/internal_resources/362/",
    "waning_crescent": "https://moon.nasa.gov/internal_resources/361/" 
}

def combine_images(img1, img2, chat_id):
    # Open the first image
    image1 = Image.open(f'images/{img1}.jpg')

    # Open the second image
    image2 = Image.open(f'images/{img2}.jpg')

    # Combine the two images side by side
    result_image = Image.new("RGB", (image1.width + image2.width, max(image1.height, image2.height)))
    result_image.paste(image1, (0, 0))
    result_image.paste(image2, (image1.width, 0))

    # Save the combined image
    image_path = f"./images/{chat_id}.jpg"
    result_image.save(image_path, format="JPEG")
    with open(image_path, "rb") as f:
        io = BytesIO(f.read())
    os.remove(image_path)
    return io
    

def moon_phase(year, month, day):
    # Set the observer's location to Uzbekistan
    observer = ephem.Observer()
    observer.lat = '41.3'
    observer.lon = '69.3'
    observer.elevation = 0

    # Calculate the phase of the Moon
    moon = ephem.Moon()
    observer.date = datetime.datetime(year, month, day)
    moon.compute(observer)
    phase = moon.moon_phase
    return phase

def get_moon_phase_image(year, month, day):
    phase = moon_phase(year, month, day)

    # Map the phase to the corresponding moon phase description
    if phase < 0.06:
        description = "new_moon"
    elif phase < 0.25:
        description = "waxing_crescent"
    elif phase < 0.26:
        description = "first_quarter"
    elif phase < 0.75:
        description = "waxing_gibbous"
    elif phase < 0.76:
        description = "full_moon"
    elif phase < 0.93:
        description = "waning_gibbous"
    elif phase < 0.94:
        description = "last_quarter"
    else:
        description = "waning_crescent"

    return description, phase


def get_moon_image_url(description):
    # Use the description to index the `moon_photos` dictionary
    image_url = MOON_PHOTOS[description]
    return image_url
