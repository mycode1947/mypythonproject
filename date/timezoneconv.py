#!/usr/bin/env python
from datetime import datetime
from pytz import timezone
format="%Y-%m-%d %H:%M:%S %Z%z"
date_now=datetime.now(timezone('UTC'))
print "Printing localtime zone"
print date_now.strftime(format)
sg_date=date_now.astimezone(timezone('Asia/Singapore'))
print "Singapore timezone is "
sg_date=sg_date.strftime(format)
print sg_date
