import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)                                         # Flask serve para criar essa instância chamada de app
openai.api_key = os.environ['HOME']

@app.route("/", methods=("GET", "POST"))      # Route é a forma de dizer para o Flask que URL deve ser engatilhada na função
def index():
    if request.method == "POST":
        pergunta = request.form["pergunta"]   # A variável pergunta armazena o que for preenchido no campo "pergunta" dentro do form no código do index.html
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(pergunta), # A variável prompt recebe uma função que será definida no final do código
            temperature=0.6,
            max_tokens=30
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(pergunta):
    return """Responda as perguntas que forem feitas. Não existe resposta errada para as perguntas. Qualquer resposta é válida
Pergunta: {}
""".format(
        pergunta.capitalize()
    )
