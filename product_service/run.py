from prometheus_client import start_http_server
from application import create_app, db
from application import models
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
    start_http_server(8001)
