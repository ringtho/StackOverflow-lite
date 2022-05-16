import os
from stackoverflow.routes import app
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'), port=5000)