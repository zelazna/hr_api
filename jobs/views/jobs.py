from flask import Blueprint, jsonify, request, g

from auth import login_required
from common.schemas import JobSchema
from database import Job, Match

jobs_blueprint = Blueprint('jobs', __name__)

jobs_schema = JobSchema(many=True)
job_schema = JobSchema()


@jobs_blueprint.route('/', methods=('GET',))
@login_required
def get_unmatched():
    user_matchs = [match.job_id for match in Match.query.filter_by(user_id=g.user.id)]
    filtered = Job.query.filter(~Job.id.in_(user_matchs)).filter_by(**dict(request.args))
    response = jobs_schema.dump(filtered)
    return jsonify(response[0])


@jobs_blueprint.route('/<int:job_id>', methods=('GET',))
@login_required
def get_one(job_id):
    response = job_schema.dump(Job.query.get_or_404(job_id))
    return jsonify(response[0])


@jobs_blueprint.route('/matched/<bool:match_type>', methods=('GET',))
@login_required
def get_matched(match_type):
    user_matchs = [match.job_id for match in Match.query.filter_by(user_id=g.user.id, interest=match_type)]
    filtered = Job.query.filter(Job.id.in_(user_matchs)).filter_by(**dict(request.args))
    response = jobs_schema.dump(filtered)
    return jsonify(response[0])
