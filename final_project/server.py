import machinetranslation
from deep_translator import MyMemoryTranslator
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    French_text=MyMemoryTranslator(source='english', target='french').translate(textToTranslate)
    print(French_text)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here 
    English_text=MyMemoryTranslator(source='french', target='english').translate(textToTranslate)
    print(English_text)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
