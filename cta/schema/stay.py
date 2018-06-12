# -*- coding: utf-8 -*-

from cta.model.stay import Stay
from cta import ma


class StaySchema(ma.ModelSchema):

    class Meta:
        model = Stay
        exclude = ('updated_at', 'created_at')