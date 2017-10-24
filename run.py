from app import app

if __name__ == '__main__':
    app.config.from_object('config')
    app.run(host=app.config.get('SERVER_ADDR'),
            port=app.config.get('SERVER_PORT'),
            debug=app.config.get('ISDEBUG'))
