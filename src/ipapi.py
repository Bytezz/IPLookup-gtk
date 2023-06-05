# ipapi.py
#
# Copyright 2023 Bytez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import sys
from urllib.request import urlopen
import socket

def internet_available():
    try:
        s = socket.create_connection(("1.1.1.1", 80), 2)
        s.close()
        return True
    except:
        return False

def is_ip(address):
    return not address.split(".")[-1].isalpha()

def get_ip_info(ip):
    ip = ip.strip()
    result = {}

    if ip != "":
        result = json.loads(urlopen("http://ip-api.com/json/{}".format(ip)).read())

    return result
