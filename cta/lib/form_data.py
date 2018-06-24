# # -*- coding: utf-8 -*-
# import datetime
#
# class Formdata():
#
#     def hotel_data(self, data):
#         hotel = data['hotel']
#         hotel_obj = {
#             "id": hotel.get("id", None),
#             "name": hotel.get("name", None),
#             "city": hotel.get("city", None),
#             'rating': hotel.get("rating", None),
#             "desc": hotel.get("desc", None),
#             "room_type": hotel.get("room_type", None),
#             "address": hotel.get("address", None),
#             "star": hotel.get("star", None),
#             "check_in": datetime.datetime.now(),
#             "check_out": datetime.datetime.now(),
#             "status": hotel.get("status", None),
#             "breakfast": hotel.get("breakfast", None),
#             "balcony": hotel.get("ac", None),
#         }
#         return hotel_obj
#
#         member = hotel.get("member", None)
#         if member:
#             member_obj = {
#                 "no_of_adults": member.get("no_of_adults", None),
#                 "total_members": member.get("total_members", None),
#                 "children": member.get("children", None),
#                 "hotel_id": hotel_obj['id'],
#             }
#             print(member_obj)
#             Member(**member_obj).save()
#         facility = hotel.get("facilities", None)
#         facility_obj = {
#             "hotel_id": hotel_obj['id'],
#             "ac": facility.get("ac", None),
#             "bed_type": facility.get("bed_type", None),
#             "no_of_bed": facility.get("no_of_bed", None),
#             "bathroom_cosmetics": facility.get("bathroom_cosmetics", None),
#             "bathroom_nightie": facility.get("bathroom_nightie", None),
#             "bathroom_towels": facility.get("bathroom_towels", None),
#             "bathroom_with_shower": facility.get("bathroom_with_shower", None),
#             "desk": facility.get("desk", None),
#             "electric_kettle": facility.get("electric_kettle", None),
#             "fan": facility.get("fan", None),
#             "food_serve_at_room": facility.get("food_serve_at_room", None),
#             "free_evening_snacks": facility.get("free_evening_snacks", None),
#             "free_toiletries": facility.get("free_toiletries", None),
#             "hairdryer": facility.get("hairdryer", None),
#             "heater": facility.get("heater", None),
#             "ironing_facility": facility.get("ironing_facility", None),
#             "morning_newspaper": facility.get("morning_newspaper", None),
#             "phone": facility.get("phone", None),
#             "room_safe": facility.get("room_safe", None),
#             "room_seating_area": facility.get("room_seating_area", None),
#             "room_slipper": facility.get("room_slipper", None),
#             "tv": facility.get("tv", None),
#             "view": facility.get("view", None),
#             "wardrobes_closet": facility.get("wardrobes_closet", None),
#             "weighing_machine": facility.get("weighing_machine", None),
#             "wifi": facility.get("wifi", None)
#         }
#         Facility(**facility_obj).save()
#         amenity = hotel.get("amenities", None)
#         amenity_obj = {
#             "hotel_id": hotel_obj['id'],
#             "Room_cleaning_service": amenity.get("Room_cleaning_service", None),
#             "banquets": amenity.get("banquets", None),
#             "bar": amenity.get("bar", None),
#             "child_baby_cot": amenity.get("child_baby_cot", None),
#             "conference_room": amenity.get("conference_room", None),
#             "doorman": amenity.get("doorman", None),
#             "express_check_in_out": amenity.get("express_check_in_out", None),
#             "gym": amenity.get("gym", None),
#             "hairdresser": amenity.get("hairdresser", None),
#             "indoor_swimming_pool": amenity.get("indoor_swimming_pool", None),
#             "laundry_service": amenity.get("laundry_service", None),
#             "lift": amenity.get("lift", None),
#             "non_smoking_smoking_rooms": amenity.get("non_smoking_smoking_rooms", None),
#             "outdoor_swimming_pool": amenity.get("outdoor_swimming_pool", None),
#             "pet_allowance": amenity.get("pet_allowance", None),
#             "pool": amenity.get("pool", None),
#             "porter_service": amenity.get("porter_service", None),
#             "restaurant": amenity.get("restaurant", None),
#             "spa": amenity.get("spa", None),
#             "terrace": amenity.get("terrace", None),
#             "twenty_four_hr_reception": amenity.get("twenty_four_hr_reception", None),
#             "twenty_four_hr_room_service": amenity.get("twenty_four_hr_room_service", None),
#             "wheelchair_accessible": amenity.get("wheelchair_accessible", None),
#             "wifi_in_lobby": amenity.get("wifi_in_lobby", None)
#
#         }
#         amenity(**amenity_obj).save()
#         if hotel['images']:
#             for image in hotel['images']:
#                 image_obj = {
#                     "hotel_id": hotel_obj['id'],
#                     "image_url": image.get("image_url", None)
#                 }
#                 print(image_obj)
#                 Image(**image_obj).save()
#         if hotel['deals']:
#             for deal in hotel['deals']:
#                 website_dic = deal["website"]
#                 deal_obj = {
#                     "id": deal.get("id", None),
#                     "price": deal.get("price", None),
#                     "weekend": deal.get("weekend", None),
#                     "hotel_id": hotel_obj['id'],
#                     "website_id": website_dic.get("id", None)
#                 }
#                 if Website.query.filter_by(id=website_dic.get("id", None)).first() is None:
#                     website_obj = {
#                         "id": website_dic.get("id", None),
#                         "website": website_dic.get("website", None),
#                         "logo_image": website_dic.get("logo_image", None),
#                     }
#                     print(website_obj)
#                     Website(**website_obj).save()
#                 print(deal_obj)
#                 Deal(**deal_obj).save()
#
