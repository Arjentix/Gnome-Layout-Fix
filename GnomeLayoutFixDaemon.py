#! /usr/bin/env python

'''
Author: Polyakov Daniil
Mail: arjentix@gmail.com
Github: Arjentix
Date: 06.08.19
'''

import sys
import os
import dbus
import glib
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

# Function that handles layout swithing and making fixes
def signal_handler(*args, **kwargs):
	if args[0] == '/org/gnome/desktop/input-sources/mru-sources':
		get_mru_sources = 'gsettings get org.gnome.desktop.input-sources mru-sources'
		set_sources = 'gsettings set org.gnome.desktop.input-sources sources'

		# Getting most recently used sources
		mru_sources = subprocess.check_output(get_mru_sources.split())

		# Setting argument
		call_args = set_sources.split()
		call_args.append(mru_sources.rstrip('\n'))

		# Setting sources
		subprocess.call(call_args)

# Main loop that listens to layout swithing event
if __name__ == '__main__':
	# Running as daemon
	pid = os.fork()
	if pid > 0:
		sys.exit(0)
	
	DBusGMainLoop(set_as_default=True)

	session_bus = dbus.SessionBus()
	session_bus.add_signal_receiver(handler_function=signal_handler,
									dbus_interface='ca.desrt.dconf.Writer')

	mainloop = glib.MainLoop()
	mainloop.run()
