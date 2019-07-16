import os

FB_APP_ID = 513860962699080

# To generate a new secret key:
import random, string

SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
