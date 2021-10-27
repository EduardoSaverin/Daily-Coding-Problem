# Problem #30

from typing import List

class Problem30(object):
    def __init__(self) -> None:
        super().__init__()

    def run(self, input: List[int]) -> int:
        l_index, r_index = 0, len(input)-1
        left_max, right_max = input[l_index], input[r_index]
        total_water: int = 0
        while l_index <= r_index:
            if input[l_index] < input[r_index]:
                if input[l_index] > left_max:
                    left_max = input[l_index]
                else:
                    total_water += left_max - input[l_index]
                l_index += 1
            else:
                if input[r_index] > right_max:
                    right_max = input[r_index]
                else:
                    total_water += right_max - input[r_index]
                r_index -= 1
        return total_water

if __name__ == '__main__':
    arr:List[int] = list(map(int, input('Enter array elements separated by space\n').split(' ')))
    pb: Problem30 = Problem30()
    print('Solution : ', pb.run(arr))