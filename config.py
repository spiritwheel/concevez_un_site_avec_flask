FB_APP_ID = 513860962699080

# To generate a new secret key:
import random, string

SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])
