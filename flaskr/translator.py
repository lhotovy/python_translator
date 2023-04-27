from flask import Flask, render_template, url_for, jsonify, request
import deepl
from form import TranslateForm

############# Global variables ##############

app = Flask(__name__)
app.secret_key = "gd6df5g4fhfg64h6fggh46gh"
DEEPL_API_KEY = "e4219fbb-19e6-f0d9-f6d5-1dab58ad3b2f:fx"
DEEPL_ENDPOINT = " https://api-free.deepl.com"

############# Routes #############

@app.route('/', methods=["GET", "POST"])
def home():
    form = TranslateForm()
    return render_template("page.html", form=form)

@app.route('/translated', methods=["POST", "GET"])
def translate():
    
    translator = deepl.Translator(DEEPL_API_KEY)

    user_text = request.args.get("inputText", 0, type=str)
    target_lang = request.args.get("target_lang", 0, type=str)

    result = translator.translate_text(user_text, target_lang=target_lang)
    print(result)
    print(result.detected_source_lang)
   
    return jsonify(result = result)


if __name__ == "__main__":
   app.run(debug=True, port=3001)
