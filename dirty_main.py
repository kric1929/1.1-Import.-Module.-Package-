from datetime import datetime
from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(datetime.now(calculate_salary()))
    print(datetime.now(get_employees()))
