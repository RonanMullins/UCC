# ScriptName: main.py
# Author: Ronan Mullins 121107333

from my_functions import *


def main():

# # 1
#     print(firsts("mississippi"))
#     # Should return ⇒ "misp" 
#     print(firsts("abcdefg"))
#     # Should return ⇒ "abcdefg" 
#     print(firsts("aaaaaaaa"))
#     # Should return ⇒ "a" 
#     print(firsts(""))
#     # Should return ⇒ "" 


# # 2
#     print(F("poop", "pee"))
#     # Should return ⇒ ["p", "p"]
#     print(F("Dog", "Dog"))
#     # Should return ⇒ ["D", "o", "g"]

#3
    print(iter_factorial(5))
    # Should return ⇒ 120
    print(iter_factorial(8))
    # Should return ⇒ 40320
    print(iter_factorial(0.3))
    # Should return ⇒ "Oops"
    print(iter_factorial(0))
    # Should return ⇒ 1
    print(iter_factorial(-5))
    # Should return ⇒ "Oops"
    print(iter_factorial("5"))
    # Should return ⇒ "Oops"

# # 4
#     print(removeVowels("the brown fox jumped over the lazy dog"))
#     # Should return ⇒ "th brwn fx jmpd vr th lzy dg"



# 5
    # print(hailstone(10))
    # # Should return ⇒ [10, 5, 16, 8, 4, 2, 1]
    # # print(hailstone(1))
    # # # Should return ⇒ [1]
    # print(hailstone(4000))
    # Should return ⇒ [4000, 2000, 1000, 500, 250, 125, 376, 188, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    # print(hailstone(0))
    # # Should return ⇒ "Oops"
    # print(hailstone(-10))
    # # Should return ⇒ "Oops"
    # print(hailstone(1.1))
    # # Should return ⇒ "Oops"
    # print(hailstone((1, 1)))
    # # Should return ⇒ "Oops"
    # print(hailstone([1, 1]))
    # # Should return ⇒ "Oops"
    # print(hailstone("Chrono Trigger"))
    # # Should return ⇒ "Oops"

# # 6
#     print(chooseLargest([1, 2, 3, 4, 5], [2, 2, 9, 0, 9]))
#     # Should return ⇒ [2, 2, 9, 4, 9]
#     print(chooseLargest([3, 3], [3, 3]))
#     # # Should return ⇒ [3, 3]
#     print(chooseLargest(4, 1))
#     # Should return ⇒ [4]
#     print(chooseLargest(4.20, 6.9))
#     # Should return ⇒ [6.9]
#     print(chooseLargest([9, 6, 3], [9, 9]))
#     # Should return ⇒ "Oops"
#     print(chooseLargest("Chrono", "Trigger"))
#     # Should return ⇒ "Oops"
#     print(chooseLargest([9, 6, 3], "Trigger"))
#     # Should return ⇒ "Oops"
#     print(chooseLargest("Chrono", 16))
#     # Should return ⇒ "Oops"

# # 7 
#     print(loop_the_loop("poop", "pee"))
#     # Should return ⇒ ["pp", "pe", "pe", "op", "oe", "oe", "op", "oe", "oe", "pp", "pe", "pe"]
#     print(loop_the_loop("y", "o"))
#     # Should return ⇒ ["yo"]
#     print(loop_the_loop("100,000", "KM"))
#     # Should return ⇒ ["1K", "1M", "0K", "0M", "0K", "0M", ",K", ",M", "0K", "0M", "0K", "0M", "0K", "0M"]
#     print(loop_the_loop(420, 69))
#     # Should return ⇒ "Oops"
#     print(loop_the_loop(420.69, "Trigger"))
#     # Should return ⇒ "Oops"
#     print(loop_the_loop(["Poo", "poo"], ["Pee", "pee"]))
#     # Should return ⇒ "["PP", "Pe", "Pe", "Pp", "Pe", "Pe", "oP", "oe", "oe", "op", "oe", "oe", "oP", "oe", "oe", "op", "oe", "oe", "pP", "pe", "pe", "pp", "pe", "pe", "oP", "oe", "oe", "op", "oe", "oe", "oP", "oe", "oe", "op", "oe", "oe"]"
#     print(loop_the_loop(("Poo", "poo"), ("Pee", "pee")))
#     # Should return ⇒ "["PP", "Pe", "Pe", "Pp", "Pe", "Pe", "oP", "oe", "oe", "op", "oe", "oe", "oP", "oe", "oe", "op", "oe", "oe", "pP", "pe", "pe", "pp", "pe", "pe", "oP", "oe", "oe", "op", "oe", "oe", "oP", "oe", "oe", "op", "oe", "oe"]"
#     print(loop_the_loop(("Chr", "ono"), "Trigger"))
#     # Should return ⇒ "["CT", "Cr", "Ci", "Cg", "Cg", "Ce", "Cr", "hT", "hr", "hi", "hg", "hg", "he", "hr", "rT", "rr", "ri", "rg", "rg", "re", "rr", "oT", "or", "oi", "og", "og", "oe", "or", "nT", "nr", "ni", "ng", "ng", "ne", "nr", "oT", "or", "oi", "og", "og", "oe", "or"]"

if __name__ == "__main__":

    main()
