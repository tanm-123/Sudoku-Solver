from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
        for i in range(1,4):
                for j in range(1,10):
                        if pos[0]==i and pos[1]==j:
                                if int(j/3)==j/3:
                                        return (int(j/3))
                                else:
                                        return (j//3 + 1)
        for i in range(4,7):
                for j in range (1,10):
                        if pos[0]==i and pos[1]==j:
                                if int(j/3)==j/3:
                                        return (int(j/3 +3))
                                else:
                                        return(j//3 + 4)
        for i in range(7,10):
                for j in range (1,10):
                        if pos[0]==i and pos[1]==j:
                                if int(j/3)==j/3:
                                        return (int(j/3 +6))
                                else:
                                        return(j//3 + 7)

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
        if pos[1]/3==int(pos[1]/3) and pos[0]/3==int(pos[0]/3):
                return(9)
        if pos[1]/3==int(pos[1]/3) and pos[0]/3!=int(pos[0]/3):
                return(3+3*((pos[0]%3)-1))
        if pos[1]/3!=int(pos[1]/3) and pos[0]/3==int(pos[0]/3):
                return(pos[1]%3 +6)
        if pos[1]/3!=int(pos[1]/3) and pos[0]/3!=int(pos[0]/3):
                return( pos[1]%3 + 3*((pos[0]%3)-1))

def get_block(sudoku:List[List[int]], x: int) -> List[int]:
        z=[]
        if x%3!=0 and x!=7 and x!=8:
                for i in range((x//3)+3**(x//3),(x//3)+3**(x//3)+3):
                        for j in range(3*(x%3)-2,3*(x%3)+1):
                                z.append(sudoku[i-1][j-1])
        if x==7 or x==8:
                for i in range (7,10):
                        for j in range(3*(x%3)-2,3*(x%3)+1):
                                z.append(sudoku[i-1][j-1])
        else:
                for i in range(x-2,x+1):
                        for j in range(7,10):
                                z.append(sudoku[i-1][j-1])
                                
        return list(z)
        

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
        l=[]
        for j in range(1,10):
                l.append(sudoku[i-1][j-1])
        return list(l)

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
        l=[]
        for j in range (1,10):
                l.append(sudoku[j-1][x-1])
        return list(l)

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
        for i in range(1,10):
                for j in range(1,10):
                        if (sudoku[i-1][j-1])==0:
                                return(i,j)
                        
        return (-1,-1)

def valid_list(lst: List[int])-> bool:
        for i in lst:
                for j in range (lst.index(i)+1,len(lst)):
                        if i==lst[j] and i!=0:
                                return False
        return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
        l=[]
        for i in range(0,9):
                l.append([])
                for j in range(0,9):
                        l[i].append(sudoku[j][i])
        for i in range (0,9):
               if valid_list(sudoku[i])==True and valid_list(l[i])==True and valid_list(get_block(sudoku,i+1))==True:
                       return True
        return False


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
        q=[1,2,3,4,5,6,7,8,9]
        r=[]
        tr=get_row(sudoku,pos[0])
        tc=get_column(sudoku,pos[1])
        x=get_block_num(sudoku,[pos[0],pos[1]])
        tb=get_block(sudoku,x)
        for i in range(0,9):
                for j in range(0,9):
                        if q[i]==tr[j]:
                                r.append(tr[j])
                        if q[i]==tc[j]:
                                r.append(tc[j])
                        if q[i]==tb[j]:
                                r.append(tb[j])
        s=[]
        for i in r:
                if i not in s:
                        s.append(i)
        
        for i in s:
                q.remove(i)
        #q.append(sudoku[pos[0]-1][pos[1]-1])
        q.append(0)
        q.remove(0)
        return list(q)

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
        sudoku[pos[0]-1][pos[1]-1]=num
        return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
        sudoku[pos[0]-1][pos[1]-1]=0
        return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
        pos=find_first_unassigned_position(sudoku)
        #t.append(pos)
        if pos==(-1,-1):
                if valid_sudoku(sudoku)==True:
                        return (True, sudoku)
                else:
                        return(False, sudoku)
        else:
                l=get_candidates(sudoku,pos)
                #z.append(l)
                #if len(l)==0:
                        #undo_move(sudoku,t[0])
                        #t.pop(0)
                        #for j in range(len(t)-1,0,-1):
                                #t.pop(j)
                        
                for i in l:
                        make_move(sudoku,pos,i)
                        if sudoku_solver(sudoku)[0]==True:
                                return (True, sudoku)
                        else:
                                undo_move(sudoku,pos)
                return (False, sudoku)
                
                #if len(l)!=0:
                        #make_move(sudoku,pos,l[0])
                        #z[-1].pop(0)
                #else:
                        #
                                #
                                        #undo_move(sudoku,t[i-1])
                                        #
                                                #t.pop(j)
                                        #make_move(sudoku,t[i-1],z[i-1][0])
                                        #sudoku_solver(sudoku)
                                        #break
                        #if len(l)==0:
                                #return(False, sudoku)


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
        #print("Testcases for In Lab evaluation")
        #print("Get Block Number:")
        #print(get_block_num(sudoku,(4,4)))
        #print(get_block_num(sudoku,(7,2)))
        #print(get_block_num(sudoku,(2,6)))
        #print("Get Block:")
        #print(get_block(sudoku,4))
        #print(get_block(sudoku,5))
        #print(get_block(sudoku,9))
        #print("Get Row:")
        #print(get_row(sudoku,3))
        #print(get_row(sudoku,5))
        #print(get_row(sudoku,9))
        #print(get_position_inside_block(sudoku,[5,7]))
        #print("Get Column:")
        #print(get_column(sudoku,3))
        #print(get_column(sudoku,5))
        #print(get_column(sudoku,9))
        #print(find_first_unassigned_position(sudoku))
        print(valid_list([7,0,5,0,7,0,0,0,0,0,7,1,0,0,0,0,6,0]))
        #print(valid_list([5,3,0,0,7,0,0,0,0]))
        print(valid_sudoku(sudoku))
        #print(get_candidates(sudoku,[9,9]))
        #print(make_move(sudoku,[7,9],5))
        #print(undo_move(sudoku,[3,9]))
        
# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)
