# -*- coding: utf-8 -*-

from cta.model.website import Website
from cta import ma


class WebsiteSchema(ma.ModelSchema):

    class Meta:
        model = Website
        exclude = ('updated_at', 'created_at', 'room')