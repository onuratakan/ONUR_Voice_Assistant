from say_me_something import say
from ask_me_something import ask
import speech_recognition as sr
from .offical_data_system import *


class ONUR_Voice_Assistant:
   
   def __init__(self):
      say("""I'm listening to you boss""")
      self.data = OFFICAL_DATA
      self.run()


   def run(self):
      while True:
         expression = ask()
         if not expression == "exit":
            self.engine(expression)
         else:
            exit()


   def engine(self, expression):
      print(expression)
      know = False

      for situation in self.data:
         if situation[0] in situation:
            know = True
            exec(situation[1])
      
      if not know:
         say("""I don't now""")


    