import pygame as pg
import random

from board import TTCBoard
import bot
import player


def main():
    b = TTCBoard()
    player1 = player.Player(random.choice((-1, 1)), b)
    # player1 = bot.RandomBot(b, random.choice((-1, 1)))
    player2 = bot.OneLayerBot(b, -1 if player1.getSymbol() == 1 else 1)

    if player1.getSymbol() == 1:
        player1_turn = True
    else:
        player1_turn = False

    pg.init()
    screen = pg.display.set_mode((800, 600), pg.DOUBLEBUF | pg.RESIZABLE)
    clock = pg.time.Clock()

    running = True
    while running:
        window_size = screen.get_size()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if player1_turn:
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    player1.move(mouse_pos, window_size[0], window_size[1])
                    player1_turn = not player1_turn
                # player1.move()
                # player1_turn = not player1_turn
            else:
                player2.move()
                player1_turn = not player1_turn

        if b.hasWinner():
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
