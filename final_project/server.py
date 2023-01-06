"""
This is file defines to translator API routes.
"""

from flask import Flask, render_template, request

from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french():
    """
    This route takes a param for input text and returns a translated string:
    textToTranslate: str
    """
    text = request.args.get('textToTranslate')

    translated = translator.english_to_french(text)

    return translated


@app.route("/frenchToEnglish")
def french_to_english():
    """
    This route takes a param for input text and returns a translated string:
    textToTranslate: str
    """
    text = request.args.get('textToTranslate')

    translated = translator.french_to_english(text)

    return translated


@app.route("/")
def render_index():
    """
    This is the root route for this server.
    It renders the index.html static page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
