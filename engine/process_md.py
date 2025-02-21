#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This is a set of functions that work on Markdown file, before compiling them to html.

Go to page.py (Page) pre_process to add a new function from here."""

import re

import logging
logger = logging.getLogger('geekbook')
logger.setLevel(logging.INFO)


def right_MD_from_webservices(text):
    """ Just paste the url generated by Dropbox to convert it in a markdown img """
    changed = False
    for l in text.split('\n'):
        rx = re.compile('https://www.dropbox.com/(?P<img_id>.+)\?dl=0').search(l)
        rx2 = re.compile('(?<!.)http://g.recordit.co/(?P<rec_id>.+).gif(?!.)').search(l)
        if rx:
            text = re.sub(r'https://www.dropbox.com/(?P<img_id>.+)\?dl=0',
                          '![img](https://www.dropbox.com/' + rx.group('img_id') + '\?raw=1)', text)
            logger.info('dropbox link detected')
            changed = True
        if rx2:
            text = re.sub(r'(?<!.)http://g.recordit.co/(?P<rec_id>.+).gif(?!.)',
                          '![rec](http://g.recordit.co/' + rx2.group('rec_id') + '.gif)',
                          text)
            logger.info('Recordit link detected')
            changed = True
    return text, changed


def get_youtube_embeds_insert(text):
    ntext = ''
    changed = False
    for l in text.split('\n'):
        if l.strip().startswith('[yti:'):
            video_id = l.replace('[yti:', '').replace(']', '').strip()
            logger.info('youtube video detected: %s', video_id)
            l = '<iframe width="800" height="441" src="https://www.youtube.com/embed/' + \
                video_id + '" frameborder="0" allowfullscreen></iframe>' + \
                           '<https://www.youtube.com/watch?v=' + video_id + '>'
            changed = True
        ntext += l + '\n'
    return ntext, changed
