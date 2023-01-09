from parse_personal_cabinet_fields import parse_personal_cabinet_fields
from parse_selection_round_schedule import parse_selection_round_schedule
from parse_score_limits import parse_score_limits


with open('template_calendar.ics', "r") as template_calendar:
    calendar_string = template_calendar.read()

fields_list, category, score_list = parse_personal_cabinet_fields()
fields_schedule_dict = parse_selection_round_schedule()
fields_score_limits_dict_ = parse_score_limits()

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
print()

pass_counter = 11 # passed with diplomas
approximately_pass_counter = 0

for (field_name, score) in zip(fields_list, score_list):

    print(f'FIELD: {field_name}')
    print(f'YOUR SCORE: {score}')
    print(f'PASS SCORE 2022: {fields_score_limits_dict_.get(field_name, "undefined")}')

    if score != '-':
        if float(score) > fields_score_limits_dict_.get(field_name, 50):
            pass_counter += 1
            print('SUCCESS')
        elif (abs(float(score) - fields_score_limits_dict_.get(field_name, 99)) / fields_score_limits_dict_.get(field_name, 99)) < 0.1:
            approximately_pass_counter += 1
            print('POSSIBLY SUCCESS')
        else:
            print('FAIL')
    print()

print(pass_counter)
print(approximately_pass_counter)



