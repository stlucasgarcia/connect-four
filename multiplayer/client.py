import json
import socket

HOST = "127.0.0.1"
PORT = 12345

turn_params = [
    "play_again",
    "turn",
    "chip",
    "scores",
    "column",
    "matrix",
    "sound_chip_1",
    "sound_chip_2",
    "usernames",
    "start_time",
    "option",
]


class Client:
    def __init__(self, host: str = None):
        print("Inicializando cliente...")
        self.host = host
        self.client = None

        self.player_id = None
        self.is_player_one = False
        self.turn = 1
        self.is_running = False
        self.usernames = ['AI 1', 'AI 2']

        self.player_turn = None
        self.move_chip = None
        self._last_move_data = {}

    def post_init(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host if self.host else HOST, PORT))

        print(f"Cliente conectado na porta {PORT}")

    def _on_move_chip(self, *args, **kwargs):
        response: tuple = self.player_turn(*args, **kwargs)

        self.turn = response[1]

        if kwargs.get("ignore_move"):
            turn = 1 if response[1] == 2 else 2
            self.turn = turn

            response = (response[0], turn, *response[2:])

        self.params_to_dict(response)

        return response

    def add_player_move(self, players_turn):
        self.player_turn = players_turn
        self.move_chip = self._on_move_chip

    def listen(self):
        self.is_running = True

        while self.is_running:
            data = self.client.recv(1024).decode()

            if not data:
                print(f'Desconectado do servidor')
                self.is_running = False

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
                parameters = self._convert_parameters()

                self.move_chip(
                    data.get("column") + 1,
                    parameters[1],
                    1 if self.is_player_one else 2,
                    *parameters[3:],
                    ignore_move=True,
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

    def params_to_dict(self, data):
        self._last_move_data = {k: v for k, v in zip(turn_params, data)}

    def _convert_parameters(self):
        return [
            self._last_move_data["column"],
            self._last_move_data["matrix"],
            self._last_move_data["turn"],
            self._last_move_data["sound_chip_1"],
            self._last_move_data["sound_chip_2"],
            self._last_move_data["usernames"],
            self._last_move_data["start_time"],
            self._last_move_data["scores"],
            self._last_move_data["option"],
        ]

    def _send_json(self, data: dict):
        self.client.send(json.dumps(data).encode("utf-8"))
