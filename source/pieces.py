import pygame

imp = pygame.image.load("src/Allies/icons/knight.png")

ALLIES = [pygame.image.load("src/Allies/icons/witch_hunter.png"),
          pygame.image.load("src/Allies/icons/scout.png"), 
          pygame.image.load("src/Allies/icons/seer.png"), 
          pygame.image.load("src/Allies/icons/knight.png"), 
          pygame.image.load("src/Allies/icons/shaman.png"), 
          pygame.image.load("src/Allies/icons/dwarf.png"), 
          pygame.image.load("src/Allies/icons/barbarian.png"), 
          pygame.image.load("src/Allies/icons/monk.png"), 
          pygame.image.load("src/Allies/icons/hero.png"), 
          pygame.image.load("src/Allies/icons/wizard.png"), 
          pygame.image.load("src/Allies/icons/bomb.png"), 
          pygame.image.load("src/Allies/icons/flag.png")]
BLUE_ICON = pygame.image.load("src/Allies/icons/blue_icon.png")

ENEMIES = [pygame.image.load("src/Enemies/icons/vampire.png"),
           pygame.image.load("src/Enemies/icons/imp.png"),
           pygame.image.load("src/Enemies/icons/drow.png"),
           pygame.image.load("src/Enemies/icons/undead.png"),
           pygame.image.load("src/Enemies/icons/goblin.png"),
           pygame.image.load("src/Enemies/icons/orc.png"),
           pygame.image.load("src/Enemies/icons/troll.png"),
           pygame.image.load("src/Enemies/icons/lich.png"),
           pygame.image.load("src/Enemies/icons/golem.png"),
           pygame.image.load("src/Enemies/icons/witch.png"),
           pygame.image.load("src/Enemies/icons/bomb.png"),
           pygame.image.load("src/Enemies/icons/flag.png")]
RED_ICON = pygame.image.load("src/Enemies/icons/red_icon.png")

HIGHLIGHT_PLAYER = pygame.image.load("src/img/highlight_player.png")
HIGHLIGHT_ENEMY = pygame.image.load("src/img/highlight_enemy.png")
HIGHLIGHT_BS = pygame.image.load("src/img/highlight_bs.png")

CELL_SIZE = 80
LBORDER = 100

class Piece:

    def __init__(self, num, ally=True):
        self.id = abs(num)
        self.lit = False
        self.enemy = num < 0 
        self.player = 0 < num < 14
        self.bomb = abs(num) == 11
        self.flag = abs(num) == 12
        self.icon = False
        if num in range (1,13):
            self.icon = ALLIES[num-1] if ally else ENEMIES[abs(num)-1]
        elif num < 0:
            self.icon = RED_ICON if ally else BLUE_ICON

    def draw(self, screen, pos):
        i,j = pos
        pos = (LBORDER + j*(CELL_SIZE) + 2, LBORDER + i*(CELL_SIZE) + 2, CELL_SIZE-3, CELL_SIZE-3)
        if self.lit:
            if self.player:
                img = HIGHLIGHT_PLAYER
            elif self.enemy:
                img = HIGHLIGHT_ENEMY
            else:
                img = HIGHLIGHT_BS
            screen.blit(img, (LBORDER + j*(CELL_SIZE), LBORDER + i*(CELL_SIZE), CELL_SIZE, CELL_SIZE))
        if self.icon:
            screen.blit(self.icon, pos)


    