from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.logger.setLevel(logging.INFO)  
@app.route('/')
def home():
    app.logger.info("Page d'accueil visitée")
    return "Hello CI/CD & Observabilité!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
