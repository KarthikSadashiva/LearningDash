'''
@author: Karthik HS
@company: UST Global
@description: This program will generate random sequence of length {{ count }}, with lower limit set by {{ lower_limit}}
                and upper limit being {{ upper_limit }} along with the inter sequence delay of {{ delay }}
'''

import random
import time
import matplotlib.pyplot as plt


def generate_random_sequence(lower_limt, upper_limit, delay, count):
    '''
    :param lower_limt:
    :param upper_limit:
    :param delay:
    :param count:
    :return:
    '''
    random_sequence = []
    for i in range(count):
        random_sequence.append(random.uniform(lower_limt, upper_limit))
        time.sleep(delay)
    return random_sequence


a = generate_random_sequence(280, 320, 0.0001, int(500))
print(a)
plt.plot(a)
plt.show()
