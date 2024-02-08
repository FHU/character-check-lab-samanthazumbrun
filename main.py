def check_character(word, index):
    char = word[index]
    type = ''
    if char.isalpha():
        type = 'letter'
    elif char.isspace():
        type = 'white space'
    elif char.isdigit():
        type = 'digit'
    else:
        type = 'unknown'
    
    return type
            


if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
    #test