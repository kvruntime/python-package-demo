import _context

_context.__file__
from demopack import functions


def test__calculate_energy__take_100_2_expected_200():
    power = 100
    hours = 2
    expected = 200

    predicate = functions.calculate_energy(power, hours)

    assert predicate == expected
    return None


def test__calculate_energy__take_0_10_expected_0():
    power = 0
    hours = 2
    expected = 0

    predicate = functions.calculate_energy(power, hours)

    assert predicate == expected
    return None
