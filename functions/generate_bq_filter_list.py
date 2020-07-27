def generate_bq_filter_list(element_list, is_numeric = False):
    if is_numeric == True:
        return ','.join(str(e) for e in element_list)
    else:
        counter = 1
        filter_list = ''
        for each_element in element_list:
            if counter == 1:
                filter_list = "'" + str(each_element) + "'"
                counter += 1
            else:
                filter_list = filter_list + ",'" + str(each_element) + "'"
                counter += 1
        return filter_list

