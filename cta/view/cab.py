from cta.model.cab import Cab, CabAmenity, CabBooking, CabImage, CabDeal, CabTax, CabDealAssociation
from cta import app
from flask import jsonify, request
from cta.schema.cab import CabAmenitySchema, CabBookingSchema, CabImageSchema, CabDealSchema, CabSchema, CabTaxSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/cab', methods=['GET', 'POST'])
def cab_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        # args.pop('page', None)
        # args.pop('per_page', None)
        # page = int(request.args.get('page', 1))
        # per_page = int(request.args.get('per_page', 10))
        data = Cab.query.filter_by(**args).all()
        result = CabSchema(many=True).dump(data)
        return jsonify({'result': {'cabs': result.data}, 'message': "Success", 'error': False})
    else:
        p = Cab(**request.json)
        # a = CabDealAssociation()
        # a = CabDeal()
        # p.deals.append(a)
        # post = Cab(**request.json)
        p.save()
        result = CabSchema().dump(p)
        return jsonify({'result': {'cab': result.data}, 'message': "Success", 'error': False})