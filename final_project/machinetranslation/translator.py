"""
This module has functions to translate strings between English and French.
"""

import os

from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
apiurl = os.environ['url']
version = os.environ['version']

auth = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=auth
)

lang_translator.set_service_url(apiurl)


class TranslationFailedException (Exception):
    """
    Exception raised when the translation API failed.

    Attributes:
        code -- the error code from the API
        message -- a corresponding message
    """

    def __init__(self, code, message):
        self.code = code
        self.message = f'Could not translate - api error [{code}] -> {message}'

        super().__init__(self.message)


def english_to_french(english_text: str) -> str:
    """
    This function takes an English str as input and
    returns the equivalent French as a string.
    """
    _check_input(english_text)

    if english_text == '':
        return ''

    return _translate(lang_translator, english_text, 'en', 'fr')


def french_to_english(french_text: str) -> str:
    """
    This function takes a French string as input and
    returns the equivalent English as a string.
    """
    _check_input(french_text)

    if french_text == '':
        return ''

    return _translate(lang_translator, french_text, 'fr', 'en')


def _translate(translator: LanguageTranslatorV3, text: str, source_lang_id: str, target_lang_id: str) -> str:
    translation = translator.translate(
        text=text,
        model_id=f'{source_lang_id}-{target_lang_id}'
    )

    translated_text = ''
    try:
        result = translation.get_result()
        translated_text = result.get('translations')[0].get('translation')
    except ApiException as ex:
        raise TranslationFailedException(ex.code, ex.message) from ex

    return translated_text


def _check_input(input_val: str):
    if input_val is None:
        raise Exception('Input value can not be None')

