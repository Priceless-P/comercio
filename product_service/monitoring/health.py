from flask import jsonify
from monitoring import health_blueprint


def is_database_reachable():
    """Check if database is connected"""
    try:
        from application.models import Product
        Product.query.all()
        return True
    except Exception:
        return False


@health_blueprint.route('/health')
def health_check():
    """Registers health check endpoints"""
    if is_database_reachable():
        return jsonify({'status': 'healthy'}), 200
    else:
        return jsonify({'status': 'unhealthy'}), 503
