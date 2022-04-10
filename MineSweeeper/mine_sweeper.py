import numpy as np


class MineSweeper:

    @staticmethod
    def create_mine_field(f_size: int,
                          coor_y: list,
                          coor_x: list) -> list:

        for elem in list(coor_y + coor_x):
            if elem >= f_size:
                raise ValueError(
                    "Co-ordinate of bomb position must in the field",
                    "{}".format(np.arange(0, f_size, 1).tolist()),
                    "Coordinate = {} is input.".format(elem))

        mine_coor = list(set(zip(coor_y, coor_x)))

        board = []

        for row in range(f_size):

            board.append([0] * f_size)

            for idx in range(0, len(mine_coor)):

                if mine_coor[idx][0] == row:

                    for col in range(f_size):

                        if mine_coor[idx][1] == col:
                            board[row][col] = "B"

        return board

    @staticmethod
    def number_around_bomb(mine_idx: int,
                           f_size: int):

        if mine_idx >= f_size:
            raise ValueError()

        results = [mine_idx - 1, mine_idx, mine_idx + 1]

        for idx, res in enumerate(results):

            if res < 0 or res >= f_size:
                results.pop(idx)

        return results

    def find_mines(self, mine_field):

        for row_idx, row in enumerate(mine_field):
            for pos_idx, position in enumerate(row):

                if position == "B":

                    for pos_around_bomb_x in self.number_around_bomb(row_idx, len(mine_field)):
                        for pos_around_bomb_y in self.number_around_bomb(pos_idx, len(mine_field)):

                            try:
                                mine_field[pos_around_bomb_x][pos_around_bomb_y] += 1

                            except:
                                pass

        results = []

        for row in mine_field:
            results.append(list(map(lambda pos: str(pos), row)))

        return results


# main function #
def mine_sweeper_map(f_size: int,
                     coor_y: list,
                     coor_x: list) -> list:
    ms = MineSweeper()

    field = ms.create_mine_field(f_size, coor_y, coor_x)

    game_map = ms.find_mines(field)

    return game_map


if __name__ == "__main__":

    field_size = int(input("field_size: "))

    mine_qty = int(field_size / 3) + field_size

    coor_bomb_y = (np
                   .random
                   .randint(0, field_size - 1, mine_qty)
                   .tolist())

    coor_bomb_x = (np
                   .random
                   .randint(0, field_size - 1, mine_qty)
                   .tolist())

    result = mine_sweeper_map(f_size=field_size,
                              coor_y=coor_bomb_y,
                              coor_x=coor_bomb_x)

    print("mine_qty = {}".format(mine_qty))

    for x in result:
        print(x)
