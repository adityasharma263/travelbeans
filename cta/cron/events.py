# # -*- coding: utf-8 -*-
# __author__ = 'hmharshit'
# import hashlib
# from random import sample
#
# import facebook
# from flask_script import Command
# from slugify import slugify
#
# from tdgtrends import app, logging
# from tdgtrends.constants.events import EVENTS_SEARCH_KEYWORDS
# from tdgtrends.models.events import Event, EventOwner, EventMedia, EventFeed, FlickRImage
# from tdgtrends.models.organizer import Organizer
# from tdgtrends.lib.sendmail import SendEmail
# from tdgtrends.lib.flickr import FlickrImage
# from tdgtrends.lib.events import FindPaid
#
#
# class EventsFetch(Command):
#     def run(self):
#         resp = {}
#         _events = []
#         try:
#             api = facebook.GraphAPI(app.config["FACEBOOK_ACCESS_TOKEN"])
#             for event in EVENTS_SEARCH_KEYWORDS:
#                 logging.info(event['name'])
#                 response = api.request(
#                     'search?q={}&type=event&limit={}&fields=id,attending_count,can_guests_invite,can_viewer_post,'
#                     'category,cover,declined_count,description,end_time,event_times,guest_list_enabled,interested_count,'
#                     'is_canceled,is_draft,is_page_owned,is_viewer_admin,maybe_count,name,noreply_count,owner,'
#                     'parent_group,place,start_time,ticket_uri,ticketing_privacy_uri,ticketing_terms_uri,updated_time,'
#                     'feed,picture,photos'.format(event.get("name"), event.get("limit")))
#                 for result in response.get("data"):
#                     try:
#                         resp = {
#                             "name": result.get("name"),
#                             "event_id": result.get("id"),
#                             "description": result.get("description"),
#                             "start_time": result.get("start_time"),
#                             "end_time": result.get("end_time"),
#                             "priority": False,
#                             "hash": hashlib.md5(result.get("name").encode('utf-8')).hexdigest(),
#                             "interested_rate": result.get("interested_count"),
#                             "going_rate": result.get("attending_count"),
#                             "is_booking": None,
#                             "url": result.get("cover").get("source"),
#                             "owner_name": result.get("owner").get("name"),
#                             "owner_url": result.get("owner").get("id"),
#                             "street": result.get("place").get("location").get("street"),
#                             "zip": result.get("place").get("location").get("zip"),
#                             "city": result.get("place").get("location").get("city"),
#                             "country": result.get("place").get("location").get("country"),
#                             "latitude": result.get("place").get("location").get("latitude"),
#                             "longitude": result.get("place").get("location").get("longitude")
#                         }
#                     except Exception as e:
#                         pass
#
#                     _events.append(resp)
#
#             for response in sample(_events, len(_events) - 1):
#                 events = Event.query.filter_by(event_id=response['event_id']).first()
#                 if not events:
#                     organizer_detail = self.organizer(response.get("owner_url"))
#                     event_owner = EventOwner(name=response.get("owner_name"), url=response.get("owner_url"),
#                                              email=organizer_detail.get("emails"),
#                                              about=organizer_detail.get("about"),
#                                              phone_number=organizer_detail.get("phone"))
#                     EventOwner.save(event_owner)
#                     response["organizer_id"] = EventOwner.id
#                     events = Event(**response)
#                     Event.save(events)
#                     FindPaid().ispaid(events)
#                     SendEmail().send_email()
#
#                     event_media = EventMedia(url=response.get("url"), event_id=events.id)
#                     EventMedia.save(event_media)
#
#             FetchEventsFeed().run()
#
#         except Exception as e:
#             logging.exception(e)
#
#     def organizer(self, owner_url):
#         try:
#             api = facebook.GraphAPI(app.config["FACEBOOK_ACCESS_TOKEN"])
#             organizer_details = api.request('{}?fields=id,name,about,emails,phone'.format(owner_url))
#             return organizer_details
#
#         except Exception as e:
#             logging.exception(e)
#
#
# class FetchEventsFeed(Command):
#     def run(self):
#         try:
#             events = Event.query.all()
#             for event in events:
#                 logging.info(event.slug)
#                 api = facebook.GraphAPI(app.config["FACEBOOK_ACCESS_TOKEN"])
#                 feeds = api.request('{}?fields=feed'.format(event.event_id))
#                 try:
#                     for feed in feeds.get('feed').get('data'):
#                         event_feed = EventFeed.query.filter_by(feed_id=feed.get("id")).first()
#                         if not event_feed:
#                             event_feed = EventFeed(message=feed.get("message"), event_id=event.id,
#                                                    feed_id=feed.get("id"), update_time=feed.get("update_time"))
#                             EventFeed.save(event_feed)
#
#                 except:
#                     logging.info("event does not have any feeds\n")
#
#         except Exception as e:
#             logging.exception(e)
#
#
# class PhotoFlickr(Command):
#     def run(self):
#         try:
#             events = Event.query.all()
#             per_page = 10
#             keyword_id = 1
#             for event in events:
#                 photo_list = FlickrImage().search(text=event.slug, per_page=per_page, keyword_id=keyword_id)
#                 try:
#                     for image in photo_list:
#                         event_image = FlickRImage.query.filter_by(image_id=image.get('image_id')).first()
#                         if not event_image:
#                             event_image = FlickRImage(url=image['url'], event_id=event.id, image_id=image['image_id'])
#                             FlickRImage.save(event_image)
#                 except Exception as e:
#                     import traceback
#                     print(traceback.print_exc())
#                     logging.info("event has no photos")
#
#         except Exception as e:
#             logging.exception(e)
