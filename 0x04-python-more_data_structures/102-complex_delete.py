def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)
    
    for key in keys_to_delete:
        del a_dictionary[key]
    
    return a_dictionary


if __name__ == "__main__":
    from print_sorted_dictionary import print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
