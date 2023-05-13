# main.py
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

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import IplookupWindow

from . import ipapi

class IplookupApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='io.github.bytezz.IPLookup',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.on_quit_action, ['<primary>q'])
        self.create_action('about', self.on_about_action)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        self.win = self.props.active_window
        if not self.win:
            self.win = IplookupWindow(application=self)
        self.win.present()

        self.win.ip_entry.connect("apply", self.on_search)
        #self.win.search_btn.connect("clicked", self.on_search)

    def on_quit_action(self, widget, _):
        self.quit()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='IP Lookup',
                                application_icon='io.github.bytezz.IPLookup',
                                developer_name='Bytez',
                                version='0.1.1',
                                developers=['Bytez'],
                                copyright='© 2023 Bytez')
        about.present()

    def on_search(self, widget):
        # TODO: Call deferred
        # TODO: Show an osd GtkProgressBar
        if self.win.ip_entry.get_text().strip() != "":
            if ipapi.internet_available():
                ipinfo = ipapi.get_ip_info(self.win.ip_entry.get_text())

                if ipinfo != {} and ipinfo["status"] == "success":
                    self.win.network_label.set_label(ipinfo["as"])
                    self.win.isp_label.set_label(ipinfo["isp"])
                    self.win.org_label.set_label(ipinfo["org"])

                    self.win.city_label.set_label(ipinfo["city"])
                    self.win.region_label.set_label(ipinfo["regionName"]+", "+ipinfo["region"])
                    self.win.country_label.set_label(ipinfo["country"]+", "+ipinfo["countryCode"])
                    self.win.zip_label.set_label(ipinfo["zip"])
                    self.win.timezone_label.set_label(ipinfo["timezone"])
                    self.win.coordinates_label.set_label(str(ipinfo["lat"])+", "+str(ipinfo["lon"]))
                    self.win.coordinates_label.set_uri("geo://"+str(ipinfo["lat"])+","+str(ipinfo["lon"]))
                    self.win.coordinates_label.set_visible(True)
                elif "message" in ipinfo:
                    # TODO: Repleace with a toast
                    self.win.error_dialog.set_body(ipinfo["message"].capitalize()+".")
                    self.win.error_dialog.present()
            else:
                # TODO: Repleace with a banner
                self.win.error_dialog.set_body("No internet connection available.")
                self.win.error_dialog.present()

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = IplookupApplication()
    return app.run(sys.argv)

