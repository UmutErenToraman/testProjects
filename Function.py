def list_contains(List1, List2):
    check = 0
    for m in List1:
        for n in List2:
            if m == n:
                check = 1
                return check
    return check

