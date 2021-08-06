from say_me_something import say
from ask_me_something import ask
from .offical_data_system import *


class ONUR_Voice_Assistant:
   
   def __init__(self, data = OFFICAL_DATA):
      self.data = data


   def run(self):
      say("""I'm listening to you boss""")
      while True:
         expression = ask()
         if not expression == "shut down":
            self.engine(expression)
         else:
            exit()


   def engine(self, expression):
      know = False

      for situation in self.data:
         if not type(situation[0]) == list:
            if situation[0] in expression:
               know = True
               exec(situation[1])
         else:
            for sub_situation_trigger in situation[0]:
               if sub_situation_trigger in expression:
                  know = True
                  exec(situation[1])               
      
      if not know and not expression == "":
         say("""I don't now""")


ONUR = ONUR_Voice_Assistant()


if __name__ == "__main__":
   ONUR.run()
