#!/usr/bin/env python3

import gi
import os
import locale
import requests
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gio
from locale import gettext as tr

# Tərcümə məlumatları
APPNAME = "turan-welcome"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Tərcümə funksiyaları
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)

# GTK Builder
builder = Gtk.Builder()
builder.set_translation_domain(APPNAME)
builder.add_from_file("/usr/share/turan/proqramlar/turan-welcome/welcome.glade")

window = builder.get_object("window")
window.show_all()

command = "echo $(lsb_release -sr)"
out = subprocess.check_output(command, shell=True)
versiya_label = builder.get_object("versiya")
class Handler():
    versiya_label.set_label(out.decode())
    def on_exit(self, button):
        Gtk.main_quit()

builder.connect_signals(Handler())
Gtk.main()