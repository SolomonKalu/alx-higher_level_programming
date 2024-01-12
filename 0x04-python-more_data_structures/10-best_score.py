#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    large = max(a_dictionary.values())
    for x, value in a_dictionary.items():
	if value is large:
	    return x
