
import numpy as np
import matplotlib.pyplot as plt

def pi_run(nums,loops):
    pi_avg = 0
    pi_value_list = []
    for i in range(loops):
        value = 0
        x = np.random.uniform(0,1,nums).tolist()
        y = np.random.uniform(0,1,nums).tolist()
        for j in range(nums):
            z = np.sqrt(x[j]*x[j] + y[j]*y[j])
            if z <= 1:
                value += 1
            float_value = float(value)
            pi_value = float_value*4/nums
            pi_value_list.append(pi_value)
            pi_avg += pi_value

    pi = pi_avg/loops
    ind = range(1, loops+1)
    fig = plt.plot(ind,pi_value_list)
    return(pi, fig)
    #plt.show()

pi_run(1000, 100)
