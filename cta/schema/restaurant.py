# -*- coding: utf-8 -*-

from cta.model.restaurant import Restaurant, RestaurantAmenity, RestaurantImage,\
    Menu, Collection, Cuisine, Association, Dish

from cta import ma


class MenuSchema(ma.ModelSchema):
    class Meta:
        model = Menu
        exclude = ('updated_at', 'created_at')


class CollectionSchema(ma.ModelSchema):
    class Meta:
        model = Collection
        exclude = ('updated_at', 'created_at')

class DishSchema(ma.ModelSchema):
    class Meta:
        model = Dish
        exclude = ('updated_at', 'created_at')

class RestaurantAmenitySchema(ma.ModelSchema):
    class Meta:
        model = RestaurantAmenity
        exclude = ('updated_at', 'created_at')

class RestaurantImageSchema(ma.ModelSchema):
    class Meta:
        model = RestaurantImage
        exclude = ('updated_at', 'created_at')


class CuisineSchema(ma.ModelSchema):
    class Meta:
        model = Cuisine
        exclude = ('updated_at', 'created_at')


class AssociationSchema(ma.ModelSchema):
    dishes = ma.Nested(DishSchema, many=False)
    collections = ma.Nested(CollectionSchema, many=False)
    cuisines = ma.Nested(CuisineSchema, many=False)

    class Meta:
        model = Association
        exclude = ('updated_at', 'created_at')

class RestaurantSchema(ma.ModelSchema):
    amenities = ma.Nested(RestaurantAmenitySchema, many=False)
    images = ma.Nested(RestaurantImageSchema, many=True)
    menus = ma.Nested(MenuSchema, many=False)
    association = ma.Nested(AssociationSchema, many=True)
    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')