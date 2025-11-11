def count_symbol(s:str)->str:
    """ Count the quantity of each number in a sequence """
    
    t = s[0]
    c = 0
    result = ''
    
    for item in s:
        if item == t:
            c += 1
        else:
            result += str(c) + t
            t = item
            c = 1
            
    result += str(c) + t 
    
    return result


def inp_validator(s:str)->bool:
    """ Validate the input """
    
    # check if entered symbols can be converted to type int
    try:
        for symb in s: 
            int(symb)
        check_1 = True
    except:
        check_1 = False
    
    # check if length of input > 0
    check_2 = len(s) > 0
        
    return check_1 and check_2 


# main function
def count_symbol_loop(step=10):
    """Modify input string with symbols counter. Loop request

    Args:
        step (int, optional): number of iterrations. Defaults to 10
    Returns:
        string: modified string after every iterration (step)
    """
       
    while True:
        inp_1 = input('New look-and-say sequence? (y/n):').strip()
        
        if inp_1 != 'y':
            print('EXIT')
            break
        else:
            inp_2 = input ('Number to start (int > 0):')
            
            if not inp_validator(inp_2):
                print('CHECK the input! USE integer numbers > 0, at least ONE number is required!!')
                continue
            
            print(f'Start number: {inp_2}')
            
        for n in range(step):
            inp_2 = count_symbol(inp_2)
            print(f'{n} -', inp_2)
        
        
count_symbol_loop()