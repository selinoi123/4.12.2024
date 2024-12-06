#START 1
def is_valid_parentheses(x: str) -> bool:
    arr = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in x:
        if char in brackets.values():
            arr.append(char)
        elif char in brackets.keys():
            if len(arr) == 0 or arr[-1] != brackets[char]:
                return False
            else:
                return True

    return len(arr) == 0
#END

#START 2
def remove_duplicates(arr):
    if not arr:
        return []

    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)
        else:
            i += 1
    return arr
#END

#START 3
def merge_sorted_lists(list1, list2):
    connecting = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            connecting.append(list1[i])
            i += 1
        else:
            connecting.append(list2[j])
            j += 1

    while i < len(list1):
        connecting.append(list1[i])
        i += 1

    while j < len(list2):
        connecting.append(list2[j])
        j += 1

    return connecting
#END