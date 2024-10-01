from demopack.customtypes import Number
from demopack.executor import app


def calculate_energy(power: Number, hours: int) -> Number:
    return power * hours


def running_script():
    return app()
