
from flask import Flask, render_template, request, redirect, url_for
from app import app

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)
