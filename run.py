import os
from dotenv import load_dotenv
load_dotenv()
from app_package import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5050)
    # This options have not been working on the server
    # app.run()
    port = int(os.environ.get("FLASK_RUN_PORT"))
    host = os.environ.get("FLASK_RUN_HOST")
    app.run(host=host, port=port)
    # app.run(port=port)