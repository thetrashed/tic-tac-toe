import pygame as pg
import random

import player
import board


def main():
    b = board.TTCBoard()
    human = player.Player(random.choice((-1, 1)), b)
    computer = player.Player(0 if human.getSymbol == 1 else 1, b)
    
    pg.init()

    screen = pg.display.set_mode((800, 600), pg.DOUBLEBUF)
    clock = pg.time.Clock()

    running = True
    while running:
        window_size = screen.get_size()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                human.updateBoard(mouse_pos, window_size[0], window_size[1])

        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            running = False

        screen.fill("black")
        b.drawBoard(screen, window_size[0], window_size[1])

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
