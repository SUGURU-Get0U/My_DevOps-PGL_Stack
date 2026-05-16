import os
import redis
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
)
metrics = PrometheusMetrics(app) # This creates the /metrics route automatically

from views import ticket_blueprint

app.register_blueprint(ticket_blueprint)

