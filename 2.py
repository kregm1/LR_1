def copy_if_different_by_threshold(input_generator, threshold):
    prev_value = None
    for value in input_generator:
        if prev_value is None or abs(value - prev_value) > threshold:
            yield value
            prev_value = value


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def copy_if_different_by_levenshtein(input_generator, threshold):
    prev_value = None
    for value in input_generator:
        if prev_value is None or levenshtein(value, prev_value) >= threshold:
            yield value
            prev_value = value


def main():
    input_values = [1, 1.1, 2, 2.2, 2.3, 3.0, 2.4, 3.1, 3.1, 4.0]
    threshold = 0.5

    filtered_values_generator = copy_if_different_by_threshold(input_values, threshold)

    for value in filtered_values_generator:
        print(f'Output value: {value}')


    input_values_string = ["hello", "h3llo", "hell", "help", "helper", "helpp"]
    threshold = 2

    filtered_values_generator_string = copy_if_different_by_levenshtein(input_values_string, threshold)

    for value in filtered_values_generator_string:
        print(f'Output value string: {value}')


if __name__ == '__main__':
    main()
