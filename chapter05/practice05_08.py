import pprint


def get_busy_days(_agenda):
    _busy_days = list()
    _schedule = _agenda['schedule']
    for _day_schedule in _schedule:
        _events = _day_schedule.get('events')
        if _events:
            _busy_days.append(_day_schedule['day'])
    return _busy_days


def get_events(_agenda, _day):
    _events = list()
    _schedule = _agenda['schedule']
    for _day_schedule in _schedule:
        if _day_schedule['day'] == _day:
            _day_events = _day_schedule.get('events')
            if _day_events:
                _events.extend(_day_events)
    return _events


if __name__ == '__main__':
    print("\n--- original dict ---")
    agenda = {
        'employee': 'Johny Brown',
        'schedule': [
            {
                'day': 'Monday',
                'events': [
                    {
                        'start': '09:00 AM',
                        'end': '10:00 AM',
                        'name': 'Doctor Appointment'
                    },
                    {
                        'start': '11:00 AM',
                        'end': '11:30 AM',
                        'name': 'Team meeting'
                    }
                ]
            },
            {
                'day': 'Wednesday',
                'events': [
                    {
                        'start': '01:00 PM',
                        'end': '02:00 PM',
                        'name': 'Lunch Break',
                    },
                    {
                        'start': '04:00 PM',
                        'end': '05:00 PM',
                        'name': 'Scrum meeting',
                    },
                ]
            },
            {
                'day': 'Friday',
                'events': [],
            },
            {
                'day': 'Sunday',
            },
        ],
    }
    pprint.pprint(agenda, indent=4)

    print("\n--- busy days ---")
    print(get_busy_days(agenda))

    print("\n--- agenda events for Monday ---")
    for event in get_events(agenda, 'Monday'):
        print(event)
