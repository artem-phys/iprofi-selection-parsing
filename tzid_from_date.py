def tzid_from_date(date):

    months_dict = {'ноября': 11, 'декабря': 12}

    day, month_name, time = date.split()
    hours = time[:time.find(':')].zfill(2)
    minutes = time[time.find(':') + 1:]

    tzid = f'Europe/Moscow:2022{months_dict[month_name]}{day}T{hours}{minutes}00'

    return tzid
