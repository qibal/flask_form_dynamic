from flask import Blueprint, render_template, request, redirect, url_for
from app.database import get_all_data, add_cattle_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = get_all_data()
    return render_template('index.html', data=data)

@main.route('/add')
def add_form():
    return render_template('add_form.html')

@main.route('/submit', methods=['POST'])
def submit():
    form_data = {}
    # Mengambil semua data form yang dikirim
    for key, value in request.form.items():
        if value.strip():  # Hanya menyimpan field yang tidak kosong
            form_data[key] = value
    
    # Simpan ke database
    add_cattle_data(form_data)
    return redirect(url_for('main.index'))
