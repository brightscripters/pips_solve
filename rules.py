
import inspect
import os

# Rule functions
# Takes group
# Returns True when passed and False for failed
# Returns None upon invalid input


##############################
def exitInfo( frame ):
    info = inspect.getframeinfo(frame)
    print(f"Exiting { os.path.basename(info.filename)}, line {info.lineno}")
    exit()

##############################
def allSame(group):
    if len(group) < 2:
        print('*** ERROR! A group must have at least two items. Not ', len(group))
        return None

    prev = group[0]
    for item in group[1:]:
        if prev != item:
            return False

    return True


##############################
def allDifferent(group):
    if len(group) < 2:
        print('*** ERROR! A group must have at least two items. Not ', len(group))
        return None
    
    if len(group) == len(set(group)):
        return True

    return False


##############################
# Create a function
# Takes a group
# Returns bool

def makeSumIs(sumIs):
    return lambda group: sum(group) == sumIs


# Greater than
def makeSumGt(sumGt):
    return lambda group: sum(group) > sumGt


# Less than
def makeSumLt(sumLt):
    return lambda group: sum(group) < sumLt