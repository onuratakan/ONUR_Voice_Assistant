#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from flask import jsonify
from waitress import serve
from ONUR_Data.ONUR_offical_data_system import OFFICAL_DATA


class ONUR_Voice_Assistant:
   
   def __init__(self, data = OFFICAL_DATA):
      self.data = data

  
   def run_api(self, host = "0.0.0.0"):

      self.api = flask.Flask(__name__)
      @self.api.route("/<expression>", methods=["GET"])
      def onur_api(expression):
         return jsonify(self.engine(expression))       
      serve(self.api, host=host, port=2005)

   def engine(self, expression):

      for situation in self.data:
         for sub_situation_trigger in situation[0]:
            if sub_situation_trigger in expression:
               return situation[1](expression)
      
      return """I don't now"""


ONUR = ONUR_Voice_Assistant()


if __name__ == "__main__":
   ONUR.run_api()
