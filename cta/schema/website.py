# -*- coding: utf-8 -*-

from cta.model.website import Website
from cta.schema.price import PriceSchema
from cta import ma


class WebsiteSchema(ma.ModelSchema):
    price = ma.Nested(PriceSchema, many=True)

    class Meta:
        model = Website
        exclude = ('updated_at', 'created_at', 'room')