def lazy_sum_generator(seq, size):
    start = 0
    while start < len(seq):
        end = start + size
        yield sum(seq[start:end])
        start = end
