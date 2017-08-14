# -*- coding: utf-8 -*-
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