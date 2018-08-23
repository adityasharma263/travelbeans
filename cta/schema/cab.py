# -*- coding: utf-8 -*-

from cta.model.cab import Cab, CabAmenity, CabImage, CabDeal, CabWebsite, CabCollection, CabCollectionProduct
from cta import ma


class CabWebsiteSchema(ma.ModelSchema):
    class Meta:
        model = CabWebsite
        exclude = ('updated_at', 'created_at')


class CabAmenitySchema(ma.ModelSchema):
    class Meta:
        model = CabAmenity
        exclude = ('updated_at', 'created_at')


class CabImageSchema(ma.ModelSchema):
    class Meta:
        model = CabImage
        exclude = ('updated_at', 'created_at')


class CabCollectionProductSchema(ma.ModelSchema):
    class Meta:
        model = CabCollectionProduct
        exclude = ('updated_at', 'created_at')


class CabDealSchema(ma.ModelSchema):
    website = ma.Nested(CabWebsiteSchema, many=False)

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


class CabCollectionSchema(ma.ModelSchema):
    products = ma.Nested(CabCollectionProductSchema, many=True)
    cabs = ma.Nested(CabSchema, many=True)

    class Meta:
        model = CabCollection
        exclude = ('updated_at', 'created_at', 'hotel')