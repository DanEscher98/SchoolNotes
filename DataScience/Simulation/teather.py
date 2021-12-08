#    Arrive at the theater, get in line, and wait to purchase a ticket.
#    Buy a ticket from the box office.
#    Wait in line to have the ticket checked.
#    Get the ticket checked by an usher.
#    Choose whether or not to get in line for the concession stand:
#        If they get in line, then they purchase food.
#        If they don’t get in line, then they skip to the last step.
#    Go find their seat.

import simpy
import random
import statistics

wait_times = []


class Theater(object):
    def __init__(self, env, num_cashiers):
        # In simpy, resources are the parts of the environment
        # (env) that are limited in number.
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3))


def go_to_movies(env, moviegoer, theater):
    # Moviegoer arrives at the teather
    arrival_time = env.now

    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(moviegoer))

    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    if random.choice([True, False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # Moviegoer heads into the theater
    wait_times.append(env.noew - arrival_time)


def run_theater(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    while True:
        yield env.timeout(0.20)
        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))


def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    return average_wait


def calculate_wait_time(arrival_time, departure_time):
    average_wait = statistics.mean(wait_times)
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("input # of ushers working")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1cashier, 1 server, 1 usher.")
        params = [1, 1, 1]
    return params


if __name__ == '__main__':
    random.seed(42)
    num_cashiers, num_servers, num_ushers = get_user_input()

    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=90)

    mins, secs = get_average_wait_time(wait_times)
    print(
        "Running simulation...\n",
        f"The average wait time is {mins} minutes and {secs} seconds.")
