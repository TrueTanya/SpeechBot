import pyttsx3
engine = pyttsx3.init()
engine.say('У Вас будет возможность мониторить передвижения ребенка через приложения для. Местонахождение будет отображаться в виде точек на карте')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog. ')
   engine.say('У Вас будет возможность мониторить передвижения ребенка через приложения для.')
engine.runAndWait()