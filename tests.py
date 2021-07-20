from unittest import TestCase

from solution import find_subarray_with_max_sum


class TestSubarray(TestCase):

    def test_find_subarray_with_max_sum(self):
        self.assertTupleEqual((3, 5), find_subarray_with_max_sum([10, -3, -12, 8, 42, 1, -7, 0, 3]))  # default case
        self.assertTupleEqual((1, 1), find_subarray_with_max_sum([-2, 1]))  # kill max_sum first element case
        self.assertTupleEqual((0, 0), find_subarray_with_max_sum([1, -2]))  # kill max_sum first element case revers
        self.assertTupleEqual((0, 0), find_subarray_with_max_sum([0, 0, 0, 0]))  # zeros case
        self.assertTupleEqual((0, 0), find_subarray_with_max_sum([1]))  # one element case
        self.assertTupleEqual((0, 0), find_subarray_with_max_sum([0]))  # one element zero case
        self.assertTupleEqual((0, 0), find_subarray_with_max_sum([-7]))  # one negative element case
        self.assertTupleEqual((5, 5), find_subarray_with_max_sum([-10, -3, -12, -8, -42, -1, -7, -3]))  # all negative
        self.assertTupleEqual((0, 7), find_subarray_with_max_sum([10, 3, 12, 8, 42, 1, 7, 3]))  # all positive case
        # 2 same subarrays case
        self.assertTupleEqual((7, 11), find_subarray_with_max_sum([10, -3, -12, 8, 42, 1, -77, 0, 3, 8, 42, 1]))
        # subarray with max sum at the beginning case
        self.assertTupleEqual((0, 1), find_subarray_with_max_sum([10, 3, -12, -8, -42, 1, 7, -3]))
        # subarray with max sum at the beginning case
        self.assertTupleEqual((6, 7), find_subarray_with_max_sum([-12, -8, -42, 1, -7, -3, 10, 3]))
        # real numbers case
        self.assertTupleEqual((3, 5), find_subarray_with_max_sum([.10, -.3, -.12, .8, .42, .1, -.7, 0.0, .3]))
        # int and real numbers case
        self.assertTupleEqual((3, 5), find_subarray_with_max_sum([.10, -.3, -.12, .8, 42, .1, -.7, 0, .3]))

    def test_find_subarray_with_max_sum_empty_list_case(self):
        with self.assertRaises(ValueError):
            find_subarray_with_max_sum([])

    def test_find_subarray_with_max_sum_wrong_type(self):
        with self.assertRaises(TypeError):
            find_subarray_with_max_sum((16, 54))  # type: ignore
