import parse


def parse_personal_cabinet_fields():

    # Сохранённая HTML-страница личного кабинета Я-Профессионал
    personal_cabinet_html = "Личный кабинет «Я — профессионал».html"

    with open(personal_cabinet_html, "rb") as pc:

        # Reading
        line = pc.read().decode('utf8')

        # Parsing
        format_string = '<div class="stage-cards__head-text">{}</div>'
        findall_result = parse.findall(format_string, line.strip())

        fields_list = []

        for result in findall_result:
            full_name = result[0]
            field_name = full_name[:full_name.rfind('(') - 1]
            category = full_name[full_name.rfind('(') + 1: -1]
            fields_list.append(field_name)

        return fields_list, category


if __name__ == '__main__':
    fields_list_, category_ = parse_personal_cabinet_fields()

    print(*fields_list_, sep='\n')
    print()
    print(f'Всего направлений: {len(fields_list_)}')
    print(f'Категория участия: {category_}')
