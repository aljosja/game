class Tile:
    def __init__(self, value=None):
        self.value = value


def domino():
    return Tile([1, 1])


if __name__ == "__main__":
    print('\n=== This Module Contains ==================')
    print('Tile(value=None)')
    print('===========================================')
    print(f"Tile(0): {Tile(0).value}")
    print(f"domino(): {domino().value}")
    print("===========================================\n")
