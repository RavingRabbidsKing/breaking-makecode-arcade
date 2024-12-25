basic.show_number(0)
basic.show_leds("""
    . # . # .
    . . . . .
    # # # # #
    . . . . .
    . . # . .
    """)
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
