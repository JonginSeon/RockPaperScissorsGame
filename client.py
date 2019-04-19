import pygame
from network import Network
pygame.font.init()

#settubg height and width of the window
width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

rock = pygame.image.load("images/rock.png").convert()
rock=pygame.transform.scale(rock,(200, 200))

scissors = pygame.image.load("images/scissors.png").convert()
scissors=pygame.transform.scale(scissors,(200, 200))


paper = pygame.image.load("images/paper.png").convert()
paper=pygame.transform.scale(paper,(200, 200))



class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 200
        self.height = 200

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
        win.blit(rock ,  ( 100,400))
        win.blit(scissors ,  ( 400,400))
        win.blit(paper ,  ( 700,400))

        pygame.display.flip() # paint screen one time
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, p):
    win.fill((0,0,0)) #background color black

    if not(game.connected()):

        welcome2 = pygame.image.load("images/welcome2.png").convert()
        welcome2 = pygame.transform.scale(welcome2,(900, 900))
        win.blit(welcome2, (0,0))

        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Finding Match", 1, (0,0,0), True)
        win.blit(text, (270,500))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 0,0))
        win.blit(text, (80, 200))

        text = font.render("Opponents", 1, (0, 0, 0))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (255,255,255))
            text2 = font.render(move2, 1, (255, 255, 255))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (255,255,255))
            elif game.p1Went:
                text1 = font.render("Select an Option", 1, (255, 255, 255))
            else:
                text1 = font.render("Select an Option", 1, (255, 255, 255))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (255,255,255))
            elif game.p2Went:
                text2 = font.render("Select an Option", 1, (255, 255, 255))
            else:
                text2 = font.render("Select an Option", 1, (255, 255, 255))

        if p == 1:
            win.blit(text2, (250, 100))
           # win.blit(text1, (250, 100))
        else:
            win.blit(text1, (250, 100))
            #win.blit(text2, (250, 800))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

# creates the buttons at the given locations
btns = [Button("Rock", 100, 400, (0,0,0)), Button("Scissors", 400, 400, (255,0,0)), Button("Paper", 700, 400, (0,255,0))]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("arial", 90)
            move1 = game.get_player_move(0)
            move2 = game.get_player_move(1)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                win.fill((0,0,0))

                if move1[0] == "R" and move2[0] == "S":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))


                    win.blit(rock ,  ( 200,350))
                    win.blit(scissors ,  ( 500,350))
                   # win.blit(paper ,  ( 0,450))


                elif move1[0] == "S" and move2[0] == "R":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))


                    win.blit(scissors ,( 200,350))
                    win.blit(rock ,  ( 500,350))

                elif move1[0] == "R" and move2[0] == "P":

                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(rock ,( 200,350))
                    win.blit(paper ,  ( 500,350))
                elif move1[0] == "P" and move2[0] == "R":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(paper ,( 200,350))
                    win.blit(rock ,  ( 500,350))
                elif move1[0] == "S" and move2[0] == "P":
                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(scissors ,( 200,350))
                    win.blit(paper ,  ( 500,350))
                elif move1[0] == "P" and move2[0] == "S":
                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(paper ,( 200,350))
                    win.blit(scissors ,  ( 500,350))
                text = font.render("You Won!", 1, (255,0,0))

            elif game.winner() == -1:
                win.fill((0,0,0))
                if move1[0] == "R" and move2[0] == "R":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    rock1 = pygame.image.load("images/rock.png").convert()
                    rock1=pygame.transform.scale(rock1,(200, 200))


                    win.blit(rock ,  ( 200,350))
                    win.blit(rock1 ,  ( 500,350))
                if move1[0] == "S" and move2[0] == "S":
                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))

                    scissors1 = pygame.image.load("images/scissors.png").convert()
                    scissors1=pygame.transform.scale(scissors1,(200, 200))


                    win.blit(scissors ,  ( 200,350))
                    win.blit(scissors1 ,  ( 500,350))
                if move1[0] == "P" and move2[0] == "P":
                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    paper1 = pygame.image.load("images/paper.png").convert()
                    paper1=pygame.transform.scale(paper1,(200, 200))


                    win.blit(paper ,  ( 200,350))
                    win.blit(paper1 ,  ( 500,350))

                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                win.fill((0,0,0))
                if move1[0] == "R" and move2[0] == "S":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))


                    win.blit(rock ,  ( 200,350))
                    win.blit(scissors ,  ( 500,350))
                   # win.blit(paper ,  ( 0,450))


                elif move1[0] == "S" and move2[0] == "R":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))


                    win.blit(scissors ,( 200,350))
                    win.blit(rock ,  ( 500,350))

                elif move1[0] == "R" and move2[0] == "P":

                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(rock ,( 200,350))
                    win.blit(paper ,  ( 500,350))
                elif move1[0] == "P" and move2[0] == "R":
                    rock = pygame.image.load("images/rock.png").convert()
                    rock=pygame.transform.scale(rock,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(paper ,( 200,350))
                    win.blit(rock ,  ( 500,350))
                elif move1[0] == "S" and move2[0] == "P":
                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(scissors ,( 200,350))
                    win.blit(paper ,  ( 500,350))
                elif move1[0] == "P" and move2[0] == "S":
                    scissors = pygame.image.load("images/scissors.png").convert()
                    scissors=pygame.transform.scale(scissors,(200, 200))

                    paper = pygame.image.load("images/paper.png").convert()
                    paper=pygame.transform.scale(paper,(200, 200))

                    win.blit(paper ,( 200,350))
                    win.blit(scissors ,  ( 500,350))
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (350,200))
            pygame.display.update()
            pygame.time.delay(4000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        #win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        #text = font.render("Click to Play!", 1, (255,0,0))

        welcome = pygame.image.load("images/welcome.png").convert()
        welcome=pygame.transform.scale(welcome,(900, 900))
        win.blit(welcome, (0,0))
        text = font.render("Rock Paper Scissors Game", 1, (0,0,0))
        win.blit(text, (100,150))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
