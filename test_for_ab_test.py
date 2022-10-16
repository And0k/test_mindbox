#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Purpose: personal test
# Copyright (C) 2022 Andrey Korzh <ao.korzh@gmail.com>

import numpy as np


def sum_digits(n: np.ndarray) -> np.ndarray:
    """
    Sums the digits in each array element
    :param n: integer array
    """
    s = n % 10
    while any(n := n // 10):
        s += n % 10
    return s


def group_sum(id_start: int, id_end: int) -> np.ndarray:
    """
    Sum of numbers (IDs) in each group, when IDs is a range from ``id_start`` to ``id_end`` and
     groups are defined by the sum of their digits
    :param id_start: ID range start
    :param id_end: ID range end
    :return: numpy array: sums of IDs in each group. Index of array element is a group number
    """
    # create IDs
    customers_id = np.arange(id_start, id_end)
    # assign group for IDs
    customers_group = sum_digits(customers_id)
    # calculate number of IDs in each group
    return np.bincount(customers_group)


# Required functions ##################################################################################################


def test_group_sum_1(n_customers: int) -> np.ndarray:
    """
    Sum of customers in each group, when customers IDs is a range from 0 to ``n_customers`` and
     groups are defined by the sum of their digits
    :param n_customers: customers number
    :return: numpy array: sums of IDs in each group. Index of array element is a group number
    """
    return group_sum(0, n_customers)


def test_group_sum_2(n_customers: int, n_first_id: int) -> np.ndarray:
    """
    Sum of customers in each group, when customers IDs is a range from ``n_first_id`` to
    ``n_first_id`` +``n_customers`` and groups IDs are defined by the sum of their digits
    :param n_customers: customers number
    :param n_first_id: first client ID
    :return: numpy array: sums of IDs in each group. Index of array element is a group number
    """
    return group_sum(n_first_id, n_first_id + n_customers)


if __name__ == '__main__':
    # Example run of two required functions (test_group_sum_1 and test_group_sum_2) and print their results.

    # Customers number for both functions:
    n_customers = 22
    # Starting customer' ID for 2nd function:
    n_first_id = 5

    for i_test in [1, 2]:
        title = f'Test {i_test}: n_first_id = {n_first_id}'
        print(title)
        print('-' * len(title))

        out = test_group_sum_1(n_customers) if i_test == 1 else test_group_sum_2(n_customers, n_first_id)

        # Result: clients number per group
        print(f'Group#\tClients')
        for i, s in enumerate(out):
            if s:
                print(f'{i:2d}\t{s:8d}')
        print()
    print('Ok>')
