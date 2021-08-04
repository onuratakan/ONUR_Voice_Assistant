from say_me_something import say
import speech_recognition as sr
from .offical_data_system import *


class ONUR_Voice_Assistant:
   
   def __init__(self):
      say("""I'm listening to you boss""")
      self.data = OFFICAL_DATA
      self.listen()

   @staticmethod
   def ask():
      r = sr.Recognizer()
      with sr.Microphone() as source:
         print("Say something")
         audio = r.listen(source)
      try:
         data = r.recognize_google(audio, language='en-en')
         data = data.lower()
         return data

      except sr.UnknownValueError:
            print("I can't understand")  


   def listen(self):
      while True:
         self.engine(self.ask())


   def engine(self, expression):
      print(expression)
      know = False

      for situation in self.data:
         if situation[0] in situation:
            know = True
            exec(situation[1])
      
      if not know:
         say("""I don't now""")


    