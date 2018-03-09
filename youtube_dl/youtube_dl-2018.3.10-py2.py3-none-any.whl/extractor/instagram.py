from __future__ import unicode_literals

import itertools
import re

from .common import InfoExtractor
from ..compat import compat_str
from ..utils import (
    get_element_by_attribute,
    int_or_none,
    lowercase_escape,
    try_get,
)


class InstagramIE(InfoExtractor):
    _VALID_URL = r'(?P<url>https?://(?:www\.)?instagram\.com/p/(?P<id>[^/?#&]+))'
    _TESTS = [{
        'url': 'https://instagram.com/p/aye83DjauH/?foo=bar#abc',
        'md5': '0d2da106a9d2631273e192b372806516',
        'info_dict': {
            'id': 'aye83DjauH',
            'ext': 'mp4',
            'title': 'Video by naomipq',
            'description': 'md5:1f17f0ab29bd6fe2bfad705f58de3cb8',
            'thumbnail': r're:^https?://.*\.jpg',
            'timestamp': 1371748545,
            'upload_date': '20130620',
            'uploader_id': 'naomipq',
            'uploader': 'Naomi Leonor Phan-Quang',
            'like_count': int,
            'comment_count': int,
            'comments': list,
        },
    }, {
        # missing description
        'url': 'https://www.instagram.com/p/BA-pQFBG8HZ/?taken-by=britneyspears',
        'info_dict': {
            'id': 'BA-pQFBG8HZ',
            'ext': 'mp4',
            'title': 'Video by britneyspears',
            'thumbnail': r're:^https?://.*\.jpg',
            'timestamp': 1453760977,
            'upload_date': '20160125',
            'uploader_id': 'britneyspears',
            'uploader': 'Britney Spears',
            'like_count': int,
            'comment_count': int,
            'comments': list,
        },
        'params': {
            'skip_download': True,
        },
    }, {
        # multi video post
        'url': 'https://www.instagram.com/p/BQ0eAlwhDrw/',
        'playlist': [{
            'info_dict': {
                'id': 'BQ0dSaohpPW',
                'ext': 'mp4',
                'title': 'Video 1',
            },
        }, {
            'info_dict': {
                'id': 'BQ0dTpOhuHT',
                'ext': 'mp4',
                'title': 'Video 2',
            },
        }, {
            'info_dict': {
                'id': 'BQ0dT7RBFeF',
                'ext': 'mp4',
                'title': 'Video 3',
            },
        }],
        'info_dict': {
            'id': 'BQ0eAlwhDrw',
            'title': 'Post by instagram',
            'description': 'md5:0f9203fc6a2ce4d228da5754bcf54957',
        },
    }, {
        'url': 'https://instagram.com/p/-Cmh1cukG2/',
        'only_matching': True,
    }, {
        'url': 'http://instagram.com/p/9o6LshA7zy/embed/',
        'only_matching': True,
    }]

    @staticmethod
    def _extract_embed_url(webpage):
        mobj = re.search(
            r'<iframe[^>]+src=(["\'])(?P<url>(?:https?:)?//(?:www\.)?instagram\.com/p/[^/]+/embed.*?)\1',
            webpage)
        if mobj:
            return mobj.group('url')

        blockquote_el = get_element_by_attribute(
            'class', 'instagram-media', webpage)
        if blockquote_el is None:
            return

        mobj = re.search(
            r'<a[^>]+href=([\'"])(?P<link>[^\'"]+)\1', blockquote_el)
        if mobj:
            return mobj.group('link')

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')
        url = mobj.group('url')

        webpage = self._download_webpage(url, video_id)

        (video_url, description, thumbnail, timestamp, uploader,
         uploader_id, like_count, comment_count, comments, height,
         width) = [None] * 11

        shared_data = self._parse_json(
            self._search_regex(
                r'window\._sharedData\s*=\s*({.+?});',
                webpage, 'shared data', default='{}'),
            video_id, fatal=False)
        if shared_data:
            media = try_get(
                shared_data,
                (lambda x: x['entry_data']['PostPage'][0]['graphql']['shortcode_media'],
                 lambda x: x['entry_data']['PostPage'][0]['media']),
                dict)
            if media:
                video_url = media.get('video_url')
                height = int_or_none(media.get('dimensions', {}).get('height'))
                width = int_or_none(media.get('dimensions', {}).get('width'))
                description = try_get(
                    media, lambda x: x['edge_media_to_caption']['edges'][0]['node']['text'],
                    compat_str) or media.get('caption')
                thumbnail = media.get('display_src')
                timestamp = int_or_none(media.get('taken_at_timestamp') or media.get('date'))
                uploader = media.get('owner', {}).get('full_name')
                uploader_id = media.get('owner', {}).get('username')

                def get_count(key, kind):
                    return int_or_none(try_get(
                        media, (lambda x: x['edge_media_%s' % key]['count'],
                                lambda x: x['%ss' % kind]['count'])))
                like_count = get_count('preview_like', 'like')
                comment_count = get_count('to_comment', 'comment')

                comments = [{
                    'author': comment.get('user', {}).get('username'),
                    'author_id': comment.get('user', {}).get('id'),
                    'id': comment.get('id'),
                    'text': comment.get('text'),
                    'timestamp': int_or_none(comment.get('created_at')),
                } for comment in media.get(
                    'comments', {}).get('nodes', []) if comment.get('text')]
                if not video_url:
                    edges = try_get(
                        media, lambda x: x['edge_sidecar_to_children']['edges'],
                        list) or []
                    if edges:
                        entries = []
                        for edge_num, edge in enumerate(edges, start=1):
                            node = try_get(edge, lambda x: x['node'], dict)
                            if not node:
                                continue
                            node_video_url = try_get(node, lambda x: x['video_url'], compat_str)
                            if not node_video_url:
                                continue
                            entries.append({
                                'id': node.get('shortcode') or node['id'],
                                'title': 'Video %d' % edge_num,
                                'url': node_video_url,
                                'thumbnail': node.get('display_url'),
                                'width': int_or_none(try_get(node, lambda x: x['dimensions']['width'])),
                                'height': int_or_none(try_get(node, lambda x: x['dimensions']['height'])),
                                'view_count': int_or_none(node.get('video_view_count')),
                            })
                        return self.playlist_result(
                            entries, video_id,
                            'Post by %s' % uploader_id if uploader_id else None,
                            description)

        if not video_url:
            video_url = self._og_search_video_url(webpage, secure=False)

        formats = [{
            'url': video_url,
            'width': width,
            'height': height,
        }]

        if not uploader_id:
            uploader_id = self._search_regex(
                r'"owner"\s*:\s*{\s*"username"\s*:\s*"(.+?)"',
                webpage, 'uploader id', fatal=False)

        if not description:
            description = self._search_regex(
                r'"caption"\s*:\s*"(.+?)"', webpage, 'description', default=None)
            if description is not None:
                description = lowercase_escape(description)

        if not thumbnail:
            thumbnail = self._og_search_thumbnail(webpage)

        return {
            'id': video_id,
            'formats': formats,
            'ext': 'mp4',
            'title': 'Video by %s' % uploader_id,
            'description': description,
            'thumbnail': thumbnail,
            'timestamp': timestamp,
            'uploader_id': uploader_id,
            'uploader': uploader,
            'like_count': like_count,
            'comment_count': comment_count,
            'comments': comments,
        }


class InstagramUserIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?instagram\.com/(?P<id>[^/]{2,})/?(?:$|[?#])'
    IE_DESC = 'Instagram user profile'
    IE_NAME = 'instagram:user'
    _TEST = {
        'url': 'https://instagram.com/porsche',
        'info_dict': {
            'id': 'porsche',
            'title': 'porsche',
        },
        'playlist_count': 5,
        'params': {
            'extract_flat': True,
            'skip_download': True,
            'playlistend': 5,
        }
    }

    def _entries(self, uploader_id):
        query = {
            '__a': 1,
        }

        def get_count(kind):
            return int_or_none(try_get(
                node, lambda x: x['%ss' % kind]['count']))

        for page_num in itertools.count(1):
            page = self._download_json(
                'https://instagram.com/%s/' % uploader_id, uploader_id,
                note='Downloading page %d' % page_num,
                fatal=False, query=query)
            if not page:
                break

            nodes = try_get(page, lambda x: x['user']['media']['nodes'], list)
            if not nodes:
                break

            max_id = None

            for node in nodes:
                node_id = node.get('id')
                if node_id:
                    max_id = node_id

                if node.get('__typename') != 'GraphVideo' and node.get('is_video') is not True:
                    continue
                video_id = node.get('code')
                if not video_id:
                    continue

                info = self.url_result(
                    'https://instagram.com/p/%s/' % video_id,
                    ie=InstagramIE.ie_key(), video_id=video_id)

                description = try_get(
                    node, [lambda x: x['caption'], lambda x: x['text']['id']],
                    compat_str)
                thumbnail = node.get('thumbnail_src') or node.get('display_src')
                timestamp = int_or_none(node.get('date'))

                comment_count = get_count('comment')
                like_count = get_count('like')
                view_count = int_or_none(node.get('video_views'))

                info.update({
                    'description': description,
                    'thumbnail': thumbnail,
                    'timestamp': timestamp,
                    'comment_count': comment_count,
                    'like_count': like_count,
                    'view_count': view_count,
                })

                yield info

            if not max_id:
                break

            query['max_id'] = max_id

    def _real_extract(self, url):
        uploader_id = self._match_id(url)
        return self.playlist_result(
            self._entries(uploader_id), uploader_id, uploader_id)
