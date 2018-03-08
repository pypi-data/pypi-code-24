# -*- coding: utf-8 -*-

from ming import schema as s
from ming.odm import FieldProperty, RelationProperty, ForeignIdProperty
from ming.odm.declarative import MappedClass
from googleplusauth.model import DBSession


class GoogleAuth(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'googleplusauth_info'
        indexes = [(('_user_id', ), )]

    _id = FieldProperty(s.ObjectId)
    registered = FieldProperty(s.Bool, if_missing=False)
    just_connected = FieldProperty(s.Bool, if_missing=False)
    profile_picture = FieldProperty(s.String)

    _user_id = ForeignIdProperty('User')
    user = RelationProperty('User')

    google_id = FieldProperty(s.String, required=True)
    access_token = FieldProperty(s.String, required=True)
    access_token_expiry = FieldProperty(s.DateTime, required=True)

    @classmethod
    def ga_user_by_google_id(cls, google_id):
        google_auth_user = cls.query.find({'google_id': google_id}).first()
        return google_auth_user

    @classmethod
    def googleplusauth_user(cls, user_id):
        return cls.query.find({'_user_id': user_id}).first()
