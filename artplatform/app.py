from artplatform import create_app

app = create_app('deploy')

if __name__ == "__main__":
    app.debug = True
    app.run()


