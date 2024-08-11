import pytest
from solutions.CHK.checkout_solution import checkout


def test_checkout():
    basket = checkout("A, B, C, D")
    assert basket == 115


def test_checkout_empty():
    basket = checkout("")
    assert basket == 0


def test_checkout_invalid():
    basket = checkout("A, B, C, E")
    assert basket == 140


def test_checkout_invalid2():
    basket = checkout("A, B, C, 4")
    assert basket == -1


def test_checkout_valid():
    basket = checkout("A,B,C,D")
    assert basket == 115


def test_special_offer_checkout():
    basket = checkout("A, A, A, B, C, D")
    assert basket == 195


def test_special_offer_checkout2():
    basket = checkout("A, A, C, B, B, D")
    assert basket == 180


def test_special_offer_checkout3():
    basket = checkout("A, A, A, A")
    assert basket == 180


def test_special_offer_checkout4():
    basket = checkout("A, A, A, B, B, B")
    assert basket == 205


def test_special_offer_checkout5():
    basket = checkout("A, A, A, A, A, A")
    assert basket == 250


def test_special_offer_checkout6():
    basket = checkout("A, A, A, A, A, A, A")
    assert basket == 300


def test_checkout2():
    basket = checkout("A")
    assert basket == 50


def test_checkout3():
    basket = checkout("B")
    assert basket == 30


def test_checkout4():
    basket = checkout("C")
    assert basket == 20


def test_checkout5():
    basket = checkout("D")
    assert basket == 15


def test_checkout6():
    basket = checkout("a")
    assert basket == -1


def test_checkout7():
    basket = checkout("AAAA")
    assert basket == 180


def test_checkout8():
    basket = checkout("aaaa")
    assert basket == -1

def test_checkout9():
    basket = checkout("-")
    assert basket == -1


def test_checkout10():
    assert checkout("ABCa") == -1


def test_checkout11():
    assert checkout("AxA") == -1


def test_checkout12():
    assert checkout("ABCD") == 115
    assert checkout("AA") == 100
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180
    assert checkout("AAAAA") == 200
    assert checkout("AAAAAA") == 250
    assert checkout("B") == 30
    assert checkout("BB") == 45
    assert checkout("BBB") == 75
    assert checkout("BBBB") == 90
    assert checkout("ABCDABCD") == 215
    assert checkout("BABDDCAC") == 215
    assert checkout("AAABB") == 175
    assert checkout("AAAAAAABBBBBCCCD") == (200)+(2*50)+(2*45)+(30)+(3*20)+(15)


def test_checkout13():
    assert checkout("ABCEE") == 150
    assert checkout("AECDE") == 165
    assert checkout("AECDEE") == 205
    assert checkout("ABEEEE") == 210
    assert checkout("ABBEEEE") == 210


def test_checkout14():
    assert checkout("EEEEBBA") == 210
    assert checkout("EEEEBBB") == 190


def test_checkout15():
    assert checkout("AAFFF") == 120
    assert checkout("AAFFFF") == 130
    assert checkout("AAFFFFFF") == 140
    assert checkout("AAFF") == 120
    assert checkout("AAF") == 110
    assert checkout("AAAAAFFFF") == 230


def test_checkout16():
    assert checkout("AAAEEBFFF") == 230
    assert checkout("FFFAAAEEBF") == 240


def test_checkout17():
    assert checkout("AAAEEBFFFZ") == 280
    assert checkout("FFFAAAEEBFVVVV") == 420

def test_checkout18():
    assert checkout("UUU") == 120
    assert checkout("UUUU") == 120

def test_checkout19():
    assert checkout("ZZZX") ==

