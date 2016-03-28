#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GreekGetter(object):
    '''
    A simple localizer a la gettext.
    '''

    def __init__(self):
        self.translator = dict(dog='Sparky', cat='Tom')

    # We will punt if we dont have a translation.
    def get(self, message_id):
        return self.translator.get(message_id, str(message_id))

class EnglishGetter(object):
    '''
    Simple echoes the message ids.
    '''

    def get(self, message_id):
        return str(message_id)

def get_localizer(language='English'):
    '''
    The factory method.
    '''

    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

# Create our localizers:
e, g = get_localizer(language='English'), get_localizer(language='Greek')

# Localize some text:
for msg_id in 'dog parrot cat bear'.split():
    print e.get(msg_id), g.get(msg_id)