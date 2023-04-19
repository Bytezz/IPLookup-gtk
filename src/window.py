# window.py
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

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/github/bytezz/IPLookup/window.ui')
class IplookupWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'IplookupWindow'

    error_dialog = Gtk.Template.Child()

    ip_entry = Gtk.Template.Child()

    #search_btn = Gtk.Template.Child()

    network_label = Gtk.Template.Child()
    city_label = Gtk.Template.Child()
    country_label = Gtk.Template.Child()
    isp_label = Gtk.Template.Child()
    coordinates_label = Gtk.Template.Child()
    org_label = Gtk.Template.Child()
    region_label = Gtk.Template.Child()
    timezone_label = Gtk.Template.Child()
    zip_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ip_entry.grab_focus()
