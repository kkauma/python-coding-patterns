def is_palindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if left == right:
            left += 1
            right -= 1
        else:
            return False
    return True