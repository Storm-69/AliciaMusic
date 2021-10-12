# AliciaMusic- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAv_Kqp7hmAoVovRRfLR8ijCeEcBf-u8yQYjgef9ElKv2cEO2hx5IOBg2lp5XsoV3wRChbe4ZNLlt_dHW9g_8YNTeJYg8QRLNAp1NW0iHpLjKYeH4eKmy26aLhBotRIFZemfE5gAZ3ZjOU1nyg-Nn5_sMNZOv0w-uusshRfD5qjMaCoswMMmqyXS6aA8z6SqSupmWR1pkI6mpHVxkPTKtetHUEfyhtc5AaDzkKOKk61n6zzD8mpBsx8Wj2KbsYcyWM_poIz1vj25nktj2qG9NIQ8WaXPKnz7d3_nMDOFIjXEezZZIk4a4cWwDxCWQKI6ais24dje49NR0WTg8BXTsLmcAiVAwA")
BOT_TOKEN = getenv("BOT_TOKEN", "2035708565:AAH8L6b2fB09IjJ_lb1v0vEvXzWaw6Wu0Hc")
BOT_NAME = getenv("BOT_NAME", "Alicia MusicBot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MafiaBot_Support")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c81a1be4c5aa4c7b009b7.jpg")
admins = {}
API_ID = int(getenv("API_ID", 7953443))
API_HASH = getenv("API_HASH", "04f1d039abcea1b7a9abcf976863d315")
BOT_USERNAME = getenv("BOT_USERNAME", "AliciaGroup_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Alicia Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "MafiaBot_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "AliciaMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/H1M4N5HU0P/AliciaMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "DSCCEX-RQCOQV-RPBVBD-RAZLFC-ARQ")
PMPERMIT = getenv("PMPERMIT", "https://telegra.ph/file/c81a1be4c5aa4c7b009b7.jpg")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", 1879610627 1212368262 1995334187).split()))
