from libqtile.widget import backlight


widget.Backlight(

    backlight_name="intel_backlight",

fmt="brightness : {}",

step=5,

change_command="light -S {0}")