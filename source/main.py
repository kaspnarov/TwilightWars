import pygame
from pygame.locals import *
import board
import states

# Set initial PyGame variables
W_SIZE = W_WIDTH, W_HEIGHT = (1000, 1000)

pygame.init()

screen = pygame.display.set_mode(W_SIZE)
screen.fill((220, 120, 0))

pygame.display.set_caption("Twilight Wars")
icon = pygame.image.load("src/img/logo.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("src/sound/music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
click_sfx = pygame.mixer.Sound("src/sound/click.wav")
click_sfx.set_volume(0.5)

# States constants
MENU = 0
GAME = 1
RULES = 2
PAUSE = 3
VERSUS = 4
ENDGAME = 5
CHOOSETEAM = 6
ENEMYPLAY = 7
CREATECOMP = 8

# Game States
game_state = MENU
MAIN_MENU = states.State(MENU)
RULES_SCREEN = states.State(RULES)
PAUSE_SCREEN = states.State(PAUSE)
VERSUS_SCREEN = states.State(VERSUS)
ENDGAME_SCREEN = states.State(ENDGAME)
CHOOSE_TEAM = states.State(CHOOSETEAM)
CREATE_COMP = states.State(CREATECOMP)

# Team constants
BLUE = True
RED = False

playerAttack = False
pieces = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 11, 11, 11, 11, 11, 11, 12]

# Initialize the game
run = True

