from calendar import month_abbr
from datetime import datetime as dt


class DateTime:

    def __init__(self):
        pass

    def day(self):
        return str(dt.now().day).zfill(2)

    def month(self):
        return month_abbr[dt.now().month]
    
    def year(self):
        return str(dt.now().year)
    
    def hour(self):
        return str(dt.now().hour).zfill(2)

    def minute(self):
        return str(dt.now().minute).zfill(2)

