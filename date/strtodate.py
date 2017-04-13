#!/usr/bin/env python
from datetime import datetime
from pytz import timezone
format="%Y-%m-%d %H:%M:%S %Z%z"
dt=datetime.strptime('Aug 5 1982 12:30 AM','%b %d %Y %I:%M %p')
print dt
