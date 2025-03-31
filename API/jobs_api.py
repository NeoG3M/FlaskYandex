import flask
from flask import jsonify, make_response, request

from data import db_session
from data.jobs import Job

jobs_bp = flask.Blueprint('jobs_api', __name__)


@jobs_bp.route('/jobs', methods=['GET'])
def get_all_jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify({'jobs': [item.to_dict(only=('id', 'work_size', 'job')) for item in jobs]})


@jobs_bp.route('/jobs', methods=['POST'])
def post_job():
    if not request.json:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if not all(key in request.json for key in ['team_leader', 'job', 'work_size', 'is_finished', 'collaborators']):
        return make_response(jsonify({'error': 'Wrong request'}), 400)

    job = Job(
        id=request.json['id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        is_finished=request.json['is_finished']
    )
    session = db_session.create_session()
    session.add(job)
    session.commit()
    return jsonify({'id': job.id})


@jobs_bp.route('/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    session = db_session.create_session()
    job = session.get(Job, job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'jobs': [job.to_dict(only=('id', 'work_size', 'job'))]})
