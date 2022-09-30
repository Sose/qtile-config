#!/usr/bin/env sh

# Make Caps Lock an additional Esc and both Shift Keys toggle Caps Lock
setxkbmap -option caps:escape,shift:both_capslock &

autorandr -c

feh --bg-scale /home/sose/.wallpapers/haskell.png

picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

dunst & disown

xfce4-power-manager & disown

nm-applet & disown

# polybar & disown # polybar? why not qtile's bar...

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
