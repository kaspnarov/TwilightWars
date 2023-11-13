import pygame
import pieces

# States constants
MENU = 0
GAME = 1
RULES = 2
PAUSE = 3
VERSUS = 4
ENDGAME = 5
CHOOSETEAM = 6
CREATECOMP = 8

BUTTON_SIZE = [(400,150), (0,0), (80,80), (100,100), (0,0), (300,100), (400,700), (0,0), (80,80)]
SCREENS = [pygame.image.load("src/img/menu_screen.png"),
           0,
           0,
           pygame.image.load("src/img/pause_screen.png"),
           pygame.image.load("src/img/versus_screen.png"),
           0,
           pygame.image.load("src/img/choose_team_screen.png"),
           0,
           0]
MENU_BUTTONS = [pygame.image.load("src/Buttons/Menu/play_button.png"),
                pygame.image.load("src/Buttons/Menu/play_button_hovered.png"),
                pygame.image.load("src/Buttons/Menu/rules_button.png"),
                pygame.image.load("src/Buttons/Menu/rules_button_hovered.png"),
                pygame.image.load("src/Buttons/Menu/exit_button.png"),
                pygame.image.load("src/Buttons/Menu/exit_button_hovered.png"),
                pygame.image.load("src/Buttons/Menu/sound_button.png"),
                pygame.image.load("src/Buttons/Menu/sound_button_hovered.png"),
                pygame.image.load("src/Buttons/Menu/sound_off_button.png"),
                pygame.image.load("src/Buttons/Menu/sound_off_button_hovered.png")]
PAUSE_BUTTONS = [pygame.image.load("src/Buttons/Pause/resume_button.png"),
                 pygame.image.load("src/Buttons/Pause/resume_button_hovered.png"),
                 pygame.image.load("src/Buttons/Pause/home_button.png"),
                 pygame.image.load("src/Buttons/Pause/home_button_hovered.png"),
                 pygame.image.load("src/Buttons/Pause/sound_button.png"),
                 pygame.image.load("src/Buttons/Pause/sound_button_hovered.png"),
                 pygame.image.load("src/Buttons/Pause/sound_off_button.png"),
                 pygame.image.load("src/Buttons/Pause/sound_off_button_hovered.png")]
CHOOSETEAM_BUTTONS = [pygame.image.load("src/Buttons/ChooseTeam/blue_button.jpg"),
                      pygame.image.load("src/Buttons/ChooseTeam/blue_button_hovered.jpg"),
                      pygame.image.load("src/Buttons/ChooseTeam/red_button.jpg"),
                      pygame.image.load("src/Buttons/ChooseTeam/red_button_hovered.jpg"),
                      pygame.image.load("src/Buttons/ChooseTeam/back_button.png"),
                      pygame.image.load("src/Buttons/ChooseTeam/back_button_hovered.png"),]

VERSUS_BLUE =  [pygame.image.load("src/Allies/nobg/WitchHunter.png"),
                pygame.image.load("src/Allies/nobg/Scout.png"),
                pygame.image.load("src/Allies/nobg/Seer.png"),
                pygame.image.load("src/Allies/nobg/Knight.png"),
                pygame.image.load("src/Allies/nobg/Shaman.png"),
                pygame.image.load("src/Allies/nobg/Dwarf.png"),
                pygame.image.load("src/Allies/nobg/Barbarian.png"),
                pygame.image.load("src/Allies/nobg/Monk.png"),
                pygame.image.load("src/Allies/nobg/Hero.png"),
                pygame.image.load("src/Allies/nobg/Wizard.png"),
                pygame.image.load("src/Allies/nobg/Spelltrap.png"),
                pygame.image.load("src/Allies/nobg/Grail.png")]
VERSUS_RED = [pygame.image.load("src/Enemies/nobg/Vampire.png"),
              pygame.image.load("src/Enemies/nobg/Imp.png"),
              pygame.image.load("src/Enemies/nobg/Drow.png"),
              pygame.image.load("src/Enemies/nobg/Undead.png"),
              pygame.image.load("src/Enemies/nobg/Goblin.png"),
              pygame.image.load("src/Enemies/nobg/Orc.png"),
              pygame.image.load("src/Enemies/nobg/Troll.png"),
              pygame.image.load("src/Enemies/nobg/Lich.png"),
              pygame.image.load("src/Enemies/nobg/Golem.png"),
              pygame.image.load("src/Enemies/nobg/Witch.png"),
              pygame.image.load("src/Enemies/nobg/Helltrap.png"),
              pygame.image.load("src/Enemies/nobg/Necronomicon.png")]

