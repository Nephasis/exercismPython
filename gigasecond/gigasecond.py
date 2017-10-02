from datetime import timedelta

def add_gigasecond(birth):
    return birth+timedelta(days=10**9/86400.0)
