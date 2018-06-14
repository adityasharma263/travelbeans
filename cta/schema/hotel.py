# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel
from cta.model.website import Website
from cta.model.image import Image
from cta.model.room import Room
from cta import ma


class StaySchema(ma.ModelSchema):

    class Meta:
        model =
        exclude = ('updated_at', 'created_at')