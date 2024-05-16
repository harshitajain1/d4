##create a function to accept 3 paramter and join them return ouput should be a dictinory 
##ouput :-
##       { val1: paramter1, val2: parameter2, val3: paramter3, joinText: joined text of 3 paramter}	
		
print('This is a dictionary')

def dictName(val1,val2,val3):
    join_Name = f'{val1}{val2}{val3}'
    result = {
        'Name1':val1,
        'Name2':val2,
        'Name3':val3,
        'joinName':join_Name
    }
    return result


val1 = "DIC"
val2 = "TION"
val3 = "ARY"
output = dictName(val1,val2,val3)

print(output)