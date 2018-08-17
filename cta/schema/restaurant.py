# -*- coding: utf-8 -*-

from cta.model.restaurant import Restaurant, RestaurantAmenity, RestaurantImage,\
    Menu, Collection, Cuisine, RestaurantAssociation, Dish, RestaurantChain

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


class RestaurantAssociationSchema(ma.ModelSchema):

    class Meta:
        model = RestaurantAssociation
        exclude = ('updated_at', 'created_at')


class RestaurantForChainSchema(ma.ModelSchema):
    amenities = ma.Nested(RestaurantAmenitySchema, many=False)
    images = ma.Nested(RestaurantImageSchema, many=True)
    dishes = ma.Nested(DishSchema, many=True)
    menus = ma.Nested(MenuSchema, many=False)
    collections = ma.Nested(CollectionSchema, many=True)
    cuisines = ma.Nested(CuisineSchema, many=True)

    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')


class RestaurantChainSchema(ma.ModelSchema):
    restaurants = ma.Nested(RestaurantForChainSchema, many=True)

    class Meta:
        model = RestaurantChain
        exclude = ('updated_at', 'created_at')


class RestaurantSchema(ma.ModelSchema):
    amenities = ma.Nested(RestaurantAmenitySchema, many=False)
    images = ma.Nested(RestaurantImageSchema, many=True)
    dishes = ma.Nested(DishSchema, many=True)
    menus = ma.Nested(MenuSchema, many=False)
    collections = ma.Nested(CollectionSchema, many=True)
    cuisines = ma.Nested(CuisineSchema, many=True)
    restaurant_chain = ma.Nested(RestaurantChainSchema, many=False, exclude=('restaurants', 'updated_at', 'created_at'))

    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')