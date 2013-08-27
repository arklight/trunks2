# sleep1 from midnight to 3 and get up
sleep1 = 3  # hours
# sleep2 from 3:15am till 6:15am and get up
sleep2 = 3  # hours


def total_sleep():
    total_sleep = sleep1 + sleep2
    print str(total_sleep) + ' hours of sleep'

total_sleep()