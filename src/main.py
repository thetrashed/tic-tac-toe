import pygame as pg
import random

from board import TTCBoard
from bot import botMove
import player


def main():
    b = TTCBoard()
    human = player.Player(random.choice((-1, 1)), b)
    computer = player.Player(-1 if human.getSymbol() == 1 else 1, b)

    if human.getSymbol() == 1:
        player_turn = True
    else:
        player_turn = False

    pg.init()
    screen = pg.display.set_mode((800, 600), pg.DOUBLEBUF | pg.RESIZABLE)
    clock = pg.time.Clock()

    running = True
    while running:
        window_size = screen.get_size()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if player_turn:
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    human.updateBoard(mouse_pos, window_size[0], window_size[1])
                    player_turn = not player_turn
            else:
                botMove(b, computer)
                player_turn = not player_turn

        if b.checkGameEnd():
            running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            running = False

        screen.fill("black")
        b.drawBoard(screen, window_size[0], window_size[1])

        pg.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
