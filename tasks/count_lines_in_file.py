def count_lines(filename, skip_header = False):
    line_counter = 0
    with open(filename, 'r') as givenfile:
        for line in givenfile:
            line_counter += 1
    if skip_header == True:
        line_counter = line_counter - 1
    return line_counter