while run:
    
    if game_state == MENU:
        MAIN_MENU.draw(screen)
    elif game_state == GAME:
        BOARD.draw(screen)
    elif game_state == RULES:
        RULES_SCREEN.draw(screen, page)
    elif game_state == PAUSE:
        PAUSE_SCREEN.draw(screen)
    elif game_state == VERSUS:
        pygame.time.delay(500)
        BOARD.draw(screen)
        pygame.time.delay(100)
        game_state = ENEMYPLAY if playerAttack else GAME
        playerAttack = False
    elif game_state == ENDGAME:
        BOARD.draw(screen)
        ENDGAME_SCREEN.draw(screen, game_winner)
    elif game_state == CHOOSETEAM:
        CHOOSE_TEAM.draw(screen)
    elif game_state == ENEMYPLAY:
        enemyAttack = BOARD.moveEnemy()
        if enemyAttack:
            attacked, attacker, winner, endgame, draw = enemyAttack
            VERSUS_SCREEN.draw(screen, (attacked.id, attacker.id, winner, team, draw))
            game_state = ENDGAME if endgame else VERSUS
        else: 
            game_state = GAME
    elif game_state == CREATECOMP:
        BOARD.draw(screen)
        CREATE_COMP.draw(screen, (highlighted,available_pieces,team,allset))

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if game_state == GAME:
            if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
                game_state = ENDGAME
                break
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                game_state = PAUSE
                break
            if event.type == MOUSEBUTTONUP:
                if not BOARD.hasHighlighted():
                    x,y = pygame.mouse.get_pos()
                    if BOARD.isHovered(x,y):
                        pos = x,y = BOARD.getIndexes(x,y)
                        if BOARD.state[y][x] > 0 and not (BOARD.board[y][x].bomb or BOARD.board[y][x].flag or BOARD.board[y][x].id == 14):
                            moves = BOARD.validMoves(pos)
                            attacks = BOARD.attacks(pos)
                
                else:
                    xPiece,yPiece = pos
                    x,y = pygame.mouse.get_pos()
                    pos = x,y = BOARD.getIndexes(x,y)
                    if (x,y) in moves:
                        BOARD.attack((xPiece,yPiece), (x,y))
                        BOARD.empty(xPiece, yPiece)
                        game_state = ENEMYPLAY

                    elif (x,y) in attacks:
                        enemy = BOARD.board[y][x]
                        ally = BOARD.board[yPiece][xPiece]
                        param = (ally.id, enemy.id, 1, team, False)
                        game_state = VERSUS

                        if ally.id > abs(enemy.id):
                            param = (ally.id, enemy.id, 0, team, False)
                            BOARD.attack((xPiece,yPiece), (x,y))
                        elif ally.id == abs(enemy.id):
                            param = (ally.id, enemy.id, 0, team, True)
                            BOARD.empty(x,y)
                        elif enemy.bomb and ally.id == 3:
                            param = (ally.id, enemy.id, 0, team, False)
                            BOARD.attack((xPiece,yPiece), (x,y))
                        elif enemy.id == 10 and ally.id == 1:
                            param = (ally.id, enemy.id, 0, team, False)
                            BOARD.attack((xPiece,yPiece), (x,y))
                        elif enemy.flag:
                            param = (ally.id, enemy.id, 0, team, False)
                            BOARD.attack((xPiece,yPiece), (x,y))
                            game_winner = 0
                            game_state = ENDGAME

                        VERSUS_SCREEN.draw(screen, param)
                        BOARD.empty(xPiece, yPiece)
                        playerAttack = True

                    BOARD.switchPath()
    
        elif game_state == MENU: 
            buttons = MAIN_MENU.getButtons()
            if event.type == MOUSEBUTTONUP:
                click_sfx.play()
                if MAIN_MENU.isHovering(buttons[0]):
                    game_state = CHOOSETEAM
                elif MAIN_MENU.isHovering(buttons[1]):
                    page = 0
                    game_state = RULES
                elif MAIN_MENU.isHovering(buttons[2]):
                    run = False
                elif MAIN_MENU.isHovering(buttons[3]):
                    pause = pygame.mixer.music.get_busy()
                    pygame.mixer.music.pause() if pause else pygame.mixer.music.unpause()

        elif game_state == RULES:
            buttons = RULES_SCREEN.getButtons()
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                game_state = MENU
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and page < 3:
                page += 1
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT and page > 0:
                page -=1
            if event.type == MOUSEBUTTONUP:
                click_sfx.play()
                if RULES_SCREEN.isHovering(buttons[0]) and page > 0:
                    page -= 1
                elif RULES_SCREEN.isHovering(buttons[1]) and page < 3:
                    page +=1
                elif RULES_SCREEN.isHovering(buttons[2]):
                    game_state = MENU

        elif game_state == CHOOSETEAM:
            game_winner = 1
            available_pieces = pieces.copy()
            highlighted = False
            allset = False
            
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                game_state = MENU

            buttons = CHOOSE_TEAM.getButtons()    
            if event.type == MOUSEBUTTONUP:
                click_sfx.play()
                if CHOOSE_TEAM.isHovering(buttons[0]):
                    team = BLUE
                    BOARD = board.Board(BLUE)
                    game_state = CREATECOMP
                if CHOOSE_TEAM.isHovering(buttons[1]):
                    team = RED
                    BOARD = board.Board(RED)
                    game_state = CREATECOMP
                if CHOOSE_TEAM.isHovering((50,50)):
                    game_state = MENU

        elif game_state == PAUSE:
            buttons = PAUSE_SCREEN.getButtons() 
            
            if event.type == MOUSEBUTTONUP:
                click_sfx.play()
                if PAUSE_SCREEN.isHovering(buttons[0]):
                    game_state = GAME
                elif PAUSE_SCREEN.isHovering(buttons[1]):
                    game_state = MENU
                elif PAUSE_SCREEN.isHovering(buttons[2]):
                    pause = pygame.mixer.music.get_busy()
                    pygame.mixer.music.pause() if pause else pygame.mixer.music.unpause()

            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                game_state = GAME

        elif game_state == ENDGAME:
            button = ENDGAME_SCREEN.getButtons()
            if event.type == MOUSEBUTTONUP:
                click_sfx.play()
                if ENDGAME_SCREEN.isHovering(button):
                    game_state = MENU

        elif game_state == CREATECOMP:
            buttons = CREATE_COMP.getButtons()
            squares = buttons[0:40]
            icons = buttons[40:52]
            start = buttons[52]
            random = buttons[53]
            if BOARD.getScores() == (0,0):
                allset = True

            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                game_state = CHOOSETEAM

            if event.type == MOUSEBUTTONUP:
                if CREATE_COMP.isHovering(random):
                    click_sfx.play()
                    BOARD.fillAlly()
                    allset = True
                    available_pieces = []

                if allset:
                    click_sfx.play()
                    if CREATE_COMP.isHovering(start):
                        BOARD.gameOn = True
                        game_state = GAME

                else:
                    for square in squares:
                        x,y = square
                        if CREATE_COMP.isHovering(square):
                            highlighted = ((x-100)//80, (y-100)//80)
                    for icon in icons:
                        if CREATE_COMP.isHovering(icon) and highlighted:
                            j,i = highlighted
                            if not BOARD.state[i][j]:
                                x,y = icon
                                piece = ((x-20)//80)+1
                                if piece in available_pieces:
                                    available_pieces.remove(piece)
                                    BOARD.setPiece(piece, highlighted)

    pygame.display.update()

pygame.quit()
