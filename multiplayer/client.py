import json
import socket

HOST = "127.0.0.1"
PORT = 12345


class Client:
    def __init__(self, host: str = None):
        print("Inicializando cliente...")

        self.player_id = None
        self.is_player_one = False
        self.is_running = True
        self.usernames = ['AI 1', 'AI 2']

        self.player_turn = None
        self.move_chip = None
        self._last_move_data = {}

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host if host else HOST, PORT))

        print(f"Cliente conectado na porta {PORT}")

    def _on_move_chip(self, *args):
        response = self.player_turn(*args)
        self._last_move_data = {str(value): value for value in response}

        return response

    def add_player_move(self, players_turn):
        self.player_turn = players_turn
        self.move_chip = self._on_move_chip

    def listen(self):
        while self.is_running:
            data = self.client.recv(1024).decode()

            if not data:
                print(f'Desconectado do servidor')
                break

            data = json.loads(data)
            print(f'Recebido {data}')

            # Primeira interação com o servidor
            if data.get("type") == "connect":
                self.player_id = data["player_id"]
                self.is_player_one = data["is_player_one"]

            elif data.get("type") == "info":
                usernames: list = data.get('usernames')

                if not self.is_player_one:
                    usernames.reverse()

                self.usernames = usernames

            # Movimento do oponente
            elif data.get("type") == "opponent_move":
                print("opponent_move")
                parameters = self._convert_parameters()

                self.move_chip(
                    data.get("column"),
                    parameters[1],
                    1 if self.is_player_one else 2,
                    parameters[3:],
                )

        self.client.close()

    def move(self, column: int):
        self._send_json({"type": "move", "player": self.player_id, "column": column})

    def send_username(self, username):
        self._send_json({"type": "info", "player": self.player_id, "username": username})

    def confirm_player2(self):
        self._send_json({"type": "player2_ready"})

    def close(self):
        self.is_running = False
        self.client.close()

    def _convert_parameters(self):
        return [
            self._last_move_data["column"],
            self._last_move_data["matrix"],
            self._last_move_data["player_turn"],
            self._last_move_data["sound_chip_1"],
            self._last_move_data["sound_chip_2"],
            self._last_move_data["usernames"],
            self._last_move_data["start_time"],
            self._last_move_data["scores"],
            self._last_move_data["option"],
        ]

    def _send_json(self, data: dict):
        self.client.send(json.dumps(data).encode("utf-8"))
