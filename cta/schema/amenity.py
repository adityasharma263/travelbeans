# -*- coding: utf-8 -*-

from cta.model.amenity import Amenity
from cta import ma


class AmenitySchema(ma.ModelSchema):
    class Meta:
        model = Amenity
        exclude = ('updated_at', 'created_at')