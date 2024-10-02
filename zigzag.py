import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not


try:
    while True: # Main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces
            indent += 1
            if indent == 10:
                # Change direction
                indentIncreasing = False 
            
        else:
            # Decrease the number of spaces
            indent -= 1
            if indent == 0:
                # Change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit
