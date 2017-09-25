# -*- coding: utf-8 -*-
from functools import wraps

import arrow
import dateutil.parser
from dateutil import tz


def str_to_time(s, time_zone='Asia/Shanghai'):
    """
    str time to datetime
    """
    tzinfo = tz.gettz(time_zone)
    if not s:
        return None
    try:
        dt = dateutil.parser.parse(s).replace(tzinfo=tzinfo)
        return dt
    except ValueError:
        raise ValueError('%s parsed error' % s)


def get_offset_limit(args):
    """
    return offset limit
    """
    if 'offset' in args and 'limit' in args:
       try:
          offset = int(args.get('offset', 0))
       except ValueError:
          offset = 0
       try:
          limit = int(args.get('limit', 20))
       except ValueError:
          limit = 0
    else:
       try:
          page = int(args.get('page', 1))
       except ValueError:
          page = 1
       try:
          limit = int(args.get('per_page', 20))
       except ValueError:
          limit = 20
       offset = limit * (page - 1)
    return offset, limit


def format_result(fields=None, **formats):
    '''
    :param data:  dict
    :param fields:  list
    :param formats:  field target type date_created: ISOString
    :return:
    '''
    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            data, _ = await func(*args, **kwargs)
            for field in fields:
                value = getattr(data, field)
                format = formats.get(field, 'ISOString')
                if format == 'ISOString':
                    data[field] = arrow.Arrow.fromdate(value).isoformat()
            return data
        return wrapper
    return decorator


def split_datetime(datetime, date_format="YYYY-MM-DD", time_format="HH:MM"):
    '''
    :param datetime: datetime object
    :return: date str and time str ex: 2017-03-02, 12:09
    '''
    tzinfo = tz.gettz('Asia/Shanghai')
    adatetime = arrow.Arrow.fromdate(datetime).to(tzinfo)
    return adatetime.format(date_format), adatetime.format(time_format)
