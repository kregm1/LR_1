def filter_and_write_data(input_channel, output_channel, diff):
    previous_value = None
    for value in input_channel:
        if previous_value is None or abs(value - previous_value) > diff:
            output_channel.send(value)
            previous_value = value


def input_generator():
    for value in input_data:
        yield value


def output_generator():
    while True:
        value = (yield)
        output_data.append(value)
