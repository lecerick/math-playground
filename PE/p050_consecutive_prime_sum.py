"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from timeit import default_timer as timer
from datetime import timedelta

start = timer()

# Generate a list of primes using the seive method
threshold = 10 ** 6
is_prime = [True for n in range(0,threshold)]
is_prime[0]=False
is_prime[1]=False
primes = []
for i in range(2,threshold):
    if is_prime[i]==True:
        for multiple in range(i*2,threshold,i):
            is_prime[multiple]=False
        primes.append(i)

print(len(primes))
# Try combinations of consecutive primes
max = 0
max_p = 0
for start_index in range(len(primes)):
    for end_index in range(start_index+1,len(primes)):
        count = end_index-start_index
        if count > max:
            sum_of_primes = sum([primes[i] for i in range(start_index,end_index)])
            if sum_of_primes > threshold: # or count <= max
                break
            if sum_of_primes in primes and count > max:
                max = count
                max_p = sum_of_primes
                # print('{} sums from {} to {} with count {}'.format(max_p,primes[start_index],primes[end_index], max))

end = timer()
print('The answer is {}, which can be written as the sum of {} consecutive primes (TIME = {})'.format(max_p,max,str(timedelta(seconds=end-start))))