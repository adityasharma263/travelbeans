# -*- coding: utf-8 -*-

from cta.model.cab import Cab, CabAmenity, CabBooking, CabImage, CabDeal, CabTax, CabWebsite, CabUser
from cta import ma


class CabWebsiteSchema(ma.ModelSchema):
    class Meta:
        model = CabWebsite
        exclude = ('updated_at', 'created_at')


class CabTaxSchema(ma.ModelSchema):
    class Meta:
        model = CabTax
        exclude = ('updated_at', 'created_at')


class CabAmenitySchema(ma.ModelSchema):
    class Meta:
        model = CabAmenity
        exclude = ('updated_at', 'created_at')


class CabImageSchema(ma.ModelSchema):
    class Meta:
        model = CabImage
        exclude = ('updated_at', 'created_at')


class CabDealSchema(ma.ModelSchema):
    website = ma.Nested(CabWebsiteSchema, many=False)
    tax = ma.Nested(CabTaxSchema, many=False)

    class Meta:
        model = CabDeal
        exclude = ('updated_at', 'created_at')


class CabSchema(ma.ModelSchema):
    deals = ma.Nested(CabDealSchema, many=True)
    amenities = ma.Nested(CabAmenitySchema, many=False)
    images = ma.Nested(CabImageSchema, many=True)

    class Meta:
        model = Cab
        exclude = ('updated_at', 'created_at')


class CabUserSchema(ma.ModelSchema):
    class Meta:
        model = CabUser
        exclude = ('updated_at', 'created_at')


class CabLogsSchema(ma.ModelSchema):
    amenities = ma.Nested(CabAmenitySchema, many=False)
    images = ma.Nested(CabImageSchema, many=True)

    class Meta:
        model = Cab
        exclude = ('updated_at', 'created_at')


class CabBookingSchema(ma.ModelSchema):
    user = ma.Nested(CabUserSchema, many=False)
    deal = ma.Nested(CabDealSchema, many=False)
    cab = ma.Nested(CabLogsSchema, many=False)

    class Meta:
        model = CabBooking
        exclude = ('updated_at', 'created_at')