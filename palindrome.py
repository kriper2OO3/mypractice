def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("Введите строку: ")

print("Возможно это палиндром, а может и нет")