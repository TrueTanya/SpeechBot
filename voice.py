import pyttsx3
import uuid
import subprocess

engine = pyttsx3.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")

def text_to_file_ogg(text):
   tmp_file_mp3 = uuid.uuid4().hex
   out_file_ogg = f'data/{tmp_file_mp3}.ogg'
   engine.save_to_file(text, out_file_ogg)
   #engine.save_to_file(text, f'data/{tmp_file_mp3}.mp3')
   engine.runAndWait()
   #convert mp3 to ogg
   #ffmpeg -i test.mp3 -c:a Libopus test_out.ogg
   #subprocess.run(["ffmpeg", '-i', tmp_file_mp3, '-acodec', 'libopus', out_file_ogg, '-y'])
   return out_file_ogg
   #return f'data/{tmp_file_mp3}.mp3'

def text_to_file_mp3(text):
   tmp_file_mp3 = uuid.uuid4().hex
   engine.save_to_file(text, f'data/{tmp_file_mp3}.mp3')
   engine.runAndWait()
   return f'data/{tmp_file_mp3}.mp3'

# text_to_file("Если вдруг ребенок покидает такую территорию, на смартфон родителей приходит уведомление")
# text_to_file("чтобы вернуть сегодняшнюю дату в формате")
