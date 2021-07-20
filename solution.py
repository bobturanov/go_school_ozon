from numbers import Number
from typing import Tuple, List


def find_subarray_with_max_sum(nums: List[Number]) -> Tuple[int, int]:
    # TODO docstring
    current_max_sum = 0
    max_sum = float('-inf')  # TODO подумать над 1ым эл.
    start = 0
    end = 0
    new_start = 0

    for i in range(0, len(nums)):
        current_max_sum += nums[i]

        if max_sum < current_max_sum:
            max_sum = current_max_sum
            start = new_start
            end = i

        if current_max_sum < 0:
            current_max_sum = 0
            new_start = i + 1

    return start, end


print(find_subarray_with_max_sum([-15, 20, 40, -10, 15]))  # TODO написать тесты
