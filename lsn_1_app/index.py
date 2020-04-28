from flask import Flask

web_service = Flask(__name__)

@web_service.route('/')
def home():
    return "Hello World!"

web_service.run(port=5001)