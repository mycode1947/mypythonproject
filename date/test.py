#!/usr/bin/env python
from datetime import datetime
from pytz import timezone
dt_str='Jul 26, 2016 08:30:45'
dt=datetime.strptime(dt_str,'%b %d, %Y %H:%M:%S')
print dt
print type(dt)
