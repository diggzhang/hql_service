from app import app
app.config.from_object('config')

if __name__ == '__main__':
    app.run(host=app.config.get('SERVER_ADDR'),
            port=app.config.get('SERVER_PORT'),
            debug=app.config.get('ISDEBUG'))
