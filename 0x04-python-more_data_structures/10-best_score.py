#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == max_score:
                return key
    return None



if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
