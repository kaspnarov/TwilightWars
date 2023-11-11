import random
import pygame
import pieces

pygame.font.init()


MATRIX_SIZE = 10
self_SIZE = 800
CELL_SIZE = self_SIZE//MATRIX_SIZE
LBORDER = 100
UBORDER = LBORDER + self_SIZE
BG_MAP = pygame.image.load("src/img/map.png")
BG = pygame.image.load("src/img/gamebg.png")
SCOREFONT = pygame.font.Font("src/fonts/OldLondon.ttf", 80)
LIST_WARRIORS = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 11, 11, 11, 11, 11, 11, 12]


class Board:

    def __init__(self, ally=True):
        self.state = self.randomBoard()
        self.ally = ally
        self.gameOn = False

        self.board = []

        for row in self.state:
            new_row = []
            for item in row:
                new_row.append(pieces.Piece(item, self.ally))
            self.board.append(new_row)

    def draw(self, screen):
        # Draw Background
        screen.blit(BG, (0,0))
        screen.blit(BG_MAP, (LBORDER,LBORDER))

        # Draw scores
        player_score, enemy_score = self.getScores()
        player_score_text = SCOREFONT.render(str(player_score), True, (255,255,255))
        enemy_score_text = SCOREFONT.render(str(enemy_score), True, (255,255,255))
        
        pos_player = (50,490) if self.ally else (950,490)
        pos_enemy = (950,490) if self.ally else (50,490)

        pst_rect = player_score_text.get_rect(center=pos_player)
        est_rect = enemy_score_text.get_rect(center=pos_enemy)

        if self.gameOn:
            screen.blit(player_score_text, pst_rect)
            screen.blit(enemy_score_text, est_rect)

        # Draw icons
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):
                self.board[i][j].draw(screen, (i,j))

    def validMoves(self, pos):
        x, y = pos
        moves = []

        if self.board[y][x].id == 2:
            moves = self.getPaths(pos, [])
        elif self.board[y][x].id in range(3,11) or self.board[y][x].id == 1:
            moves = self.getPath(pos, [])
        
        self.switchPath()
        
        for i,row in enumerate(self.board):
            for j,item in enumerate(row):
                if (j,i) == (x,y) :
                    item.lit = True
                elif (j,i) in moves:
                    item.lit = True

        return moves

    def getPath(self, pos, checked):
        x, y = pos
        
        for i in [-1,1]:
            try:
                piece = self.board[y+i][x]
                if (y+i in range(MATRIX_SIZE)) and not self.state[y+i][x] and not piece.lit:
                    checked.append((x,y+i))
            except IndexError: pass

        for j in [-1,1]:
            try:
                piece = self.board[y][x+j]
                if (x+j in range(MATRIX_SIZE)) and not self.state[y][x+j] and not piece.lit:
                    checked.append((x+j,y))
            except IndexError: pass

        return checked

    def getPaths(self, pos, checked=[]):
        x, y = pos
        
        for i in [-1,1]:
            try:
                if (y+i in range(MATRIX_SIZE)) and not self.state[y+i][x] and (x,y+i) not in checked:
                    checked.append((x,y+i))
                    self.getPaths((x,y+i), checked)
            except IndexError: pass

        for j in [-1,1]:
            try:
                if (x+j in range(MATRIX_SIZE)) and not self.state[y][x+j] and (x+j,y) not in checked:
                    checked.append((x+j,y))
                    self.getPaths((x+j,y), checked)
            except IndexError: pass
        
        return checked
    
    def attacks(self, pos):
        x, y = pos
        attacks = []

        if self.board[y][x].id == 2:
            for (x,y) in self.getPaths(pos, []):
                for i in [-1,1]:
                    try:
                        if (y+i in range(MATRIX_SIZE)) and self.board[y+i][x].enemy:
                            attacks.append((x,y+i))
                    except IndexError: pass

                for j in [-1,1]:
                    try:
                        if (x+j in range(MATRIX_SIZE)) and self.board[y][x+j].enemy:
                            attacks.append((x+j,y))
                    except IndexError: pass

        for i in [-1,1]:
            try:
                if (y+i in range(MATRIX_SIZE)) and self.board[y+i][x].enemy:
                    attacks.append((x,y+i))
            except IndexError: pass

        for j in [-1,1]:
            try:
                if (x+j in range(MATRIX_SIZE)) and self.board[y][x+j].enemy:
                    attacks.append((x+j,y))
            except IndexError: pass

        for (x,y) in attacks:
            self.board[y][x].lit = True

        return attacks

    def switchPath(self, on=False):
        for row in self.board:
            for piece in row:
                piece.lit = on
                
    def hasHighlighted(self):
        for row in self.board:
            for piece in row:
                if piece.lit:
                    return True

    def isHovered(self, x, y):
        if LBORDER < x < UBORDER and LBORDER < y < UBORDER:
            return True
        return False

    def getIndexes(self, x, y):
        return ((x-LBORDER)//CELL_SIZE, (y-LBORDER)//CELL_SIZE)

    def empty(self, x, y):
        self.state[y][x] = 0
        self.board[y][x] = pieces.Piece(0)

    def attack(self, posAttacker, posAttacked):
        x, y = posAttacked
        xPiece, yPiece = posAttacker
        self.state[y][x] = self.state[yPiece][xPiece]
        self.board[y][x] = pieces.Piece(self.state[yPiece][xPiece], self.ally)

    def randomBoard(self):
        state = []
        enemies = random.sample(LIST_WARRIORS, 40)
        for i in range(4):
            row = []
            for j in range(10):
                row.append(-enemies[10*i+j])
            state.append(row)
        
        for _ in range(2):
            state.append([0, 0, 14, 14, 0, 0, 14, 14, 0, 0])

        for i in range(4):
            state.append([0]*10)

        return state

    def dist(self, pos):
        x,y = pos
        return ((5-x)**2+(9-y)**2) ** (1/2)

    def movableEnemies(self):
        enemies = []
        for y in range(10):
            for x in range(10):
                movable = False
                if self.board[y][x].enemy and self.board[y][x].id < 11:
                    if y+1 in range(MATRIX_SIZE):
                        if self.board[y+1][x].id == 0:
                            movable = True

                    if y-1 in range(MATRIX_SIZE):
                        if self.board[y-1][x].id == 0:
                            movable = True

                    if x+1 in range(MATRIX_SIZE):
                        if self.board[y][x+1].id == 0:
                            movable = True

                    if x-1 in range(MATRIX_SIZE):
                        if self.board[y][x-1].id == 0:
                            movable = True
                        
                if movable:
                    enemies.append((x,y))  
        enemies.sort(key=self.dist)

        cut = min(3, len(enemies))

        return enemies[0:cut+1]


    def enemyMoves(self, pos):
        x, y = pos
        moves = []

        if self.board[y][x].id == 2:
            moves = self.getEnemyPaths(pos, [])
        elif self.board[y][x].id in range(3,11) or self.board[y][x].id == 1:
            moves = self.getEnemyPath(pos)
        
        return moves

    def getEnemyPath(self, pos):
        x, y = pos
        checked = []
        
        if y+1 in range(MATRIX_SIZE):
            if self.board[y+1][x].id == 0:
                checked.append((x,y+1))

        if y-1 in range(MATRIX_SIZE):
            if self.board[y-1][x].id == 0:
                checked.append((x,y-1))

        if x+1 in range(MATRIX_SIZE):
            if self.board[y][x+1].id == 0:
                checked.append((x+1,y))

        if x-1 in range(MATRIX_SIZE):
            if self.board[y][x-1].id == 0:
                checked.append((x-1,y))

        return checked

    def getEnemyPaths(self, pos, checked):
        x, y = pos
        
        for i in [-1,1]:
            try:
                if (y+i in range(MATRIX_SIZE)) and self.board[y+i][x].id == 0 and (x,y+i) not in checked:
                    checked.append((x,y+i))
                    self.getPaths((x,y+i), checked)
            except IndexError: pass

        for j in [-1,1]:
            try:
                if (x+j in range(MATRIX_SIZE)) and self.board[y][x+j].id == 0 and (x+j,y) not in checked:
                    checked.append((x+j,y))
                    self.getPaths((x+j,y), checked)
            except IndexError: pass
        
        return checked                    

    def enemyAttacks(self, pos):
        x, y = pos
        attacks = []

        if self.board[y][x].id == 2:
            for (x,y) in self.getEnemyPaths(pos, []):
                if y+1 in range(MATRIX_SIZE):
                    if self.board[y+1][x].player:
                        attacks.append((x,y+1))

                if y-1 in range(MATRIX_SIZE):
                    if self.board[y-1][x].player:
                        attacks.append((x,y-1))

                if x+1 in range(MATRIX_SIZE):
                    if self.board[y][x+1].player:
                        attacks.append((x+1,y))

                if x-1 in range(MATRIX_SIZE):
                    if self.board[y][x-1].player:
                        attacks.append((x-1,y))

        
        if y+1 in range(MATRIX_SIZE):
            if self.board[y+1][x].player:
                attacks.append((x,y+1))

        if y-1 in range(MATRIX_SIZE):
            if self.board[y-1][x].player:
                attacks.append((x,y-1))

        if x+1 in range(MATRIX_SIZE):
            if self.board[y][x+1].player:
                attacks.append((x+1,y))

        if x-1 in range(MATRIX_SIZE):
            if self.board[y][x-1].player:
                attacks.append((x-1,y))

        return attacks

    def moveEnemy(self):
        enemies = self.movableEnemies()
        pos = xPiece,yPiece = random.choice(enemies)
        piece = self.board[yPiece][xPiece]
        moves = self.enemyMoves((xPiece,yPiece))
        attacks = self.enemyAttacks((xPiece,yPiece))
        param = False

        if attacks != []:
            x, y = random.choice(attacks)
            attacked = self.board[y][x]
            winner = 1
            draw = False
            endgame = False

            if piece.id > attacked.id:
                winner = 0
                self.attack(pos, (x,y))
            elif piece.id == attacked.id:
                winner = 0
                draw = True
                self.empty(x,y)
            elif attacked.bomb and piece.id == 3:
                winner = 0
                self.attack(pos, (x,y))
            elif attacked.id == 10 and piece.id == 1:
                winner = 0
                self.attack(pos, (x,y))
            elif attacked.flag:
                winner = 0
                endgame = True
                self.attack(pos, (x,y))
            param = (piece, attacked, winner, endgame, draw)
            self.empty(xPiece, yPiece)

        elif moves != []:
            dist = 1000
            for move in moves:
                x,y = move
                newdist = ((5-x)**2+(9-y)**2) ** (1/2)
                if newdist < dist:
                    dist = newdist
                    chosen = move
            self.attack(pos, chosen)
            self.empty(xPiece, yPiece)

        return param

    def moveEnemy2(self):
        aliados = []
        for y in range(10):
            for x in range(10):
                if self.board[y][x].player:
                    aliados.append((x,y))

    def getScores(self):
        playerPieces = enemyPieces = 0
        for row in self.board:
            for piece in row:
                if piece.enemy:
                    enemyPieces += 1
                elif piece.player:
                    playerPieces += 1
        
        return (40-enemyPieces, 40-playerPieces)

    def setPiece(self, piece, pos):
        x,y = pos
        self.state[y][x] = piece
        self.board[y][x] = pieces.Piece(piece, self.ally)

    def fillAlly(self):
        allies = random.sample(LIST_WARRIORS, 40)
        for i in range(4):
            for j in range(10):
                piece = allies[10*i+j]
                self.state[6+i][j] = piece
                self.board[6+i][j] = pieces.Piece(piece, self.ally)
