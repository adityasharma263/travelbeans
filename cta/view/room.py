# -*- coding: utf-8 -*-

from cta.model.room import Room, Member, Facility
from cta import app
from flask import jsonify, request
from cta.schema.room import RoomSchema, MemberSchema, FacilitySchema
import datetime


@app.route('/api/v1/room', methods=['GET', 'POST'])
def room_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        date_from = request.args.get('date_from')
        date_to = request.args.get('date_to')
        if date_from and date_to:
            date_from = datetime.datetime.fromtimestamp(
                int(date_from)).strftime('%Y-%m-%d %H:%M:%S')
            date_to = datetime.datetime.fromtimestamp(
                int(date_to)).strftime('%Y-%m-%d %H:%M:%S')
            args['check_in'] = date_from
            args['check_out'] = date_to
        args.pop('date_from', None)
        args.pop('date_to', None)
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        rooms = Room.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RoomSchema(many=True).dump(rooms)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})
    else:
        post = Room(**request.json)
        post.save()
        result = RoomSchema().dump(post)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/member', methods=['GET', 'POST'])
def member_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        members = Member.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = MemberSchema(many=True).dump(members)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})
    else:
        post = Member(**request.json)
        post.save()
        result = MemberSchema().dump(post)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})




@app.route('/api/v1/facility', methods=['GET', 'POST'])
def facility_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Facility.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = FacilitySchema(many=True).dump(data)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})
    else:
        post = Facility(**request.json)
        post.save()
        result = FacilitySchema().dump(post)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})