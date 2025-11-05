# Test rules functions

import rules
import pips
import pprint


def newTestItem( arg, expect, msg = 'Unexpected' ):
    return { 'arg': arg, 'expect': expect, 'msg': msg}


def testThis( funcTest ):
    for test in funcTest['tests']:
        
        if test['arg'] == None:
            result = funcTest['fn']()
        else:
            result = funcTest['fn']( test['arg'] )

        if  result != test['expect']:
            print('*** FAILED: ', test['msg'], 'in', funcTest['fnName'] + '(',test['arg'],')')
            exit()


oneTwo = pips.piece(1,2)
board = [[-1]] * 10

########################################################## pips.rotationsHere()
testFn = lambda coordinate: pips.rotationsHere(coordinate, board)
funcTest = { 'fn': testFn, 'tests': [], 'fnName':'rotationsHere()' }
tests = funcTest['tests']

tests.append( newTestItem( (0,0), [1] ) )
tests.append( newTestItem( (0,1), [1,3] ) )
tests.append( newTestItem( (0,8), [1,3] ) )
tests.append( newTestItem( (0,9), [3] ) )

testThis( funcTest )
exit()

########################################################## piece.rotate
testFn = lambda rotation: oneTwo.rotate(rotation).getRotOffsets()
funcTest = { 'fn': testFn, 'tests': [], 'fnName':'pips.piece().rotate' }
tests = funcTest['tests']

tests.append( newTestItem( 0, [  1, 0]  ) )
tests.append( newTestItem( 1, [  0, 1]  ) )
tests.append( newTestItem( 2, [ -1, 0] ) )
tests.append( newTestItem( 3, [  0,-1] ) )

testThis( funcTest )


########################################################## piece.reverse()
testFn = lambda : oneTwo.reverse().nums
funcTest = { 'fn': testFn, 'tests': [], 'fnName':'pips.piece().reverse()' }
tests = funcTest['tests']

tests.append( newTestItem( None, pips.piece(2,1).nums  ) )


testThis( funcTest )

########################################################## allSame
funcTest = { 'fn': rules.allSame, 'tests': [], 'fnName':'allSame()' }
tests = funcTest['tests']
tests.append( newTestItem( [],    None,   'MUST FAIL on empty list' ) )
tests.append( newTestItem( [1],   None,   'MUST FAIL on single item list' ) )
tests.append( newTestItem( [1,2], False,  'Should return False.' ) )
tests.append( newTestItem( [1,1], True,   'Should return True.' ) )

testThis( funcTest )


########################################################## allDifferent
funcTest = { 'fn': rules.allDifferent, 'tests': [], 'fnName':'allDifferent()' }
tests = funcTest['tests']
tests.append( newTestItem( [],      None,   'MUST FAIL on empty list' ) )
tests.append( newTestItem( [1],     None,   'MUST FAIL on single item list' ) )
tests.append( newTestItem( [1,2],   True,   'Should return True.' ) )
tests.append( newTestItem( [1,2,3], True,   'Should return True.' ) )
tests.append( newTestItem( [1,2,1], False,  'Should return False.' ) )

testThis( funcTest )

########################################################## makeSumIs
funcTest = { 'fn': rules.makeSumIs(6), 'tests': [], 'fnName':'makeSumIs()' }
tests = funcTest['tests']
tests.append( newTestItem( [1,2,3],   True,  'Expecting True for total of 6' ) )
tests.append( newTestItem( [1,2,3,4], False, 'Expecting False for total not 6' ) )

testThis( funcTest )

########################################################## makeSumLt
funcTest = { 'fn': rules.makeSumLt(6), 'tests': [], 'fnName':'makeSumLt()' }
tests = funcTest['tests']
tests.append( newTestItem( [1,2,2],   True,  'Expecting True for total less than 6' ) )
tests.append( newTestItem( [1,2,3],   False, 'Expecting False for total == 6' ) )
tests.append( newTestItem( [1,2,4],   False, 'Expecting False for total > 6' ) )

testThis( funcTest )

########################################################## makeSumGt
funcTest = { 'fn': rules.makeSumGt(6), 'tests': [], 'fnName':'makeSumGt()' }
tests = funcTest['tests']
tests.append( newTestItem( [1,2,4],   True,  'Expecting True for total > 6' ) )
tests.append( newTestItem( [1,2,3],   False, 'Expecting False for total == 6' ) )
tests.append( newTestItem( [1,2,2],   False, 'Expecting False for total < 6' ) )

testThis( funcTest )

print("PASSED\n")