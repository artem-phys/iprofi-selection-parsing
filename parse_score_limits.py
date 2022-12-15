import parse

def parse_score_limits():

    # Сохранённая HTML-страница с расписанием олимпиады
    selection_scores_html = "Я — профессионал _ Отборочный этап.html"

    with open(selection_scores_html, "rb") as sr:

        # Reading
        line = sr.read().decode("utf-8").replace('&nbsp;', ' ')

        # Parsing
        format_string = '<div class="summary-title">{}</div>{}<!-- КАРТОЧКА МАГИСТРАТУРА/СПЕЦИАЛИТЕТ -->{}: {}балл' # </h2>{}{} баллов</div>
        findall_result = parse.findall(format_string, line)

        fields_score_limits_dict = dict()

        for result in findall_result:
            field_name = result[0].strip()
            field_score_limit = int(result[3])

            fields_score_limits_dict[field_name] = field_score_limit

        return fields_score_limits_dict


if __name__ == '__main__':
    fields_score_limits_dict_ = parse_score_limits()
    for (field, score) in fields_score_limits_dict_.items():
        print(field, score)
    print()
    print(f'Успешно обработано {len(fields_score_limits_dict_)} направления')
