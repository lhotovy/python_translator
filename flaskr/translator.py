from flask import Flask, render_template
import deepl


app = Flask(__name__, static_folder="../static")


@app.route('/')
def home():
    return render_template("page.html")


if __name__ == "__main__":
    app.run(debug=True, port=3001)

DEEPL_API_KEY = "e4219fbb-19e6-f0d9-f6d5-1dab58ad3b2f:fx"
DEEPL_ENDPOINT = " https://api-free.deepl.com"

translator = deepl.Translator(DEEPL_API_KEY)

user_text = str(input("What do you want to translate? ").encode("utf-8"))
target_lang = input('Select target language: ')


result = translator.translate_text(user_text, target_lang=target_lang)
print(result)
print(result.detected_source_lang)


