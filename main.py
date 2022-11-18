from parse_personal_cabinet_fields import parse_personal_cabinet_fields
from parse_selection_round_schedule import parse_selection_round_schedule


with open('template_calendar.ics', "r") as template_calendar:
    calendar_string = template_calendar.read()

fields_list, category = parse_personal_cabinet_fields()
fields_schedule_dict = parse_selection_round_schedule()

calendar_file = 'iprofi_selection_round.ics'

with open(calendar_file, "w", encoding='utf-8') as calendar:
    calendar.write(calendar_string)

    for field_name in fields_list:
        for tzid_start, tzid_final in fields_schedule_dict[field_name]['time_slots']:
            calendar.write("BEGIN:VEVENT" + "\n")
            calendar.write(f"DTSTART;TZID={tzid_start}" + "\n")
            calendar.write(f"DTEND;TZID={tzid_final}" + "\n")
            calendar.write(f"SUMMARY:{field_name} ({fields_schedule_dict[field_name]['time_limit']})" + "\n")
            calendar.write(f"DESCRIPTION:{fields_schedule_dict[field_name]['summary']}" + "\n")
            calendar.write("TRANSP:OPAQUE" + "\n")
            calendar.write("CATEGORIES:Отборочный этап Я-Профессионал" + "\n")
            calendar.write(f"END:VEVENT" + "\n")

    calendar.write(f"END:VCALENDAR")

print(f'{len(fields_list)} directions succesefully added to .ics')
