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
builder.add_from_file("/usr/share/turan/proqramlar/turan-welcome/turan-welcome.glade")

window = builder.get_object("window")
window.show_all()

stack = builder.get_object("pages")
desktop_session = os.environ.get("XDG_CURRENT_DESKTOP")
class Handler():

    def on_next(self, button):
        stack.set_visible_child_name("page1")

    def on_next1(self, button):
        stack.set_visible_child_name("page2")

    def on_next2(self, button):
        stack.set_visible_child_name("page3")

    def on_light_theme(self, button):
        if desktop_session == "XFCE":
          os.system('xfconf-query -c xsettings -p /Net/ThemeName -s "Fluent"')
          os.system('xfconf-query -c xsettings -p /Net/IconThemeName -s "Tela-circle"')
        elif desktop_session == "X-Cinnamon":
          os.system('gsettings set org.cinnamon.theme name Orchis-Light')
          os.system('gsettings set org.cinnamon.desktop.interface gtk-theme Orchis-Light')
          os.system('gsettings set org.cinnamon.desktop.interface icon-theme Tela-circle')

    def on_dark_theme(self, button):
        if desktop_session == "XFCE":
          os.system('xfconf-query -c xsettings -p /Net/ThemeName -s "Fluent-Dark"')
          os.system('xfconf-query -c xsettings -p /Net/IconThemeName -s "Tela-circle"')
        elif desktop_session == "X-Cinnamon":
          os.system('gsettings set org.cinnamon.theme name Orchis-Dark')
          os.system('gsettings set org.cinnamon.desktop.interface gtk-theme Orchis-Dark')
          os.system('gsettings set org.cinnamon.desktop.interface icon-theme Tela-circle')

    def on_about(self, button):
        os.system("turan-about")

    def on_exit(self, button):
        Gtk.main_quit()
        os.system("bash /usr/share/turan/proqramlar/turan-welcome/config.sh")

builder.connect_signals(Handler())
Gtk.main()
