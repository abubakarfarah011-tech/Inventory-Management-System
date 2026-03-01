#starts the application and calls the router to begin the cli program flow

# main.py

from cli.router import Router

if __name__ == "__main__":
    app = Router()
    app.start()