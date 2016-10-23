#!/usr/bin/python3

"""
08-27 in-class assignment 3

pick a date of birth & a date of death at random; indicate how many days are in that lifetime

"""

import random
import time
from datetime import datetime

def gen_date():
    # dates only between beginning of epoch and now
    # rand = random.random() # dates only between beginning of epoch and now
    
    # fun random dates
    rand = (random.random() + random.random()) / (random.random() - random.random())

    now = time.time()
    random_date = now * rand
    return(random_date)
    
def format_date(epoch):
    return(time.strftime('%Y-%m-%d', time.localtime(epoch)))
    

dates = (gen_date(), gen_date())
# birth_date = gen_date()
# death_date = birth_date
# while int(death_date) <= int(birth_date):
#     death_date = gen_date()

(birth_date, death_date) = (min(dates), max(dates))
    
    
print("Birth date is: {0}".format(format_date(birth_date)))
print("Death date is: {0}".format(format_date(death_date)))

diff = (death_date - birth_date)
diff_days = round(int(diff) / (60 * 60 * 24))

print("This lifetime was", diff_days, "days.")
