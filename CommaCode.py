def comma_code(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

# Example usage:
my_list = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(my_list)
print("Formatted list:", result)
