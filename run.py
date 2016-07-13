from app import app
import app_config

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
