from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!\n'


@app.route('/books')
def display_books():
    books = [
        {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        },
        {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        },
        {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        },
        {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        },
        {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        }
    ]
    return render_template("index.htm", books=books)