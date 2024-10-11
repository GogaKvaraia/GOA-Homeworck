def manual_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

#__________________________________________________________

def manual_replace(original, old, new):
    return original.replace(old, new)

#___________________________________________________________
def manual_append(lst, item):
    lst += [item]  # Or use lst.append(item)
    return lst
