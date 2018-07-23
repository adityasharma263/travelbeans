# -*- coding: utf-8 -*-

from cta.model.restaurant import Restaurant, RestaurantAmenity, RestaurantImage,\
    Tag, Collection, Cuisine, Association, Dish
# import graphene
# from graphene import relay
# from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
# from cta import ma


# class TagSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = Tag
#         interfaces = (relay.Node,)

# class TagConnection(relay.Connection):
#     class Meta:
#         node = TagSchema

# class CollectionSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = Collection
#         interfaces = (relay.Node,)

# class CollectionConnection(relay.Connection):
#     class Meta:
#         node = CollectionSchema


# class DishSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = Dish
#         interfaces = (relay.Node,)

# class DishConnection(relay.Connection):
#     class Meta:
#         node = DishSchema


# class RestaurantAmenitySchema(SQLAlchemyObjectType):
#     class Meta:
#         model = RestaurantAmenity
#         interfaces = (relay.Node,)


# class RestaurantAmenityConnection(relay.Connection):
#     class Meta:
#         node = RestaurantAmenitySchema


# class RestaurantImageSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = RestaurantImage
#         interfaces = (relay.Node,)

# class RestaurantImageConnection(relay.Connection):
#     class Meta:
#         node = RestaurantImageSchema

# class CuisineSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = Cuisine
#         interfaces = (relay.Node,)

# class CuisineConnection(relay.Connection):
#     class Meta:
#         node = CuisineSchema

# class AssociationSchema(SQLAlchemyObjectType):
#     class Meta:
#         model = Association
#         interfaces = (relay.Node,)

# class AssociationConnection(relay.Connection):
#     class Meta:
#         node = AssociationSchema


# # class RestaurantSchema(SQLAlchemyObjectType):
# #     class Meta:
# #         model = Restaurant
# #         interfaces = (relay.Node,)
# class RestaurantSchema(ma.ModelSchema):
#     amenities = ma.Nested(RestaurantAmenitySchema, many=False)
#     images = ma.Nested(RestaurantImageSchema, many=True)
#     tags = ma.Nested(TagSchema, many=False)
#     association = ma.Nested(AssociationSchema, many=True)

#     class Meta:
#         model = Restaurant
#         exclude = ('updated_at', 'created_at')

# # class RestaurantConnection(relay.Connection):
# #     class Meta:
# #         node = RestaurantSchema


# # class Query(graphene.ObjectType):
# #     node = relay.Node.Field()
# #     # Allows sorting over multiple columns, by default over the primary key
# #     all_tags = SQLAlchemyConnectionField(TagConnection)
# #     all_collections = SQLAlchemyConnectionField(CollectionConnection)
# #     all_cuisines = SQLAlchemyConnectionField(CuisineConnection)
# #     all_dishes = SQLAlchemyConnectionField(DishConnection)
# #     all_amenities = SQLAlchemyConnectionField(RestaurantAmenityConnection)
# #     all_images = SQLAlchemyConnectionField(RestaurantImageConnection)
# #     all_restaurants = SQLAlchemyConnectionField(RestaurantConnection)
# #     all_associations = SQLAlchemyConnectionField(AssociationConnection)

# # schema = graphene.Schema(query=Query)


from cta import ma


class TagSchema(ma.ModelSchema):
    class Meta:
        model = Tag
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
    tags = ma.Nested(TagSchema, many=False)
    association = ma.Nested(AssociationSchema, many=True)

    class Meta:
        model = Restaurant
        exclude = ('updated_at', 'created_at')