from flask import Blueprint, jsonify, request, g
from flask.views import MethodView
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app import db
from app.auth import login_required
from app.common import MatchSchema
from app.common.errors import error_response
from app.database import Match, Job

matchs_blueprint = Blueprint('matchs', __name__)

matchs_schema = MatchSchema(many=True)
match_schema = MatchSchema()


class MatchsAPI(MethodView):
    """
    Matchs Resource
    """

    @login_required
    def get(self, match_id=None):
        if match_id is None:
            response = match_schema.dump(Match.query.filter_by(**dict(request.args)))
        else:
            response = match_schema.dump(Match.query.get_or_404(match_id))
        return jsonify(response[0])

    @login_required
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return error_response(400, 'No input data provided')
        try:
            data = match_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422
        match = Match(
            interest=data[0]['interest'],
            user=g.user,
            job=Job.query.get(data[0]['job_id'])
        )
        db.session.add(match)
        try:
            db.session.commit()
        except IntegrityError:
            return error_response(422, 'already exists')
        result = match_schema.dump(Match.query.get(match.id))
        return jsonify(result[0])

    @login_required
    def put(self, match_id):
        json_data = request.get_json()
        if not json_data:
            return error_response(400, 'No input data provided')
        try:
            data = match_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422
        match = Match.query.get(match_id)
        match.interest = data[0]['interest']
        db.session.add(match)
        db.session.commit()
        result = match_schema.dump(Match.query.get(match.id))
        return jsonify(result[0])


matchs_api = MatchsAPI.as_view('matchs_api')

matchs_blueprint.add_url_rule(
    '/matchs',
    view_func=matchs_api,
    methods=['GET', 'POST', 'PUT']
)
