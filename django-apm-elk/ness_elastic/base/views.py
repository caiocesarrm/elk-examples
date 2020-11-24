from time import time
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
import re
import requests
import traceback
import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Test(APIView):
    def get(self, request, *args, **kwargs):
        logger.debug("debug log")
        logger.info("info log")
        logger.warning("warning log")
        logger.error('error log')
        logger.critical("critical log")
        return Response({'sucess':True})
