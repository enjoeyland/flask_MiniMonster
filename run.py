# This is the file that is invoked to start up a development server.
# It gets a copy of the app from your package and runs it.
# This won't be used in production, but it will see a lot of mileage in development.

from app import app

from app import views

app.run(host = '0.0.0.0',port = 80, debug = True, threaded=True)
