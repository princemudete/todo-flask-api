from flask import Blueprint, request, jsonify, abort

from .models import db, Todo
from .schemas import todo_schema, todos_schema

bp = Blueprint("api", __name__)


@bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask TODO API running"})


@bp.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return todos_schema.jsonify(todos)


@bp.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):
    todo = db.session.get(Todo, id)
    if not todo:
        abort(404)
    return todo_schema.jsonify(todo)


@bp.route("/todos", methods=["POST"])
def create_todo():
    json_data = request.get_json()
    if not json_data:
        abort(400, "No input data provided")

    try:
        todo = todo_schema.load(json_data, session=db.session)
        db.session.add(todo)
        db.session.commit()
        return todo_schema.jsonify(todo), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))


@bp.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = db.session.get(Todo, id)
    if not todo:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        abort(400, "No input data provided")

    try:
        todo = todo_schema.load(json_data, instance=todo, session=db.session, partial=True)
        db.session.commit()
        return todo_schema.jsonify(todo)
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))


@bp.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = db.session.get(Todo, id)
    if not todo:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    return "", 204


@bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@bp.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400


def register_routes(app):
    app.register_blueprint(bp)
