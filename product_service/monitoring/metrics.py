from monitoring import metrics_blueprint
from prometheus_client import Counter, REGISTRY, generate_latest


REQUEST_COUNT = Counter('http_request_total', 'Total HTTP Request', ['method', 'endpoint'])

@metrics_blueprint.route('/metrics')
def metrics():
    """Setup prometheus metrics"""
    return generate_latest(REGISTRY), 200
