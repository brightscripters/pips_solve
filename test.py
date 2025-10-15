# Test rules functionss

import rules
import inspect

def newTest( arg, expect, msg ):
    return { 'arg': arg, 'expect': expect, 'msg': msg}


def testThis( funcTest ):
    for test in funcTest['tests']:
        if funcTest['fn']( test['arg'] ) != test['expect']:
            print('*** FAILED: ', test['msg'], 'in', funcTest['fnName'])
            exit()

########################################################## allSame
funcTest = { 'fn': rules.allSame, 'tests': [], 'fnName':'allSame()' }
tests = funcTest['tests']
tests.append( newTest( [],    None,   'MUST FAIL on empty list' ) )
tests.append( newTest( [1],   None,   'MUST FAIL on single item list' ) )
tests.append( newTest( [1,2], False,  'Should return False.' ) )
tests.append( newTest( [1,1], True,   'Should return True.' ) )

testThis( funcTest )


########################################################## allDifferent
funcTest = { 'fn': rules.allDifferent, 'tests': [], 'fnName':'allDifferent()' }
tests = funcTest['tests']
tests.append( newTest( [],      None,   'MUST FAIL on empty list' ) )
tests.append( newTest( [1],     None,   'MUST FAIL on single item list' ) )
tests.append( newTest( [1,2],   True,   'Should return True.' ) )
tests.append( newTest( [1,2,3], True,   'Should return True.' ) )
tests.append( newTest( [1,2,1], False,  'Should return False.' ) )

testThis( funcTest )

########################################################## makeSumIs
funcTest = { 'fn': rules.makeSumIs(6), 'tests': [], 'fnName':'makeSumIs()' }
tests = funcTest['tests']
tests.append( newTest( [1,2,3],   True,  'Expecting True for total of 6' ) )
tests.append( newTest( [1,2,3,4], False, 'Expecting False for total not 6' ) )

testThis( funcTest )

########################################################## makeSumLt
funcTest = { 'fn': rules.makeSumLt(6), 'tests': [], 'fnName':'makeSumLt()' }
tests = funcTest['tests']
tests.append( newTest( [1,2,2],   True,  'Expecting True for total less than 6' ) )
tests.append( newTest( [1,2,3],   False, 'Expecting False for total == 6' ) )
tests.append( newTest( [1,2,4],   False, 'Expecting False for total > 6' ) )

testThis( funcTest )

########################################################## makeSumGt
funcTest = { 'fn': rules.makeSumGt(6), 'tests': [], 'fnName':'makeSumGt()' }
tests = funcTest['tests']
tests.append( newTest( [1,2,4],   True,  'Expecting True for total > 6' ) )
tests.append( newTest( [1,2,3],   False, 'Expecting False for total == 6' ) )
tests.append( newTest( [1,2,2],   False, 'Expecting False for total < 6' ) )

testThis( funcTest )

print("PASSED")