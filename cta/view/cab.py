from cta.model.cab import Cab, CabAmenity, CabBooking, CabImage, CabDeal, CabTax, CabDealAssociation, CabUser
from cta import app, db
from flask import jsonify, request
from cta.lib.cab_fare import CabFare
from cta.schema.cab import CabAmenitySchema, CabBookingSchema, CabImageSchema, CabDealSchema, CabSchema, CabTaxSchema, CabUserSchema
import datetime
from itertools import cycle
import simplejson as json




@app.route('/api/v1/cab', methods=['GET', 'POST'])
def cab_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        cab_type = request.args.get('cab_type', None)
        source_lat = request.args.get('source_lat', None)
        source_lon = request.args.get('source_lon', None)
        destination_lat = request.args.get('destination_lat', None)
        destination_lon = request.args.get('destination_lon', None)
        args.pop('source_lat', None)
        args.pop('source_lon', None)
        args.pop('destination_lat', None)
        args.pop('destination_lon', None)
        min_base_fare = request.args.get('min_base_fare', None)
        max_base_fare = request.args.get('max_base_fare', None)
        min_total_fare = request.args.get('min_total_fare', None)
        max_total_fare = request.args.get('max_total_fare', None)
        args.pop('min_base_fare', None)
        args.pop('max_base_fare', None)
        args.pop('min_total_fare', None)
        args.pop('max_total_fare', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        args.pop('page', None)
        args.pop('per_page', None)
        q = db.session.query(Cab).outerjoin(Cab.amenities).outerjoin(Cab.deals)
        for key in args:
            if key in Cab.__dict__:
                q = q.filter(getattr(Cab, key) == args[key])
            elif key in CabAmenity.__dict__:
                q = q.filter(getattr(CabAmenity, key) == args[key])
            elif key in CabDeal.__dict__:
                q = q.filter(getattr(CabDeal, key) == args[key])
        if min_base_fare and max_base_fare:
            q = q.filter(CabDeal.base_fare >= min_base_fare, CabDeal.base_fare <= max_base_fare)
        elif min_total_fare and max_total_fare:
            q = q.filter(CabDeal.total_fare >= min_total_fare, CabDeal.total_fare <= max_total_fare)
        elif rating:
            q = q.filter(Cab.rating >= rating)
        data = q.offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = CabSchema(many=True).dump(data)
        total_fare = CabFare.fare_calculation(source_lat, source_lon, destination_lat, destination_lon, cab_type)
        for cab in result['cab']:
            cab['total_fare'] = total_fare
        return jsonify({'result': {'cabs': result.data}, 'message': "Success", 'error': False})
    else:
        cab = request.json
        deals = cab.get("deals", None)
        images = cab.get("images", None)
        amenities = cab.get("amenities", None)
        cab.pop('amenities', None)
        cab.pop('deals', None)
        cab.pop('images', None)
        cab_post = Cab(**cab)
        cab_post.save()
        for deal in deals:
            if deal.get("deal_id", None):
                assoc_post = CabDealAssociation(cab_id=cab_post.id, deal_id=deal.get("deal_id", None))
                assoc_post.save()
            else:
                if deal.get("tax", None):
                    tax = deal.get("tax", None)
                    deal.pop('tax', None)
                    deal_post = CabDeal(**deal)
                    cab_post.deals.append(deal_post)
                    deal_post.save()
                    tax_post = CabTax(**tax)
                    deal_post.tax = tax_post
                    tax_post.save()
                else:
                    deal_post = CabDeal(**deal)
                    cab_post.deals.append(deal_post)
                    deal_post.save()
        for image in images:
            image["cab_id"] = cab_post.id
            image_post = CabImage(**image)
            cab_post.images.append(image_post)
            image_post.save()
        amenities["cab_id"] = cab_post.id
        amenities_post = CabAmenity(**amenities)
        cab_post.amenities = amenities_post
        amenities_post.save()
        result = CabSchema().dump(cab_post)
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


@app.route('/api/v1/cab/user', methods=['GET', 'POST'])
def cab_user():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CabUser.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabUserSchema(many=True).dump(data)
        return jsonify({'result': {'users': result.data}, 'message': "Success", 'error': False})
    else:
        post = CabUser(**request.json)
        post.save()
        result = CabUserSchema().dump(post)
        return jsonify({'result': {'users': result.data}, 'message': "Success", 'error': False})


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