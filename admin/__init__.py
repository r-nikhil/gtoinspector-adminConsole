from flask import Blueprint, jsonify

admin_console = Blueprint('admin_console', __name__, url_prefix="/admin")

# TODO: Add routes

# Example

@admin_console.route("/test/")
def example():
    return jsonify(status='working well')

# The endpoint for this would be /admin/test/