END_BG = [pygame.image.load("src/img/end-victory-bg.png"),
          pygame.image.load("src/img/end-defeat-bg.png")]
END_RIBBON = [pygame.image.load("src/img/victory-ribbon.png"),
              pygame.image.load("src/img/defeat-ribbon.png")]
END_BUTTONS = [pygame.image.load("src/Buttons/Endgame/continue-blue.png"),
              pygame.image.load("src/Buttons/Endgame/continue-blue-highlighted.png"),
              pygame.image.load("src/Buttons/Endgame/continue-red.png"),
              pygame.image.load("src/Buttons/Endgame/continue-red-highlighted.png")]

BG_MAP = pygame.image.load("src/img/map.png")
HOVER = pygame.image.load("src/img/highlight_bs.png")
HIGHLIGHT = pygame.image.load("src/img/highlight_player.png")
CREATECOMP_BUTTONS = [pygame.image.load("src/Buttons/CreateComp/start_button.png"),
                      pygame.image.load("src/Buttons/CreateComp/start_button_hovered.png"),
                      pygame.image.load("src/Buttons/CreateComp/randomize_button.png"),
                      pygame.image.load("src/Buttons/CreateComp/randomize_button_hovered.png"),
                      pygame.image.load("src/Buttons/CreateComp/start_button_disabled.png")]

RULES_PAGES = [pygame.image.load("src/img/rules_page_1.png"),
               pygame.image.load("src/img/rules_page_2.png"),
               pygame.image.load("src/img/rules_page_3.png"),
               pygame.image.load("src/img/rules_page_4.png")]
RULES_BUTTONS = [pygame.image.load("src/Buttons/Rules/back_button.png"),
                 pygame.image.load("src/Buttons/Rules/back_button_hovered.png"),
                 pygame.image.load("src/Buttons/Rules/forward_button.png"),
                 pygame.image.load("src/Buttons/Rules/forward_button_hovered.png"),
                 pygame.image.load("src/Buttons/Rules/close_button.png"),
                 pygame.image.load("src/Buttons/Rules/close_button_hovered.png")]

DARK_SCREEN = pygame.image.load("src/img/highlight_bg.png")
HIGHLIGHT_WINNER_BLUE = pygame.image.load("src/img/highlight_winner_blue.png")
HIGHLIGHT_WINNER_RED = pygame.image.load("src/img/highlight_winner_red.png")

