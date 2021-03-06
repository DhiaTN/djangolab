from functools import wraps
from django.db import connection

from .logging import getLogger


def query_statistic(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        query_count = len(connection.queries)
        time = 0.0
        result = func(*args, **kwargs)
        queries_number = len(connection.queries) - query_count
        performed_query_list = connection.queries[-queries_number:]
        for query in performed_query_list:
            if query['sql'] == 'BEGIN':
                queries_number -= 1  # ignore begin transaction
            else:
                time += float(query['time'])
        message = "[Statistics] : {total} queries performed in {time}s."
        print(message.format(total=queries_number, time=time))
        return result
    return func_wrapper
