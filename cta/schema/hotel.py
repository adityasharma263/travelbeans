# -*- coding: utf-8 -*-
from cta.model.hotel import Hotel
from cta.model.hotel import Image
from cta.model.hotel import Facility
from cta.model.hotel import Member
from cta.schema.base import safe_execute
from cta.model.hotel import Amenity
from cta.model.hotel import Deal
from cta.model.hotel import Website
from cta.model.hotel import Room
from cta.model.hotel import HotelCollection
from cta.model.hotel import CollectionProduct

from cta import ma


class WebsiteSchema(ma.ModelSchema):

    class Meta:
        model = Website
        exclude = ('updated_at', 'created_at', 'hotel')


class DealSchema(ma.ModelSchema):
    website = ma.Nested(WebsiteSchema, many=False)

    class Meta:
        model = Deal
        exclude = ('updated_at', 'created_at')


class AmenitySchema(ma.ModelSchema):
    class Meta:
        model = Amenity
        exclude = ('updated_at', 'created_at', 'hotel')


class CollectionProductSchema(ma.ModelSchema):
    class Meta:
        model = CollectionProduct
        exclude = ('updated_at', 'created_at')


class HotelCollectionSchema(ma.ModelSchema):
    products = ma.Nested(CollectionProductSchema, many=True)

    class Meta:
        model = HotelCollection
        exclude = ('updated_at', 'created_at', 'hotel')


class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image
        exclude = ('updated_at', 'created_at', 'hotel')


class MemberSchema(ma.ModelSchema):
    class Meta:
        model = Member
        exclude = ('updated_at', 'created_at', 'hotel')


class FacilitySchema(ma.ModelSchema):
    class Meta:
        model = Facility
        exclude = ('updated_at', 'created_at', 'hotel')


class RoomSchema(ma.ModelSchema):
    deals = ma.Nested(DealSchema, many=True)
    member = ma.Nested(MemberSchema, many=False)
    facilities = ma.Nested(FacilitySchema, many=False)
    check_in = ma.Method('check_in_epoch')
    check_out = ma.Method('check_out_epoch')

    def check_in_epoch(self, obj):
        return safe_execute(None, ValueError, obj.check_in)

    def check_out_epoch(self, obj):
        return safe_execute(None, ValueError, obj.check_out)

    class Meta:
        model = Room
        exclude = ('updated_at', 'created_at')


class HotelSchema(ma.ModelSchema):
    amenities = ma.Nested(AmenitySchema, many=False)
    collection = ma.Nested(HotelCollectionSchema, many=False)
    images = ma.Nested(ImageSchema, many=True)
    rooms = ma.Nested(RoomSchema, many=True)


    class Meta:
        model = Hotel
        exclude = ('updated_at', 'created_at')