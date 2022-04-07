# Simple pygame program

# Import and initialize the pygame library
import pygame
from field import path
import threading
import random
from figure import toCoord, Figure
from field import Field
from network import Network
from _thread import *
import socket


FPS = 120  # frames per second setting
fpsClock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])


def setBackground():
    global image
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))


image = pygame.image.load(r'C:\Users\Alexandar\game1\ludo.png')
player1Img = pygame.image.load(r'C:\Users\Alexandar\game1\yellowpawn.png')
player2Img = pygame.image.load(r'C:\Users\Alexandar\game1\redpawn.png')
# player1Img = pygame.transform.scale(player1Img, (path[0].w-10, path[0].w-10))

dice1 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\0.png')
dice1 = pygame.transform.scale(dice1, (path[0].w - 10, path[0].w - 10))
dice2 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\1.png')
dice2 = pygame.transform.scale(dice2, (path[0].w - 10, path[0].w - 10))
dice3 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\2.png')
dice3 = pygame.transform.scale(dice3, (path[0].w - 10, path[0].w - 10))
dice4 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\3.png')
dice4 = pygame.transform.scale(dice4, (path[0].w - 10, path[0].w - 10))
dice5 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\4.png')
dice5 = pygame.transform.scale(dice5, (path[0].w - 10, path[0].w - 10))
dice6 = pygame.image.load(r'C:\Users\Alexandar\game1\dice\5.png')
dice6 = pygame.transform.scale(dice6, (path[0].w - 10, path[0].w - 10))

dice = [dice1, dice2, dice3, dice4, dice5, dice6]
dicePos = (screen.get_width() // 2 - (path[0].w - 10) // 2, screen.get_height() // 2 - (path[0].w - 10) // 2)

fontObj = pygame.font.Font('pdark.ttf', 16)
score1 = fontObj.render("SCORE", 1, (0, 0, 0))
score2 = fontObj.render("SCORE", 1, (0, 0, 0))

i = 0

running = True
onMove = True
k = diced = False

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 30)
fieldsP1 = [Field(13, 7), Field(12, 7), Field(11, 7), Field(10, 7), Field(9, 7), Field(8, 7)]
fieldsP2 = [Field(1, 7), Field(2, 7), Field(3, 7), Field(4, 7), Field(5, 7), Field(6, 7)]

player1 = [Figure("fig1", player1Img, (425, 405), 40, fieldsP1),
           Figure("fig2", player1Img, (505, 405), 40, fieldsP1),
           Figure("fig3", player1Img, (425, 485), 40, fieldsP1),
           Figure("fig4", player1Img, (505, 485), 40, fieldsP1)]

player2 = [Figure("fig1", player2Img, (65, 40), 14, fieldsP2),
           Figure("fig2", player2Img, (145, 40), 14, fieldsP2),
           Figure("fig3", player2Img, (65, 125), 14, fieldsP2),
           Figure("fig4", player2Img, (145, 125), 14, fieldsP2), ]


def showDice(num):
    screen.blit(dice[i], dicePos)


def hasPlayableFig(player):
    for fig in player:
        if not fig.inHome:
            return True
    return False


def pickNum():
    global k, onMove, cnt, cnt1, diced
    k = False

    showDice(i)
    diced = True


n= Network()

server = "192.168.0.104"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn, player):
    conn.send(str.encode("START"))
    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                playerResponse(data)
                conn.sendall(str.encode(data))
        except:
            break

    print("Lost connection")
    conn.close()

def f():
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, 1))

start_new_thread(f, ())


def playerResponse(data):
    data = data.split(",")
    for figure in player1:
        if figure.name == data[0]:
            figure.jump(int(data[1])+1)


while running:
    # set beackground elements
    setBackground()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            if k: i = random.randint(0, 5)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            n.connect()
            if not hasPlayableFig(player2) and not i == 5:
                diced = False

            if not diced:
                k = True
                startEvent = threading.Timer(1, pickNum)
                startEvent.start()

            if onMove:
                try:
                    for figure in player2:
                        if figure.playerRect.collidepoint(event.pos[0], event.pos[1]) and diced:
                            if not (figure.inHome and not i == 5):
                                diced = False
                                n.send(figure.name + ',' + str(i))
                                figure.jump(i + 1)
                                onMove = True  # it ll be false, but true for now

                except:
                    pass

    # display elemets
    showDice(i)
    for figure in player1:
        try:
            figure.show(screen)
        except:
            pass
    for figure in player2:
        try:
            figure.show(screen)
        except:
            pass
    screen.blit(score2, (80, 15))
    screen.blit(score1, (430, 570))

    # fetch screen elements on screen
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
