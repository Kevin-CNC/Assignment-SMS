

def getNumeralInput(msg,outputmsg):
    userInput = str(input(msg))
    try:
        userInput = int(userInput)    
    except ValueError:
        print(outputmsg)
        return None
    except Exception as e:
        print(f"Something went wrong:\n{e}")
        return None
    
    return(userInput)