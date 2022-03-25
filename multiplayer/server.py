import json
import socket
import threading
from _thread import *

HOST = "127.0.0.1"
PORT = 12345

print_lock = threading.Lock()


class Server:
    def __init__(self):
        self.is_running = False
        self.server = None

        self.player1 = None
        self.player2 = None
        self.usernames = ['AI 1', 'AI 2']
        self.connections = []

        self.is_ready = False

    def post_init(self):
        print("Inicializando servidor...")

        self.is_running = True

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))

        print(f"Servidor inicializado na porta {PORT}")

        self.server.listen(5)
        print("Servidor está escutando por ações")

    def listen(self):
        while self.is_running:
            connection, address = self.server.accept()

            start_new_thread(self.threaded, (connection, address))

    def threaded(self, connection: socket, address):
        self.connections.append(connection)

        print(f'Nova conexão! {address[0]}:{address[1]}')

        # Primeiro jogador conectado
        if not self.player1:
            self.player1 = address[1]
            self._send_json(connection, {"type": "connect", "player_id": self.player1, "is_player_one": True})

        # Segundo jogador conectado
        elif self.player1 and not self.player2:
            self.player2 = address[1]
            self._send_json(connection, {"type": "connect", "player_id": self.player2, "is_player_one": False})

        while self.is_running:
            try:
                data = connection.recv(1024).decode()

                if not data:
                    raise ConnectionResetError()

                data = json.loads(data)
                print(f'Recebido {data}')

                # Movimento dos jogadores
                if data.get("type") == "move":
                    self._send_json(
                        self.connections[0] if data.get("player") == self.player2 else self.connections[1],
                        {
                            "type": "opponent_move",
                            "player": data.get("player"),
                            "column": data.get("column"),
                        },
                    )

                # Recebendo nome dos jogadores
                elif data.get("type") == "info":
                    if data.get("player") == self.player1:
                        self.usernames[0] = data.get("username")
                    elif data.get("player") == self.player2:
                        self.usernames[1] = data.get("username")

                # Confirmando partida e enviando nome dos jogadores
                elif data.get("type") == "player2_ready":
                    self._send_json(
                        connection, {
                            "type": "info",
                            "usernames": self.usernames,
                        },
                        sendall=True,
                    )

                    self.is_ready = True

            except ConnectionResetError:
                if self.player1 == address[1]:
                    self.player1 = None
                    self.is_ready = False
                elif self.player2 == address[1]:
                    self.player2 = None
                    self.is_ready = False

                print(f'Cliente {address[0]}:{address[1]} desconectado')

                print(f"{self.player1=}, {self.player2=}")

                print_lock.release()
                break

        connection.close()

    def close(self):
        self.is_running = False
        self.server.close()

    def _send_json(self, connection, data: dict, sendall=False):
        json_data = json.dumps(data).encode("utf-8")

        if sendall:
            for conn in self.connections:
                conn.send(json_data)
        else:
            connection.send(json_data)


# Just for tests
if __name__ == '__main__':
    server = Server()
    server.post_init()
    server.listen()
