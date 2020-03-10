from collections import Counter


def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def anagram(first_string, second_string):
    if Counter(first_string) == Counter(second_string):
        return True
    else:
        return False


palindrome_string = input('Enter string for check on palindrome: ').lower()
print(f'Palindrom is {palindrome(palindrome_string)}')
print('Enter strings for check on anagram: ')
first_anagram_string = input().lower()
second_anagram_string = input().lower()
print(f'Anagram is {anagram(first_anagram_string, second_anagram_string)}')
