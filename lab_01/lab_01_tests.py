import lab_01 as test

dlr = test.damerauLevenstein
lrnomatrix = test.levensteinRecoursion
lrmatrix = test.levensteinRecoursionMatrix
lmatrix = test.levensteinMatrix


def testEqualForSelfAndFtDamerau(a, b, rightanswer):
    if dlr(a, b) == lrnomatrix(a, b) == lrmatrix(a, b) == lmatrix(a, b) == rightanswer:
        print(f"Passed")
    else:
        print("ACHTUNG!!!")
        print(f"{a} {b} - NOT OK")
        print(lrnomatrix(a, b))
        print(lrmatrix(a, b))
        print(lmatrix(a, b))

def testDemarauSolo(a, b, rightanswer):
    if dlr(a, b) == rightanswer:
        print(f"Damerau passed")
    else:
        print("ACHTUNG!!!")
        print(f"DAMERAU {a} {b} - NOT OK")
        print(f"EXPECT {rightanswer} got {dlr(a,b)}")

def testForScreen(a, b, rightanswer):
    print("String one:", a)
    print("String two:", b)
    print("expect answer:", rightanswer)
    print("Levenstein matrix result", lmatrix(a, b))
    print("Levenstein recoursion result", lrnomatrix(a, b))
    print("Levenstein recoursion-matrix result", lrmatrix(a, b))

def damerautest(a, b, rightanswer):
    #damerausimpletest
    print("String one:", a)
    print("String two:", b)
    print("expect answer:", rightanswer)
    print("Damerau-Levenstein matrix result", dlr(a, b))


#testEqualForSelfAndFtDamerau("", "",  0)
#testForScreen("", "",  0)
# testEqualForSelfAndFtDamerau("1", "1",  0)
# testEqualForSelfAndFtDamerau("1", "2",  1)
# testEqualForSelfAndFtDamerau("12", "12",  0)
# testEqualForSelfAndFtDamerau("123", "12",  1)
# testForScreen("kitten", "mittens",  2)
# testEqualForSelfAndFtDamerau("1234", "1233",  1)
# testEqualForSelfAndFtDamerau("1248", "1349",  2)
# testForScreen("", "12345",  5)
damerautest("supercat", "uppercta", 3)
# testEqualForSelfAndFtDamerau("5677", "1234",  4)
# testEqualForSelfAndFtDamerau("123456", "12345",  1)
# testEqualForSelfAndFtDamerau("13579", "12345",  4)
# testEqualForSelfAndFtDamerau("123", "",  3)
# testEqualForSelfAndFtDamerau("kitten", "mittens",  2)
#
# testDemarauSolo("1234", "1324",  1)

mas = 1
print(mas.__sizeof__())

testEqualForSelfAndFtDamerau("1234", "1",  3)