# run.py
import os
from dotenv import load_dotenv
load_dotenv()
from app_package import create_app

app = create_app()

if __name__ == '__main__':
    # app.run()
    # app.run(host="0.0.0.0", port=8003)
    port = int(os.environ.get("FLASK_RUN_PORT"))
    host = os.environ.get("FLASK_RUN_HOST")
    print(f"port: {port}")
    print(f"host: {host}")
    app.run(host=host, port=port)
    # # app.run(port=port)