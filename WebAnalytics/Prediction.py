# Prediction

# Every week the number of unique visitors grows with 7% compared to the previous week.

# Giving an integer number N representing the number of unique visitors at the end of this week and an integer number W

# Your task is to

#     write a function that prints to the standard output (stdout) the number of unique visitors we are going to have after W weeks
#     please round the final result downwards to the nearest integer (e.g both 7.1 and 7.9 are rounded to 7)

# Note that your function will receive the following arguments:

#     n
#         which is an integer representing the number N described above
#     w
#         which is an integer representing the number W described above

# Data constraints

#     the value for N will not exceed 10000
#     the value for W will not exceed 50

# Example
# Input 	Output

# n: 10
# w: 3
	

# 12

# n: 40
# w: 1
	

# 42

__author__="Kevin Aloysius"


def compute_prediction(n,w):
    visitor=n
    # n is the number of unique visitors and w is the week,
    # the following code predicts the number of unique visitors after w weeks if the
    # traffic of unique visitors increases every week by 7%

    for i in range(w):
        n = n + n*0.07
        final = int(round(n))
    print "Given the Unique Visitors ",visitor," unique visitors after week ",w," will be ",final

compute_prediction(40,1)
