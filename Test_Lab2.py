import lab2


def test_find_min_max():

    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 90]

    result = lab2.calc_min_max(input_arr)

    assert (result == test_arr)
def test_calc_average():
    input_arr = [1, 2, 3, 4, 5]
    test_arr = 3

    result = lab2.calc_average(input_arr)

    assert (result == test_arr)
def test_calc_median_temperature():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = 25

    result = lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)