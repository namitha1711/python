def comma_code(lst):
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return lst[0]
    else:
        return ', '.join(lst[:-1]) + ', and ' + lst[-1]

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
main()
