import parse


def parse_personal_cabinet_fields():

    # Сохранённая HTML-страница личного кабинета Я-Профессионал
    personal_cabinet_html = "Личный кабинет «Я — профессионал».html"

    with open(personal_cabinet_html, "rb") as pc:

        # Reading
        line = pc.read().decode('utf8')

        # Parsing
        format_string_score = '<div class="stage-cards__card">{}<div class="stage-cards__head-text">{}</div>{}Балл отборочного этапа{}<div class="stage-cards__value">{}</div>'
        findall_result = parse.findall(format_string_score, line.strip())

        fields_list = []
        score_list = []

        for result in findall_result:
            cs = result[2]
            ls = cs
            new_result = parse.parse('{}<div class="stage-cards__head-text">{}</div>{}', ls)
            while not (new_result is None):
                cs = new_result[1]
                ls = new_result[2]
                new_result = parse.parse('{}<div class="stage-cards__head-text">{}</div>{}', ls)

            if cs == result[2]:
                full_name = result[1]
            else:
                full_name = cs
            score = result[4] if result[4] != '<div class="stage-cards__empty-text">-' else '-'
            field_name = full_name[:full_name.rfind('(') - 1]
            category = full_name[full_name.rfind('(') + 1: -1]
            fields_list.append(field_name)
            score_list.append(score)

        return fields_list, category, score_list


if __name__ == '__main__':
    fields_list_, category_, score_list_ = parse_personal_cabinet_fields()

    for i in range(len(fields_list_)):
        if score_list_[i] != '-':
            print(fields_list_[i], score_list_[i], sep='\t')

    print()
    print(f'Всего направлений: {len(fields_list_)}')
    print(f'Категория участия: {category_}')
