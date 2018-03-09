# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.Status import Status


class SMSResponseDetails(DefaultObject):
    @property
    @serializable(name="to", type=unicode)
    def to(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is of type: unicode
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="status", type=Status)
    def status(self):
        """
        Property is of type: Status
        """
        return self.get_field_value("status")

    @status.setter
    def status(self, status):
        """
        Property is of type: Status
        """
        self.set_field_value("status", status)

    def set_status(self, status):
        self.status = status
        return self

    @property
    @serializable(name="smsCount", type=int)
    def sms_count(self):
        """
        Property is of type: int
        """
        return self.get_field_value("sms_count")

    @sms_count.setter
    def sms_count(self, sms_count):
        """
        Property is of type: int
        """
        self.set_field_value("sms_count", sms_count)

    def set_sms_count(self, sms_count):
        self.sms_count = sms_count
        return self

    @property
    @serializable(name="messageId", type=unicode)
    def message_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("message_id")

    @message_id.setter
    def message_id(self, message_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("message_id", message_id)

    def set_message_id(self, message_id):
        self.message_id = message_id
        return self