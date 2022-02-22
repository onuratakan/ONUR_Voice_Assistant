#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from waitress import serve
from .offical_data_system import *


class ONUR_Voice_Assistant:
   
   def __init__(self, data = OFFICAL_DATA):
      self.data = data

   def run(self, host = "0.0.0.0"):
      app = flask.Flask(__name__)
      @app.route("/<expression>", methods=["GET"])
      def onur_api(expression):
         return self.engine(expression)
      serve(app, host=host, port=2005)

   def engine(self, expression):
      know = False

      for situation in self.data:
         for sub_situation_trigger in situation[0]:
            if sub_situation_trigger in expression:
               know = True
               return situation[1]()          
      
      if not know and not expression == "":
         return """I don't now"""


ONUR = ONUR_Voice_Assistant()


if __name__ == "__main__":
   ONUR.run()
