from ingineerpackage.customtypes import Number
from ingineerpackage.executor import app


def calculate_energy(power:Number, hours:int)->Number:
    return power*hours
    
def running_script():
    return app()