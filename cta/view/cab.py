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
        amenity = request.args.get('amenity')
        args.pop('amenity', None)
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        amenity_cab_id = []
        common_id = []
        if amenity:
            is_filter = 1
            try:
                cab_list = CabAmenity.query.filter(getattr(CabAmenity, amenity).is_(True)).all()
                for cab_obj in cab_list:
                    amenity_cab_id.append(cab_obj.cab_id)
            except:
                amenity_cab_id = []
        obj = {
            "amenity": amenity_cab_id,
        }
        for key, value in obj.items():
            if value:
                if not common_id:
                    common_id = value
                else:
                    common_id = list(set(common_id).intersection(value))
        data = Cab.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CabSchema(many=True).dump(data)
        return jsonify({'result': {'cabs': result.data}, 'message': "Success", 'error': False})
    else:
        obj = request.json
        deal = obj["deals"]
        obj.pop('deals', None)
        # obj["deals"] = tuple(obj["deals"])
        p = Cab(**obj)
        # a = CabDealAssociation()
        for deal in deal:
            a = CabDeal(**deal)
            p.deals.append(a)
        p.save()
        result = CabSchema().dump(p)
        return jsonify({'result': {'cab': result.data}, 'message': "Success", 'error': False})