# id = CHK_R4_002, req = checkout(""), resp = 0
# id = CHK_R4_003, req = checkout("A"), resp = 50
# id = CHK_R4_004, req = checkout("B"), resp = 30
# id = CHK_R4_005, req = checkout("C"), resp = 20
# id = CHK_R4_006, req = checkout("D"), resp = 15
# id = CHK_R4_007, req = checkout("E"), resp = 40
# id = CHK_R4_008, req = checkout("F"), resp = 10
# id = CHK_R4_009, req = checkout("G"), resp = 20
# id = CHK_R4_010, req = checkout("H"), resp = 10
# id = CHK_R4_011, req = checkout("I"), resp = 35
# id = CHK_R4_012, req = checkout("J"), resp = 60
# id = CHK_R4_013, req = checkout("K"), resp = 80
# id = CHK_R4_014, req = checkout("L"), resp = 90
# id = CHK_R4_015, req = checkout("M"), resp = 15
# id = CHK_R4_016, req = checkout("N"), resp = 40
# id = CHK_R4_017, req = checkout("O"), resp = 10
# id = CHK_R4_018, req = checkout("P"), resp = 50
# id = CHK_R4_019, req = checkout("Q"), resp = 30
# id = CHK_R4_020, req = checkout("R"), resp = 50
# id = CHK_R4_021, req = checkout("S"), resp = 30
# id = CHK_R4_022, req = checkout("T"), resp = 20
# id = CHK_R4_023, req = checkout("U"), resp = 40
# id = CHK_R4_024, req = checkout("V"), resp = 50
# id = CHK_R4_025, req = checkout("W"), resp = 20
# id = CHK_R4_026, req = checkout("X"), resp = 90
# id = CHK_R4_027, req = checkout("Y"), resp = 10
# id = CHK_R4_028, req = checkout("Z"), resp = 50
# id = CHK_R4_029, req = checkout("a"), resp = -1
# id = CHK_R4_030, req = checkout("-"), resp = -1
# id = CHK_R4_031, req = checkout("ABCa"), resp = -1
# id = CHK_R4_032, req = checkout("AxA"), resp = -1
# id = CHK_R4_033, req = checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 965
# id = CHK_R4_034, req = checkout("A"), resp = 50
# id = CHK_R4_035, req = checkout("AA"), resp = 100
# id = CHK_R4_036, req = checkout("AAA"), resp = 130
# id = CHK_R4_037, req = checkout("AAAA"), resp = 180
# id = CHK_R4_038, req = checkout("AAAAA"), resp = 200
# id = CHK_R4_039, req = checkout("AAAAAA"), resp = 250
# id = CHK_R4_040, req = checkout("AAAAAAA"), resp = 300
# id = CHK_R4_041, req = checkout("AAAAAAAA"), resp = 330
# id = CHK_R4_042, req = checkout("AAAAAAAAA"), resp = 380
# id = CHK_R4_043, req = checkout("AAAAAAAAAA"), resp = 400
# id = CHK_R4_044, req = checkout("P"), resp = 50
# id = CHK_R4_045, req = checkout("PP"), resp = 100
# id = CHK_R4_046, req = checkout("PPP"), resp = 150
# id = CHK_R4_047, req = checkout("PPPP"), resp = 200
# id = CHK_R4_048, req = checkout("PPPPP"), resp = 200
# id = CHK_R4_049, req = checkout("PPPPPP"), resp = 250
# id = CHK_R4_050, req = checkout("PPPPPPP"), resp = 300
# id = CHK_R4_051, req = checkout("PPPPPPPP"), resp = 350
# id = CHK_R4_052, req = checkout("PPPPPPPPP"), resp = 400
# id = CHK_R4_053, req = checkout("PPPPPPPPPP"), resp = 400
# id = CHK_R4_054, req = checkout("UUU"), resp = 80 (120)
# id = CHK_R4_055, req = checkout("UUUU"), resp = 120
# id = CHK_R4_056, req = checkout("UUUUU"), resp = 160
# id = CHK_R4_057, req = checkout("UUUUUUUU"), resp = 240
# id = CHK_R4_058, req = checkout("UUUUUUUU"), resp = 240
# id = CHK_R4_059, req = checkout("EE"), resp = 80
# id = CHK_R4_060, req = checkout("EEB"), resp = 80
# id = CHK_R4_061, req = checkout("EEEB"), resp = 120
# id = CHK_R4_062, req = checkout("EEEEBB"), resp = 160
# id = CHK_R4_063, req = checkout("BEBEEE"), resp = 160
# id = CHK_R4_064, req = checkout("RRR"), resp = 150
# id = CHK_R4_065, req = checkout("RRRQ"), resp = 150
# id = CHK_R4_066, req = checkout("RRRRQ"), resp = 200
# id = CHK_R4_067, req = checkout("RRRRRRQQ"), resp = 300
# id = CHK_R4_068, req = checkout("RRRQRQRR"), resp = 300
# id = CHK_R4_069, req = checkout("A"), resp = 50
# id = CHK_R4_070, req = checkout("AA"), resp = 100
# id = CHK_R4_071, req = checkout("AAA"), resp = 130
# id = CHK_R4_072, req = checkout("AAAA"), resp = 180
# id = CHK_R4_073, req = checkout("AAAAA"), resp = 200
# id = CHK_R4_074, req = checkout("AAAAAA"), resp = 250
# id = CHK_R4_075, req = checkout("H"), resp = 10
# id = CHK_R4_076, req = checkout("HH"), resp = 20
# id = CHK_R4_077, req = checkout("HHH"), resp = 30
# id = CHK_R4_078, req = checkout("HHHH"), resp = 40
# id = CHK_R4_079, req = checkout("HHHHH"), resp = 45
# id = CHK_R4_080, req = checkout("HHHHHH"), resp = 55
# id = CHK_R4_081, req = checkout("HHHHHHH"), resp = 65
# id = CHK_R4_082, req = checkout("HHHHHHHH"), resp = 75
# id = CHK_R4_083, req = checkout("HHHHHHHHH"), resp = 85
# id = CHK_R4_084, req = checkout("HHHHHHHHHH"), resp = 80
# id = CHK_R4_085, req = checkout("HHHHHHHHHHH"), resp = 90
# id = CHK_R4_086, req = checkout("HHHHHHHHHHHH"), resp = 100
# id = CHK_R4_087, req = checkout("HHHHHHHHHHHHH"), resp = 110
# id = CHK_R4_088, req = checkout("HHHHHHHHHHHHHH"), resp = 120
# id = CHK_R4_089, req = checkout("HHHHHHHHHHHHHHH"), resp = 125
# id = CHK_R4_090, req = checkout("HHHHHHHHHHHHHHHH"), resp = 135
# id = CHK_R4_091, req = checkout("HHHHHHHHHHHHHHHHH"), resp = 145
# id = CHK_R4_092, req = checkout("HHHHHHHHHHHHHHHHHH"), resp = 155
# id = CHK_R4_093, req = checkout("HHHHHHHHHHHHHHHHHHH"), resp = 165
# id = CHK_R4_094, req = checkout("HHHHHHHHHHHHHHHHHHHH"), resp = 160
# id = CHK_R4_095, req = checkout("V"), resp = 50
# id = CHK_R4_096, req = checkout("VV"), resp = 90
# id = CHK_R4_097, req = checkout("VVV"), resp = 130
# id = CHK_R4_098, req = checkout("VVVV"), resp = 180
# id = CHK_R4_099, req = checkout("VVVVV"), resp = 220
# id = CHK_R4_100, req = checkout("VVVVVV"), resp = 260
# id = CHK_R4_101, req = checkout("B"), resp = 30
# id = CHK_R4_102, req = checkout("BB"), resp = 45
# id = CHK_R4_103, req = checkout("BBB"), resp = 75
# id = CHK_R4_104, req = checkout("BBBB"), resp = 90
# id = CHK_R4_105, req = checkout("NNN"), resp = 120
# id = CHK_R4_106, req = checkout("NNNM"), resp = 120
# id = CHK_R4_107, req = checkout("NNNNM"), resp = 160
# id = CHK_R4_108, req = checkout("NNNNNNMM"), resp = 240
# id = CHK_R4_109, req = checkout("NNNMNMNN"), resp = 240
# id = CHK_R4_110, req = checkout("FF"), resp = 20
# id = CHK_R4_111, req = checkout("FFF"), resp = 20
# id = CHK_R4_112, req = checkout("FFFF"), resp = 30
# id = CHK_R4_113, req = checkout("FFFFFF"), resp = 40
# id = CHK_R4_114, req = checkout("FFFFFF"), resp = 40
# id = CHK_R4_115, req = checkout("K"), resp = 80
# id = CHK_R4_116, req = checkout("KK"), resp = 150
# id = CHK_R4_117, req = checkout("KKK"), resp = 230
# id = CHK_R4_118, req = checkout("KKKK"), resp = 300
# id = CHK_R4_119, req = checkout("Q"), resp = 30
# id = CHK_R4_120, req = checkout("QQ"), resp = 60
# id = CHK_R4_121, req = checkout("QQQ"), resp = 80
# id = CHK_R4_122, req = checkout("QQQQ"), resp = 110
# id = CHK_R4_123, req = checkout("QQQQQ"), resp = 140
# id = CHK_R4_124, req = checkout("QQQQQQ"), resp = 160
# id = CHK_R4_125, req = checkout("V"), resp = 50
# id = CHK_R4_126, req = checkout("VV"), resp = 90
# id = CHK_R4_127, req = checkout("VVV"), resp = 130
# id = CHK_R4_128, req = checkout("VVVV"), resp = 180
# id = CHK_R4_129, req = checkout("H"), resp = 10
# id = CHK_R4_130, req = checkout("HH"), resp = 20
# id = CHK_R4_131, req = checkout("HHH"), resp = 30
# id = CHK_R4_132, req = checkout("HHHH"), resp = 40
# id = CHK_R4_133, req = checkout("HHHHH"), resp = 45
# id = CHK_R4_134, req = checkout("HHHHHH"), resp = 55
# id = CHK_R4_135, req = checkout("HHHHHHH"), resp = 65
# id = CHK_R4_136, req = checkout("HHHHHHHH"), resp = 75
# id = CHK_R4_137, req = checkout("HHHHHHHHH"), resp = 85
# id = CHK_R4_138, req = checkout("HHHHHHHHHH"), resp = 80
# id = CHK_R4_139, req = checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 1880
# id = CHK_R4_140, req = checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"), resp = 1880
# id = CHK_R4_141, req = checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH"), resp = 1640
# id = CHK_R4_001, req = checkout("PPPPQRUVPQRUVPQRUVSU"), resp = 740


