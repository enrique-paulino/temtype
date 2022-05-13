from waitress import serve
from temtype import app as application

if __name__ == '__main__':
    serve(application, host="127.0.0.1", port=5000)
    #application.run(debug=False)
