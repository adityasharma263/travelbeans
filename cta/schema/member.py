# -*- coding: utf-8 -*-

from cta.model.member import Member
from cta import ma


class MemberSchema(ma.ModelSchema):
    class Meta:
        model = Member
        exclude = ('updated_at', 'created_at')