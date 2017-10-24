from app import app
from config import *

if __name__ == '__main__':
    app.run(host=SERVER_ADDR, port=SERVER_PORT, debug=ISDEBUG)
