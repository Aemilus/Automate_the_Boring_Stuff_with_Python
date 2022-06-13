"""
Write a program to find out how often a streak of six heads or a streak of six tails
comes up in a randomly generated list of heads and tails.
"""

import random

_NR_EXPERIMENTS = 10_000
_NR_FLIPS_PER_EXPERIMENT = 100


def generate_experiment_coin_flips():
    _result = list()
    for _flip_count in range(_NR_FLIPS_PER_EXPERIMENT):
        _result.append(random.choice(('H', 'T')))
    return _result


def get_streak_count(_result):
    _streaks_count = 0  # counts number of valid coin flip streaks

    _heads_streak = 0
    _tails_streak = 0
    for _side in _result:
        # check each flip coin result and increment as long as is the same result as previous, else reset the counter
        if _side == 'T':
            _tails_streak += 1
            _heads_streak = 0
        if _side == 'H':
            _heads_streak += 1
            _tails_streak = 0
        # on 6 consecutive same flip coin result then increase the valid streaks counter
        if _tails_streak == 6 or _heads_streak == 6:
            _streaks_count += 1
            _tails_streak = 0
            _heads_streak = 0
    return _streaks_count


if __name__ == '__main__':
    total_streaks = 0
    for experiment in range(_NR_EXPERIMENTS):
        streaks_count = 0
        experiment_result = generate_experiment_coin_flips()
        streaks_count += get_streak_count(experiment_result)
        total_streaks += streaks_count

        # print('Experiment:', experiment_result)
        print('Streaks count:', streaks_count)
        print("Chance of streak: {:.2%}".format(streaks_count / _NR_FLIPS_PER_EXPERIMENT))

    print("Average change of streak: {:.2%}".format(total_streaks / _NR_EXPERIMENTS / _NR_FLIPS_PER_EXPERIMENT))
