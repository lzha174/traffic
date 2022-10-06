from datetime import datetime, timedelta

import pandas

start_time_sim = datetime(2021, 5, 3, 0,0,0)

def getDateTime(n, out_date_format_str = '%m/%d/%Y %H:%M:%S'):
    n = int(n)
    final_time = start_time_sim + timedelta(seconds=n)

    final_time_str = final_time.strftime(out_date_format_str)
    return final_time_str

def format_time(n=15):
    return getDateTime(n)


