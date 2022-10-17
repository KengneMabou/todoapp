# The main entry script.

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core import app
from models import *
from controllers import *
from models.sqlalchemy_init import db

def start_app(name):
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # db.create_all()
    app.debug = True
    app.run(host="0.0.0.0")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('The main entry point')
    start_app('Starting the app ...')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
