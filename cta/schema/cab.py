# -*- coding: utf-8 -*-

from cta.model.cab import Cab, CabAmenity, CabBooking, CabImage, CabInvoice, CabTax
from cta import ma


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


class CabInvoiceSchema(ma.ModelSchema):
    class Meta:
        model = CabInvoice
        exclude = ('updated_at', 'created_at')


class CabBookingSchema(ma.ModelSchema):
    invoices = ma.Nested(CabInvoiceSchema, many=False)
    class Meta:
        model = CabBooking
        exclude = ('updated_at', 'created_at')


class CabSchema(ma.ModelSchema):
    bookings = ma.Nested(CabBookingSchema, many=True)
    amenities = ma.Nested(CabAmenitySchema, many=False)
    images = ma.Nested(CabImageSchema, many=True)

    class Meta:
        model = Cab
        exclude = ('updated_at', 'created_at')