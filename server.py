import socket
from _thread import *
import pickle
from game import Game

#IP address of the machine running the server
server = "35.40.125.89"
port = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# listens for two connections to start a game
s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(connection p, gameId):
    global idCount
    connection.send(str.encode(str(p)))

    reply = "Connected"
    while True:
        try:
            data = connection.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    connection.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    connection.close()



while True:
    connection addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    # when 2 more clients connect, a new thread is started
    start_new_thread(threaded_client, (connection p, gameId))
