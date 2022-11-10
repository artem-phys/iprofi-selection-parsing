import parse


def from_to_parser(line):

    # Two options of time interval representation
    from_to_result_1 = parse.parse('<b>{}</b> с {} по {}', line)
    from_to_result_2 = parse.parse('с {} <b>{}</b> по {} <b>{}</b>', line)

    if from_to_result_1 is not None:
        date = from_to_result_1[0]
        time_start = from_to_result_1[1]
        time_final = from_to_result_1[2]

        start = date + ' ' + time_start
        final = date + ' ' + time_final

    elif from_to_result_2 is not None:
        time_start = from_to_result_2[0]
        date_start = from_to_result_2[1]
        time_final = from_to_result_2[2]
        date_final = from_to_result_2[3]

        start = date_start + ' ' + time_start
        final = date_final + ' ' + time_final


    return start, final
