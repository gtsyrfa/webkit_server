#!/usr/bin/env python

from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from pytils.translit import translify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        translated_fname = translify(file.filename) # Делаем транслитерацию, 
        #    чтобы русские буквы не были стёрты функцией secure_filename
        fname = secure_filename(translated_fname) 
        fullpath = 'static/uploaded_files' + fname
        #Поверяем, был ли создан файл
        if os.path.exists(fullpath):
            return (f"Файл по имени \"{fname}\" уже существует! "+
            "Мы не станем его переписывать!")
        file.save(fullpath)
        return f"Файл по имени \"{fname}\" успешно загрузился!"
    return render_template("Uploadform.html")

app.run()