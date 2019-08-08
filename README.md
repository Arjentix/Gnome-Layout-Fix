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

## Attention

Then after running this program I tried to logging out and logging in again I met a new problem – I couldn't logging in cause the layout was different than my password language.  So if you faces with this problem – run another *OS* on your machine (e.g. *live* session) and modify order of layouts in the */etc/default/keyboard* file. After doing that the problem was gone.

