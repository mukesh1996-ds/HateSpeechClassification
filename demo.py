from HateSpeech.logger import logging
from HateSpeech.exception import CustomeException
import sys

logging.info("Welcome to the NLP project!")

try:
    x = 1 / 0
except Exception as e:
    print(CustomeException(e, sys)) 
