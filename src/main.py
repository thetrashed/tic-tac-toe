import pygame as pg
import random

from board import TTCBoard
import bot
import player


def openingMenu(screen, window_size):
    font = pg.font.Font(None, 50)
    welcome_text = font.render("Welcome to Tic-Tac-Toe", True, "gray")

    opening_text_rect = welcome_text.get_rect(
        center=(window_size[0] / 2, window_size[1] / 2 - 60)
    )
    screen.blit(welcome_text, opening_text_rect)

    instructions_text = font.render('Press "Space" to Play', True, "gray")
    instruction_text_rect = instructions_text.get_rect(
        center=(window_size[0] / 2, window_size[1] / 2 + 60)
    )
    screen.blit(instructions_text, instruction_text_rect)


def closingMenu(screen, window_size, winner_symbol, player):
    if player.getSymbol() == winner_symbol:
        txt = "You Won!"
    elif winner_symbol == 0:
        txt = "It Was a Draw"
    else:
        txt = "You Lost :("

    font = pg.font.Font(None, 50)
    closing_text = font.render(txt, True, "gray")
    text_rect = closing_text.get_rect(
        center=(window_size[0] / 2, window_size[1] / 2 - 60)
    )
    screen.blit(closing_text, text_rect)

    instructions_text = font.render(
        'Press "q" to Exit and "r" to Play Again', True, "gray"
    )
    instruction_text_rect = instructions_text.get_rect(
        center=(window_size[0] / 2, window_size[1] / 2 + 60)
    )
    screen.blit(instructions_text, instruction_text_rect)


def main():
    b = TTCBoard()
    player1 = player.Player(random.choice((-1, 1)), b)
    # player1 = bot.RandomBot(b, random.choice((-1, 1)))
    player2 = bot.MiniMaxBot(b, -1 if player1.getSymbol() == 1 else 1)

    if player1.getSymbol() == 1:
        player1_turn = True
    else:
        player1_turn = False

    pg.init()
    opening_menu_enabled = True
    closing_menu_enabled = False
    screen = pg.display.set_mode((800, 600), pg.DOUBLEBUF | pg.RESIZABLE)
    clock = pg.time.Clock()

    running = True
    while running:
        window_size = screen.get_size()
        if not player1_turn and not closing_menu_enabled and not opening_menu_enabled:
            font = pg.font.Font(None, 50)
            wait_text = font.render("AI making a move", True, "gray")
            text_rect = wait_text.get_rect(
                center=(window_size[0] / 2, window_size[1] / 2)
            )
            b.drawBoard(screen, window_size[0], window_size[1])
            screen.blit(wait_text, text_rect)
            pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if player1_turn and not opening_menu_enabled and not closing_menu_enabled:
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    player1.move(mouse_pos, window_size[0], window_size[1])
                    player1_turn = not player1_turn
            elif not opening_menu_enabled and not closing_menu_enabled:
                player2.move()
                player1_turn = not player1_turn

        if (winner := b.hasWinner()) != 0 or b.boardFull():
            closing_menu_enabled = True

        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            running = False
        elif keys[pg.K_SPACE] and opening_menu_enabled:
            opening_menu_enabled = False
        elif keys[pg.K_r] and closing_menu_enabled:
            b.reset()
            player1_turn = random.choice([True, False])
            closing_menu_enabled = False

        screen.fill("black")
        if opening_menu_enabled:
            openingMenu(screen, window_size)
        elif closing_menu_enabled:
            closingMenu(screen, window_size, winner, player1)
        else:
            b.drawBoard(screen, window_size[0], window_size[1])

        pg.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
