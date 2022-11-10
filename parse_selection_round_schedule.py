import parse

from from_to_parser import from_to_parser
from tzid_from_date import tzid_from_date


def parse_selection_round_schedule():

    # Сохранённая HTML-страница с расписанием олимпиады
    selection_round_html = "Я — профессионал _ Расписание отборочного этапа.html"

    with open(selection_round_html, "rb") as sr:

        # Reading
        line = sr.read().decode("utf-8").replace('&nbsp;', ' ')

        # Parsing
        format_string = '<div class="summary-title">{}</div>{}<div class="styled_text">{}</div>'
        findall_result = parse.findall(format_string, line)

        fields_schedule_dict = dict()

        for result in findall_result:
            field_name = result[0]
            field_schedule_info = result[2]

            time_limit_parsing_result = parse.parse('{}будет <b>{}</b>{}', field_schedule_info)
            time_limit = time_limit_parsing_result[1] if time_limit_parsing_result else 'Нет ограничения на время выполнения'

            fields_schedule_dict[field_name] = {}
            fields_schedule_dict[field_name]['time_limit'] = time_limit
            fields_schedule_dict[field_name]['summary'] = field_schedule_info.strip().replace('\n', ' ')
            fields_schedule_dict[field_name]['time_slots'] = []

            li_options = parse.findall('<li>{}</li>', field_schedule_info)

            if any(True for _ in li_options):
                for li_option in li_options:
                    line = li_option[0]
                    start, final = from_to_parser(line)
                    fields_schedule_dict[field_name]['time_slots'].append((tzid_from_date(start), tzid_from_date(final)))
            else:
                start, final = from_to_parser(line)
                fields_schedule_dict[field_name]['time_slots'].append((tzid_from_date(start), tzid_from_date(final)))

        return fields_schedule_dict


if __name__ == '__main__':
    fields_schedule_dict_ = parse_selection_round_schedule()
    print(fields_schedule_dict_)
