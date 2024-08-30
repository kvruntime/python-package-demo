import tests._context as _context

_context.__file__
from demopack import functions


def test__calculate_energy__take_200_10_expected_200():
    power = 100
    hours = 2
    expected = 200

    predicate = functions.calculate_energy(power, hours)

    assert predicate == expected
    return None
