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
SESSION_NAME = getenv("SESSION_NAME", "AQCN3FDdFWGi79VohQkPJWU9Nu6A6W9tdJvjDxGdvtH-YSZqNcb2D7vZiLX2S67Z-UYQRrs7glatqouFloTQyGeajwMwPn8-O1QnfdJRw7Cm96jdmKscimHT6gDvuxdWvkiH9u7753bwREv5V38bUIPFzd4hf3fBdvQVvbYIsBkUQV8IT_CpHupYj2cPXglMoPnH25zWDtFHug71p6mrw3BddS-fcmtxpCqdULvaju9KoDejW36ST6fRD6iGiTAj-gFXhYGo26Yw8v7fQESW9J9fLjAzzQYxAL7yUmGlnvyfSQIu_7hHUJxWLi66RvyCVXDcBuBvSc_AF-o-KIBpmpFRY1PwDwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1613196478:AAFXf2pnYrjW8yDOkKlWaIJg0Jtg2dkHNN8")
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
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! *").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
