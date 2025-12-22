from player import *
from euchre_engine import *


def main():
    players = [EuchrePlayer(i) for i in range(4)]
    engine = EuchreEngine(players)

    engine.play()


if __name__ == "__main__":
    main()