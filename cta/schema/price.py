# -*- coding: utf-8 -*-

from cta.model.price import Price
from cta import ma


class PriceSchema(ma.ModelSchema):
    class Meta:
        model = Price
        exclude = ('updated_at', 'created_at')