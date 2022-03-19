#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os

class Config(object):
    LOGGER = True
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    Channel_Stor = os.environ.get("Channel_Stor",None)
    Time_Sleep = int(os.environ.get("Time_Sleep",2))
    Session_string = os.environ.get("Session_string",None)
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
