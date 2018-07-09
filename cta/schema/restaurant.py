# -*- coding: utf-8 -*-

from cta.model.restaurant import Restaurant, RestaurantAmenity, RestaurantImage,\
    Category, Collections, Cuisines, Association
from cta import ma


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        exclude = ('updated_at', 'created_at')


class CollectionsSchema(ma.ModelSchema):
    class Meta:
        model = Collections
        exclude = ('updated_at', 'created_at')


class RestaurantAmenitySchema(ma.ModelSchema):
    class Meta:
        model = RestaurantAmenity
        exclude = ('updated_at', 'created_at')


class RestaurantImageSchema(ma.ModelSchema):
    class Meta:
        model = RestaurantImage
        exclude = ('updated_at', 'created_at')


class CuisinesSchema(ma.ModelSchema):
    class Meta:
        model = Cuisines
        exclude = ('updated_at', 'created_at')


class AssociationSchema(ma.ModelSchema):
    class Meta:
        model = Association
        exclude = ('updated_at', 'created_at')


class RestaurantSchema(ma.ModelSchema):
    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')