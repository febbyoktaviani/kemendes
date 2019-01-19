from flask import Flask
from flask_script import Manager
from flask_script import Command


app = Flask(__name__)
# configure your app

manager = Manager(app)

class Hello(Command):
    print(dir(app))

    def run(self):
        print("hello world")

manager.add_command('hello', Hello())

if __name__ == "__main__":
    manager.run()
