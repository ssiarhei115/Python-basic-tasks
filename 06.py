def count_symbol(s:str)->str:
    """ Modify the input string so that each symbol is preceded with a symbol's counter """
    
    t = s[0]
    count = 0
    result = ''
    
    for item in s:
        if item == t:
            count += 1
        else:
            result += str(count) + t
            t = item
            count = 1
            
    result += str(count) + t 
    
    return result


def inp_validator(s:str)->bool:
    """ Validate the input string """
    
    # check for non zero input length
    # check if length of input < 30 (for the safety purpose)
    if len(s) == 0 or len(s) > 30:
        return False
    
    # check if entered symbols can be converted to type int
    try:
        for symb in s: 
            int(symb)
        check_1 = True
    except:
        check_1 = False
    
    # check for non zero first character
    check_2 = s[0] != '0'

    return check_1 and check_2


# main function
def count_symbol_loop(iter=9):
    """ Loop request for new input. Modify the input string with symbols counters. 

    Args:
        iter (int, optional): number of iterrations. Defaults to 10
    Returns:
        string: modified string with symbols counters after each iterration
    """
       
    while True:
        inp_1 = input('New try for look-and-say sequence? (y/n):').strip()
        
        if inp_1 != 'y':
            print('EXIT')
            break
        else:
            inp_2 = input ('Number to start (int > 0):').strip()
            
            if not inp_validator(inp_2):
                print(70*'-', '\n!! CHECK THE INPUT !!\nUSE integer numbers > 0, at least ONE character is required!!\n', 70*'-')
                continue
            
            print(f'Start number {inp_2} is VALID')
            
        for n in range(iter):
            inp_2 = count_symbol(inp_2)
            print(f'{n} -', inp_2)
        print('*')        
        
        
count_symbol_loop()
