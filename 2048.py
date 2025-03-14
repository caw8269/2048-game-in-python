#2048.py

#importing logic.py file where all logic functions used have been written
import logic

#Driver Code
if __name__ == '__main__':
    mat = logic.start_game()

while(True):
    #taking the user input for the next step
    x = input("press a command")

    #we have to move up
    if(x == 'W' or x == 'w'):

        #call the move_function
        mat, flag = logic.move_up(mat)

        #get the current state and print it
        status = logic.get_current_state(mat)
        print(status)

        #if game not over then continue and add a new 2
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        
        #else break the loop
        else:
            break

    #the above process will be followed in case of each  tpye of move below

    #to move down
    elif(x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    #to move left
    elif(x == 'A' or x == 'a'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    
    #to move right
    elif(x == 'D' or x == 'd'):
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    else:
        print('Invalid key pressed')

    #print the matrix after each move
    for i in range(4):
        print(mat[i])