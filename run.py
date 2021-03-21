import logging

from app import app

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


if __name__ == '__main__':
    app.run()
