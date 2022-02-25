import cv2
import pytesseract
import boto3
import requests
import io 
from PIL import Image

def image_text(img, langs):
    response = requests.get(img)

    # temp_image = cv2.imread(img)

    img = Image.open(io.BytesIO(response.content))

    custom_config = f'-l {langs}'

    text = pytesseract.image_to_string(img, config=custom_config)

    return text

def translate(text, langs):
    client = boto3.client('translate')

    # Takes user input from terminal
    # text = input("Type something and I will have it translated for you. \n >")
    # imgtxt = main()
    if langs == "eng":
        langs = 'en'
    if langs == "jpn":
        langs = 'ja'
    if langs == "kor":
        langs = 'ko'

    # Sample of translate_text method
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=f'{langs}',
        TargetLanguageCode='en'
    )

    sourcelanguage = response.get('SourceLanguageCode')
    targetlanguage = response.get('TargetLanguageCode')
    translation = response.get('TranslatedText')

    dict={"sourcelanguage":sourcelanguage, "targetlanguage":targetlanguage, "translation": translation }
    return dict

