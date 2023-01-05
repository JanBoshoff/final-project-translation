import os
import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french (english_text: str) -> str:
	"""
	This function takes an English str as input and returns the equivalent French as a string.
	"""
	_check_input(english_text)



	return ''

def french_to_english (french_text: str) -> str:
	"""
	This function takes a French string as input and returns the equivalent English as a string.
	"""
	_check_input(french_text)

	return ''

def _check_input (input_val: str):
	if input_val is None:
		raise Exception('Input value can not be None')
