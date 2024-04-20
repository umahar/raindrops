def convert(number):
    result = ''
    if 0 in {number%3, number%5,number%7}:
        if number % 3 == 0:
            result = result + 'Pling'
        if number % 5 == 0:
            result = result + 'Plang'
        if number % 7 == 0:
            result = result + 'Plong'
        return result
    result = str(number)
    return result