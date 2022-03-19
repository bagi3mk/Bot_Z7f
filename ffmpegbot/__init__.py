#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Khamis S

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from ffmpegbot.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
Channel_Stor = Config.Channel_Stor
Time_Sleep = Config.Time_Sleep
Session_string = Config.Session_string

