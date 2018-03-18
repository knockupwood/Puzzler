import tcod
from consts import *
from handle_input import *
from unit import *
from message_console import *


def main():

    key = tcod.Key()
    mouse = tcod.Mouse()

    running = True
    while not tcod.console_is_window_closed() and running:

        Player.draw(con)
        tcod.console_blit(con, 0, 0, SCREEN_X + 1, SCREEN_Y, 0, 0, 0)
        tcod.console_flush()
        Player.clear(con)

        MesCon.update_archive(Player.get_message())
        MesCon.draw()
        MesCon.blit(con)
        MesCon.clear()

        tcod.sys_wait_for_event(tcod.EVENT_KEY_PRESS, key, mouse, True)
        action = handle_keys(key)
        move = action.get("move")
        escape = action.get("exit")

        if move:
            Player.move(move)
        if escape:
            running = False
        # TODO: use handle_keys and dictionaries to parse and perform actions


if __name__ == "__main__":
    tcod.console_set_custom_font(FONT_PATH, tcod.FONT_LAYOUT_ASCII_INROW | tcod.FONT_TYPE_GRAYSCALE)
    tcod.console_init_root(SCREEN_X, SCREEN_Y, GAME_TITLE, fullscreen=True)

    con = tcod.console_new(SCREEN_X, SCREEN_Y)
    tcod.console_set_default_foreground(0, tcod.white)

    MesCon = MessageConsole(SCREEN_X, SCREEN_Y)

    Player = Unit(CENTER_X, CENTER_Y, T_PLAYER)

    main()


