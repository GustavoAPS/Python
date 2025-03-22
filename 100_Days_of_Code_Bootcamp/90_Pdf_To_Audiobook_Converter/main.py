from gtts import gTTS


with open('text_to_convert.txt', 'r') as file:
    data = file.read().replace('\n', '')

print(data)

language = 'en'

myobj = gTTS(text=data, lang=language, slow=False)
myobj.save("converted_audio.mp3")
