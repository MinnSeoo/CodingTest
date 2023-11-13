def solution(my_string, is_suffix):
    return 1 if my_string.startswith(is_suffix) or my_string.endswith(is_suffix) else 0