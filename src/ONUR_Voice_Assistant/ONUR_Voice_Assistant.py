#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from flask import jsonify
from waitress import serve
from .offical_data_system import *


class ONUR_Voice_Assistant:
   
   def __init__(self, data = OFFICAL_DATA):
      self.data = data

      self.api = flask.Flask(__name__)
      @self.api.route("/<expression>", methods=["GET"])
      def onur_api(expression):
         return jsonify(self.engine(expression))
      @self.api.route("/<expression>/<parameter>", methods=["GET"])
      def onur_api_parameter(expression, parameter):
         return jsonify(self.engine(expression, parameter))         

   def run_api(self, host = "0.0.0.0"):
      serve(self.api, host=host, port=2005)

   def engine(self, expression, parameter=None):
      know = False

      for situation in self.data:
         for sub_situation_trigger in situation[0]:
            if sub_situation_trigger in expression:
               know = True
               if parameter is None:
                  return situation[1]()
               else:
                  return situation[1](parameter)
      
      if not know and not expression == "":
         return """I don't now"""


ONUR = ONUR_Voice_Assistant()


if __name__ == "__main__":
   ONUR.run_api()
