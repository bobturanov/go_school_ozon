from numbers import Number
from typing import Tuple, List


def find_subarray_with_max_sum(nums: List[Number]) -> Tuple[int, int]:
    """
    Returns start and end indexes of subarray with max sum.

            Parameters:
                    nums (list): list of numbers

            Returns:
                    (start, end) (tuple):  start and end indexes of subarray
    """

    if not nums:
        raise ValueError('Empty list, try not empty list')

    if not isinstance(nums, list):
        raise TypeError(f'Received {type(nums)}, try list')

    current_max_sum = 0
    max_sum = float('-inf')
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
