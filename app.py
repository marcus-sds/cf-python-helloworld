import os
from flask import Flask

app = Flask(__name__.split('.')[0])

@app.route('/')
def index():
        for x in range(1,10):
                print "Hello World"
        return "Hello World!\n"

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))
