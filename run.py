#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice
from webscraper import *
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id

def random_headline():
    with open("headlines.json",'r') as f:
        headline = json.load(f)
    return choice(headline)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    return render_template("scrape.html", headline=random_headline())


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/table")
def table():
    return render_template("table.html")



@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)


if __name__ == "__main__":
    app.run()
