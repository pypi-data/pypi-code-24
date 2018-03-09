import math

from django.conf import settings
from django.http import Http404

from .shortcuts import atoi


"""
Typical template example
===========================

Template example for paginator::

    {% if paginator.is_paginate %}
    <div class='paginator'>
        {% if paginator.get_prev_page %}
            <a href='?page={{ paginator.get_prev_page }}'>&laquo;</a>
        {% endif %}
        {% if paginator.get_prev_page_group %}
            <a href='?page={{ paginator.get_prev_page_group }}'>...</a>
        {% endif %}

        {% for page in paginator.get_bar %}
           {% ifequal page paginator.page %}
              <span>{{ page }}</span>
           {% else %}
              <a href='?page={{ page }}'>{{ page }}</a>
           {% endifequal %}
        {% endfor %}

        {% if paginator.get_next_page_group %}
            <a href='?page={{ paginator.get_next_page_group }}'>...</a>
        {% endif %}
        {% if paginator.get_next_page %}
            <a href='?page={{ paginator.get_next_page }}'>&raquo;</a>
        {% endif %}
    </div>
    {% endif %}


"""


class Paginator(object):
    """ Paginator tool

        For use ``Paginator`` need to pass into template context
        instance of ``Paginator`` object with full query_set and
        current page number.

        Optional argument ``row_per_page`` can be omitted, then object
        will look for ``ROW_PER_PAGE`` in project settings file.
    """

    def __init__(self, queryset, page=None, row_per_page=None, request=None, 
                 skip_startup_recalc=False):
        self._queryset = queryset
        self.request = request
        self._pages = None
        self.segment = None
        self._page = None
        self.row_per_page = row_per_page
        self._hits = 0

        if page is not None or request is not None and self.row_per_page != 'all':
            if not skip_startup_recalc:
                self.calc(page)

    def calc(self, page=None):
        if self.request and 'page' in self.request.GET and page is None:
            page = self.request.GET['page']
        self._page = atoi(page, 1)

        self.row_per_page = self.row_per_page or settings.PAGINATOR_PER_PAGE

        if isinstance(self._queryset, list):
            self._hits = len(self._queryset)
        else:
            self._hits = int(self._queryset.count())

        self._pages = int(math.ceil(float(self._hits)/float(self.row_per_page)))
        if not self._pages:
            self._pages = 1

        if self._page < 1 or self._page > self._pages:
            raise Http404

        self.segment = 5

    @property
    def page(self):
        if self._page is None:
            self.calc()
        return self._page

    @page.setter
    def page(self, value):
        self.calc(value)

    def get_start_url(self):
        url = '?'
        if self.request and self.request.GET:
            qset = self.request.GET.copy()
            if 'page' in qset:
                del qset['page']

            if len(qset) > 0:
                url += qset.urlencode()
                url += '&'

        return url

    def get_page_count(self):
        return self._pages

    def get_rows_count(self):
        return self._hits

    def get_offset(self):
        start = (self.page - 1) * atoi(self.row_per_page)
        end = self.page * atoi(self.row_per_page)
        return start, end

    def get_items(self):
        """ Return query set for current page """
        if self.row_per_page == 'all':
            return self._queryset

        start, end = self.get_offset()
        return self._queryset[start:end]

    def get_bar(self):
        """ Return list of page numbers for current segment """

        bar = []
        for page in range(self.page-self.segment, self.page+self.segment+1):
            if page <= 0 or page > self.get_page_count():
                continue

            bar.append(page)
        return bar

    def get_prev_page(self):
        if self.page - 1 <= 0:
            return None

        return self.page - 1

    def get_next_page(self):
        if self.page + 1 > self.get_page_count():
            return None

        return self.page + 1

    def get_prev_page_group(self):
        if self.page - self.segment*2 - 1 <= 0:
            return None
        return self.page - self.segment*2 - 1

    def get_prev_page_segment(self):
        if self.page - self.segment - 1 <= 0:
            return None
        return self.page - self.segment - 1

    def get_next_page_group(self):
        if self.page + self.segment*2 + 1 > self.get_page_count():
            return None
        return self.page + self.segment*2 + 1

    def get_next_page_segment(self):
        if self.page + self.segment + 1 > self.get_page_count():
            return None
        return self.page + self.segment + 1

    def get_last_page(self):
        return int(self.get_page_count())

    def is_paginate(self):
        return self.row_per_page != 'all' and self.get_page_count() > 1

    def set_page_by_position(self, position):
        self.page = int((position-1)/self.row_per_page)+1

    def set_inverted_page_by_position(self, position):
        """ set inverted paginator page

         Exampte: inverted paginator for 33 items:

         page4: 33..24
         page3: 23..14
         page2: 13..4
         page1: 3..1

        """
        page = None
        i = self.get_rows_count() + 1
        for p in range(1, self.get_page_count()+1):  # [1,2,3,4]
            i -= self.row_per_page
            if i <= position:
                page = p
                break
        self.page = page