class State:
    def __init__(self, state):
        self.state = state
        self.img = SCREENS[state]
        self.btn_w, self.btn_h = BUTTON_SIZE[state]

    def draw(self, screen, params=False):
        if self.state == MENU:
            screen.blit(self.img, (0,0))
            x,y = pygame.mouse.get_pos()

            for i,button in enumerate(self.getButtons()):
                xButton,yButton = button
                if i == 3:
                    if pygame.mixer.music.get_busy():
                        sound = MENU_BUTTONS[7] if self.isHovering(button) else MENU_BUTTONS[6]
                    else:
                        sound = MENU_BUTTONS[9] if self.isHovering(button) else MENU_BUTTONS[8]
                    screen.blit(sound, button)
                else:
                    if self.isHovering(button):
                        img = MENU_BUTTONS[i*2+1]
                    else:
                        img = MENU_BUTTONS[i*2]
                    screen.blit(img, button) 

        elif self.state == CHOOSETEAM:
            screen.blit(self.img, (0,0))
            x,y = pygame.mouse.get_pos()

            if 50 < x < 130 and 50 < y < 130:
                back = CHOOSETEAM_BUTTONS[5]
            else:
                back = CHOOSETEAM_BUTTONS[4]
            screen.blit(back, (50,50))

            for i,button in enumerate(self.getButtons()):
                xButton,yButton = button
                if xButton < x < xButton + self.btn_w and yButton < y < yButton + self.btn_h:
                    img = CHOOSETEAM_BUTTONS[i*2+1]
                else:
                    img = CHOOSETEAM_BUTTONS[i*2]
                screen.blit(img, button)

        elif self.state == PAUSE:
            screen.blit(self.img, (125, 250))
            for i,button in enumerate(self.getButtons()):
                if i == 2:
                    if pygame.mixer.music.get_busy():
                        img = PAUSE_BUTTONS[i*2+1] if self.isHovering(button) else PAUSE_BUTTONS[i*2]
                    else:
                        img = PAUSE_BUTTONS[i*2+3] if self.isHovering(button) else PAUSE_BUTTONS[i*2+2]
                else:
                    img = PAUSE_BUTTONS[i*2+1] if self.isHovering(button) else PAUSE_BUTTONS[i*2]
                screen.blit(img, button)

        elif self.state == VERSUS:
            ally, enemy, winner, blue_team, draw = params
            screen.blit(DARK_SCREEN, (100,100))
            screen.blit(self.img, (125,257))
            if winner or draw:
                screen.blit(HIGHLIGHT_WINNER_RED if blue_team else HIGHLIGHT_WINNER_BLUE, (520, 400))
            if not winner or draw: 
                screen.blit(HIGHLIGHT_WINNER_BLUE if blue_team else HIGHLIGHT_WINNER_RED, (270, 400))
            screen.blit(VERSUS_BLUE[ally-1] if blue_team else VERSUS_RED[ally-1], (295, 425))
            screen.blit(VERSUS_RED[enemy-1] if blue_team else VERSUS_BLUE[enemy-1], (545, 425))

        elif self.state == ENDGAME:
            win = params
            screen.blit(END_BG[win], (0,0))
            screen.blit(END_RIBBON[win], (150,300))
            x,y = pygame.mouse.get_pos()
            button = xButton, yButton = self.getButtons()
            if xButton < x < xButton + self.btn_w and yButton < y < yButton + self.btn_h:
                img = END_BUTTONS[win*2+1]
            else:
                img = END_BUTTONS[win*2]
            screen.blit(img, button)
            
        elif self.state == CREATECOMP:
            buttons = self.getButtons()
            highlighted, avail_pieces, ally, all_set = params
            squares = buttons[0:40]
            icons = buttons[40:52]

            for square in squares:
                if self.isHovering(square):
                    screen.blit(HOVER, square)

            if highlighted:
                m,n = highlighted
                screen.blit(HIGHLIGHT, (100+m*80, 100+n*80))

            for i,icon in enumerate(icons):
                xIcon,yIcon = icon
                if i+1 in avail_pieces:
                    if self.isHovering(icon):
                        screen.blit(HOVER, icon)
                    img = pieces.ALLIES[i] if ally else pieces.ENEMIES[i]
                    screen.blit(img, (xIcon+2.5, yIcon+2.5))
                    
            if all_set:
                button = (325, 430)
                if self.isHovering(button):
                    img = CREATECOMP_BUTTONS[1]
                else:
                    img = CREATECOMP_BUTTONS[0]
                screen.blit(img, button)
            
            else: 
                screen.blit(CREATECOMP_BUTTONS[4], (325, 430))

            rng = (675, 460)
            if self.isHovering(rng):
                img = CREATECOMP_BUTTONS[3]
            else:
                img = CREATECOMP_BUTTONS[2]
            screen.blit(img, rng)

        elif self.state == RULES:
            page = params
            screen.blit(RULES_PAGES[page], (0,0))
            for i,button in enumerate(self.getButtons()):
                if (page == 0 and i == 0) or (page == 3 and i == 1):
                    pass
                else:
                    img = RULES_BUTTONS[i*2+1] if self.isHovering(button) else RULES_BUTTONS[i*2]
                    screen.blit(img,button)

    def getButtons(self):
        if self.state == MENU:
            return [(300,500),(300,650),(400,820),(520,820)]
        elif self.state == PAUSE:
            return [(300, 470), (450, 470), (600, 470)]
        elif self.state == ENDGAME:
            return (350, 550)
        elif self.state == CHOOSETEAM:
            return [(66, 200), (533, 200)]
        elif self.state == CREATECOMP:
            squares = [(100+(x%10)*80, 580+(x//10)*80) for x in range(40)]
            icons = [(20+k*80, 910) for k in range(12)]
            for i in icons:
                squares.append(i)
            squares.append((325, 430))
            squares.append((675, 460))
            return squares
        elif self.state == RULES:
            return [(50,900),(870,900),(870,50)]

    def isHovering(self, button):
        width = self.btn_w
        height = self.btn_h
        if self.state == CHOOSETEAM and button == (50,50):
            width = 80
            height = 80
        elif self.state == CREATECOMP and button == (325, 430):
            width = 350
            height = 140
        elif self.state == MENU and (button == (520, 820) or button == (400,820)):
            width = 80
            height = 80
        x,y = pygame.mouse.get_pos()
        xButton,yButton = button
        if xButton < x < xButton + width and yButton < y < yButton + height:
            return True
        return False
