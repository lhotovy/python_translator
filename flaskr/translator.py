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
    translator = deepl.Translator(DEEPL_API_KEY)

    if form.validate_on_submit():            
        user_text = str(form.userInput.data)
        target_lang = str(form.target_lang.data)

        result = translator.translate_text(user_text, target_lang=target_lang)
        form.output.data = result
        print(result)
        print(result.detected_source_lang)
   
    return render_template("page.html", form=form)


if __name__ == "__main__":
   app.run(debug=True, port=3001)
