# Gnome Layout Fix

This simple program fixes Gnome problem with layout: some programs like *xbindkeys* won't work with nonstandard keyboard layout, cause *Xlib API* returns wrong button state.

It's a **workaround**, not a proper fix.

## How does it work

This program runs as a daemon and listens for *keyboard layout switching event*. Then the event was received program just sets value of *mru-sources* in *sources* (see *org.gnome.desktop.input-sources* item in *dconf-editor*).

I don't know exactly why does this setting's manipulation fixes that problem, but it works for me.

# How to run

Launch it like this from the repository directory:

```bash
./GnomeLayoutFixDaemon.py
```

I'm recommending to move it in the autostart (don't forget to type full path to the program).

