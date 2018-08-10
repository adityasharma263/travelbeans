from cta.model.cab import Cab, CabAmenity, CabBooking, CabImage, CabDeal, CabTax, CabDealAssociation
from cta import app, db
from flask import jsonify, request
from cta.schema.cab import CabAmenitySchema, CabBookingSchema, CabImageSchema, CabDealSchema, CabSchema, CabTaxSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/cab', methods=['GET', 'POST'])
def cab_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        min_fare = request.args.get('min_fare', None)
        max_fare = request.args.get('max_fare', None)
        args.pop('price_start', None)
        args.pop('price_end', None)
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        q = db.session.query(Cab).outerjoin(Cab.amenities).outerjoin(Cab.deals)
        for key in args:
            if key in Cab.__dict__:
                q = q.filter(getattr(Cab, key) == args[key])
            elif key in CabAmenity.__dict__:
                q = q.filter(getattr(CabAmenity, key) == args[key])
            elif key in CabDeal.__dict__:
                q = q.filter(getattr(CabDeal, key) == args[key])
        if min_fare and max_fare:
            q = q.filter(CabDeal.base_fare >= min_fare, CabDeal.base_fare <= max_fare)
        elif rating:
            q = q.filter(Cab.rating >= rating)
        data = q.offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = CabSchema(many=True).dump(data)
        return jsonify({'result': {'cabs': result.data}, 'message': "Success", 'error': False})
    else:
        obj = request.json
        deals = []
        # deal = obj["deals"]
        # obj.pop('deals', None)

        for index, deal in enumerate(obj["deals"]):
            print(deal)
            deal = frozenset(deal.items())
            obj["deals"][index] = deal
        print(obj)
        p = Cab(**obj)
        # a =
        # for deal in deal:
        c = CabDeal()
        p.deals.append(c)

        # a = CabDealAssociation(cab_id=p, deal_id=c)
        # a.save()
        p.save()
        result = CabSchema().dump(p)
        return jsonify({'result': {'cab': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/cab/amenity', methods=['GET', 'POST'])
def cab_amenity():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabAmenity.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabAmenitySchema(many=True).dump(data)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabAmenity(**request.json)
        post.save()
        result = CabAmenitySchema().dump(post)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/cab/deal', methods=['GET', 'POST'])
def cab_deal():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabDeal.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabDealSchema(many=True).dump(data)
        return jsonify({'result': {'deals': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabDeal(**request.json)
        post.save()
        result = CabDealSchema().dump(post)
        return jsonify({'result': {'deals': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/images', methods=['GET', 'POST'])
def cab_image_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabImage.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabImageSchema(many=True).dump(data)
        return jsonify({'result': {'images': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabImage(**request.json)
        post.save()
        result = CabImageSchema().dump(post)
        return jsonify({'result': {'image': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/cab/booking', methods=['GET', 'POST'])
def cab_booking():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabBooking.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabBookingSchema(many=True).dump(data)
        return jsonify({'result': {'bookings': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabBooking(**request.json)
        post.save()
        result = CabBookingSchema().dump(post)
        return jsonify({'result': {'bookings': result.data}, 'message': "Success", 'error': False})

@app.route('/api/v1/cab/tax', methods=['GET', 'POST'])
def cab_tax():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabTax.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabTaxSchema(many=True).dump(data)
        return jsonify({'result': {'taxes': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabTax(**request.json)
        post.save()
        result = CabTaxSchema().dump(post)
        return jsonify({'result': {'taxes': result.data}, 'message': "Success", 'error': False})