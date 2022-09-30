from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

colors = {
    "bg": '#282828',
    "bg2": '#1d2021',
    "red": '#cc241d',
    "green": '#a9b665',
    "yellow": '#FABD2F',
    "blue": '#7daea3',
    "purple": '#d3869b',
    "aqua": '#689d6a',
    "orange": '#d65d0e',
    "white": '#fbf1c7',
    "gray": '#a89984',
    "dark_gray": '#665c54',
}

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=6,
    foreground=colors["bg"],
)

extension_defaults = widget_defaults.copy()


def powerline_left(fg=colors["red"], bg=colors["bg2"]):
    return widget.TextBox(
        foreground=fg,
        background=bg,
        fontsize=18,
        text="",
        padding=-1,
    )


def powerline_right(fg=colors["red"], bg=colors["bg2"]):
    return widget.TextBox(
        foreground=fg,
        background=bg,
        fontsize=18,
        text="",
        padding=-1
    )


def separate():
    return widget.Sep(
        linewidth=0,
        padding=10,
        size_percent=50,
    )


def mywrapper(element, fg=colors["red"], bg=colors["bg"]):
    return [
        powerline_left(fg, bg),
        element,
        powerline_right(fg, bg),
        separate(),
    ]


screens = [Screen(
    top=bar.Bar(
        [separate()]
        + mywrapper(widget.GroupBox(
            borderwidth=0,
            highlight_method='block',
            block_highlight_text_color=colors["blue"],
            background=colors["green"]
        ), colors["green"])
        + mywrapper(widget.CurrentLayout(background=colors["yellow"]), colors["yellow"])
        + [widget.Prompt()]
        + mywrapper(widget.TaskList(
            max_title_width=200,
            highlight_method='block',
            border=colors["blue"],
            #fontsize = 10,
            padding_y=2,  # seems off-center without
            padding_x=3,
            background=colors["white"],
        ), colors["white"])
        + [widget.Notify()]
        + mywrapper(widget.Volume(
            fmt='墳 {}',
            mouse_callbacks={"Button3": lazy.spawn("pavucontrol")},
            background=colors["blue"],
        ), colors["blue"])
        + mywrapper(widget.Memory(fmt='{}',
                    background=colors["purple"]), colors["purple"])
        + mywrapper(widget.Battery(
            fmt='  {}',
            update_delay=5,
            background=colors["green"],
            mouse_callbacks={
                "Button1": lazy.spawn("xfce4-power-manager-settings"),
                "Button3": lazy.spawn("xfce4-power-manager-settings"),
            }), colors["green"])
        + mywrapper(widget.Systray(background=colors["orange"]), colors["orange"])
        + mywrapper(widget.Clock(
            format='%d.%m. %H:%M',
            mouse_callbacks={"Button1": lazy.spawn("gsimplecal"), },
            background=colors["aqua"],
        ), colors["aqua"]), 24, background=[colors["bg2"]]))]
