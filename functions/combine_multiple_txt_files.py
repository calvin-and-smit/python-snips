def combine_multiple_txt_files(file_list, output_file, headers = True):
    """
    This function combines multiple text files into a single file (blank lines will be included as well)
    params file_list: List of files to be combined
    params output_file: Output file
    headers: Boolean indicating whether individual files have headers or not, default is True
    return: None
    """
    total_lines = 0
    if headers == True:
        with open(output_file, 'a') as output_file:
            file_counter = 1
            for each_file in file_list:
                line_counter = 1
                if file_counter == 1:
                    with open(each_file, 'r') as input_file:
                        for each_line in input_file:
                            _ = output_file.write(each_line)
                            line_counter += 1
                    file_counter += 1
                else:
                    with open(each_file, 'r') as input_file:
                        for each_line in input_file:
                            if line_counter == 1:
                                line_counter += 1
                                continue
                            _ = output_file.write(each_line)
                            line_counter += 1
                total_lines = total_lines + line_counter
    else:
        with open(output_file, 'a') as output_file:
            for each_file in file_list:
                line_counter = 1
                with open(each_file, 'r') as input_file:
                    for each_line in input_file:
                        _ = output_file.write(each_line)
                        line_counter += 1
                total_lines = total_lines + line_counter
    print(f'Total lines written: {total_lines:,}')
