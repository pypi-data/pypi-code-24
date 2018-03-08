#!/usr/bin/env python

# Copyright (c) 2017, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from collections import namedtuple
import unittest

import numpy

import uproot

def basest(array):
    while getattr(array, "base", None) is not None:
        array = array.base
    return array

class TestTree(unittest.TestCase):
    def runTest(self):
        pass

    ###################################################### basket

    def test_flat_basket(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["i8"]
        interpretation = branch._normalize_interpretation(None)
        entrystart, entrystop = branch._normalize_entrystartstop(None, None)
        local_entrystart, local_entrystop = branch._localentries(0, entrystart, entrystop)

        one = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        two = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        self.assertTrue(numpy.array_equal(one, numpy.array([-15, -14, -13], dtype=">i8")))
        self.assertTrue(basest(one) is basest(two))

        three = branch.basket(0)
        self.assertTrue(numpy.array_equal(three, numpy.array([-15, -14, -13], dtype=">i8")))
        self.assertFalse(basest(one) is basest(three))

        buf = numpy.zeros(10, dtype=numpy.float64)
        four = branch.basket(0, interpretation.toarray(buf))
        self.assertTrue(numpy.array_equal(four, numpy.array([-15, -14, -13], dtype=">i8")))
        self.assertTrue(basest(four) is buf)

    def test_regular_basket(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["ai8"]
        interpretation = branch._normalize_interpretation(None)
        entrystart, entrystop = branch._normalize_entrystartstop(None, None)
        local_entrystart, local_entrystop = branch._localentries(0, entrystart, entrystop)

        one = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        two = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        self.assertTrue(numpy.array_equal(one, numpy.array([[-14, -13, -12]], dtype=">i8")))
        self.assertTrue(basest(one) is basest(two))

        three = branch.basket(0)
        self.assertTrue(numpy.array_equal(three, numpy.array([[-14, -13, -12]], dtype=">i8")))
        self.assertFalse(basest(one) is basest(three))

        self.assertEqual(branch.basket(0, interpretation.to(todims=(3,))).shape, (1, 3))
        self.assertEqual(branch.basket(0, interpretation.to(todims=())).shape, (3,))
        self.assertEqual(branch.basket(0, interpretation.to(todims=(1,))).shape, (3, 1))
        self.assertEqual(branch.basket(0, interpretation.to(todims=(1, 1))).shape, (3, 1, 1))
        self.assertEqual(branch.basket(0, interpretation.to(todims=(1, 3))).shape, (1, 1, 3))

        buf = numpy.zeros(10, dtype=numpy.float64)
        four = branch.basket(0, interpretation.toarray(buf))
        self.assertTrue(numpy.array_equal(four, numpy.array([-14, -13, -12], dtype=">i8")))
        self.assertTrue(basest(four) is buf)

    def test_irregular_basket(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["Ai8"]
        interpretation = branch._normalize_interpretation(None)
        entrystart, entrystop = branch._normalize_entrystartstop(None, None)
        local_entrystart, local_entrystop = branch._localentries(0, entrystart, entrystop)

        one = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        two = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        self.assertTrue(numpy.array_equal(one[0], numpy.array([], dtype=">i8")))
        self.assertTrue(numpy.array_equal(one[1], numpy.array([-15], dtype=">i8")))
        self.assertTrue(basest(one.content) is basest(two.content))

        three = branch.basket(0)
        self.assertTrue(numpy.array_equal(three[0], numpy.array([], dtype=">i8")))
        self.assertTrue(numpy.array_equal(three[1], numpy.array([-15], dtype=">i8")))

    def test_strings_basket(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["str"]
        interpretation = branch._normalize_interpretation(None)
        entrystart, entrystop = branch._normalize_entrystartstop(None, None)
        local_entrystart, local_entrystop = branch._localentries(0, entrystart, entrystop)

        one = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        two = branch._basket(0, interpretation, local_entrystart, local_entrystop, None, None)
        self.assertTrue(one.tolist() == [b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5"])
        self.assertFalse(basest(one.jaggedarray.content) is basest(two.jaggedarray.content))

        three = branch.basket(0)
        self.assertTrue(three.tolist() == [b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5"])

    ###################################################### baskets

    def test_flat_baskets(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["i8"]
        expectation = [[-15, -14, -13], [-12, -11, -10], [-9, -8, -7], [-6, -5, -4], [-3, -2, -1], [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
        self.assertEqual([x.tolist() for x in branch.baskets()], expectation)
        self.assertEqual([x.tolist() for x in branch.iterate_baskets()], expectation)

    def test_regular_baskets(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["ai8"]
        expectation = [[[-14, -13, -12]], [[-13, -12, -11]], [[-12, -11, -10]], [[-11, -10, -9]], [[-10, -9, -8]], [[-9, -8, -7]], [[-8, -7, -6]], [[-7, -6, -5]], [[-6, -5, -4]], [[-5, -4, -3]], [[-4, -3, -2]], [[-3, -2, -1]], [[-2, -1, 0]], [[-1, 0, 1]], [[0, 1, 2]], [[1, 2, 3]], [[2, 3, 4]], [[3, 4, 5]], [[4, 5, 6]], [[5, 6, 7]], [[6, 7, 8]], [[7, 8, 9]], [[8, 9, 10]], [[9, 10, 11]], [[10, 11, 12]], [[11, 12, 13]], [[12, 13, 14]], [[13, 14, 15]], [[14, 15, 16]], [[15, 16, 17]]]
        self.assertEqual([x.tolist() for x in branch.baskets()], expectation)
        self.assertEqual([x.tolist() for x in branch.iterate_baskets()], expectation)

    def test_irregular_baskets(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["Ai8"]
        expectation = [[[], [-15]], [[-15, -13]], [[-15, -13, -11]], [[-15, -13, -11, -9]], [[], [-10]], [[-10, -8]], [[-10, -8, -6]], [[-10, -8, -6, -4]], [[], [-5]], [[-5, -3]], [[-5, -3, -1]], [[-5, -3, -1, 1]], [[], [0]], [[0, 2]], [[0, 2, 4]], [[0, 2, 4, 6]], [[], [5]], [[5, 7]], [[5, 7, 9]], [[5, 7, 9, 11]], [[], [10]], [[10, 12]], [[10, 12, 14]], [[10, 12, 14, 16]]]
        self.assertEqual([len(y) for x in expectation for y in x], [0, 1, 2, 3, 4] * 6)
        self.assertEqual([x.tolist() for x in branch.baskets()], expectation)
        self.assertEqual([x.tolist() for x in branch.iterate_baskets()], expectation)

    def test_strings_baskets(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["str"]
        expectation = [[b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5"], [b"hey-6", b"hey-7", b"hey-8", b"hey-9", b"hey-10"], [b"hey-11", b"hey-12", b"hey-13", b"hey-14", b"hey-15"], [b"hey-16", b"hey-17", b"hey-18", b"hey-19", b"hey-20"], [b"hey-21", b"hey-22", b"hey-23", b"hey-24", b"hey-25"], [b"hey-26", b"hey-27", b"hey-28", b"hey-29"]]
        self.assertEqual([x.tolist() for x in branch.baskets()], expectation)
        self.assertEqual([x.tolist() for x in branch.iterate_baskets()], expectation)

    ###################################################### array

    def test_flat_array(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["i8"]
        expectation = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for entrystart, entrystop in [(None, None), (1, None), (1, 2), (1, 10), (10, 11), (10, 20), (6, 12), (6, 13)]:
            self.assertEqual(branch.array(entrystart=entrystart, entrystop=entrystop).tolist(), expectation[entrystart:entrystop])

    def test_regular_array(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["ai8"]
        expectation = [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]]
        for entrystart, entrystop in [(None, None), (1, None), (1, 2), (1, 10), (10, 11), (10, 20), (6, 12), (6, 13)]:
            self.assertEqual(branch.array(entrystart=entrystart, entrystop=entrystop).tolist(), expectation[entrystart:entrystop])

    def test_irregular_array(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["Ai8"]
        expectation = [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]]
        self.assertEqual([len(x) for x in expectation], [0, 1, 2, 3, 4] * 6)
        for entrystart, entrystop in [(None, None), (1, None), (1, 2), (1, 10), (10, 11), (10, 20), (6, 12), (6, 13)]:
            self.assertEqual(branch.array(entrystart=entrystart, entrystop=entrystop).tolist(), expectation[entrystart:entrystop])

    def test_strings_array(self):
        branch = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]["str"]
        expectation = [b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5", b"hey-6", b"hey-7", b"hey-8", b"hey-9", b"hey-10", b"hey-11", b"hey-12", b"hey-13", b"hey-14", b"hey-15", b"hey-16", b"hey-17", b"hey-18", b"hey-19", b"hey-20", b"hey-21", b"hey-22", b"hey-23", b"hey-24", b"hey-25", b"hey-26", b"hey-27", b"hey-28", b"hey-29"]
        for entrystart, entrystop in [(None, None), (1, None), (1, 2), (1, 10), (10, 11), (10, 20), (6, 12), (6, 13)]:
            self.assertEqual(branch.array(entrystart=entrystart, entrystop=entrystop).tolist(), expectation[entrystart:entrystop])

    ###################################################### iterate

    def test_flat_iterate(self):
        tree = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]
        expectation = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for n in 1000, 5, 6, 7:
            self.assertEqual([x.tolist() for (x,) in tree.iterate("i8", n, outputtype=tuple)], [expectation[x : x + n] for x in range(0, len(expectation), n)])

    def test_regular_iterate(self):
        tree = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]
        expectation = [[-14, -13, -12], [-13, -12, -11], [-12, -11, -10], [-11, -10, -9], [-10, -9, -8], [-9, -8, -7], [-8, -7, -6], [-7, -6, -5], [-6, -5, -4], [-5, -4, -3], [-4, -3, -2], [-3, -2, -1], [-2, -1, 0], [-1, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17]]
        for n in 1000, 5, 6, 7:
            self.assertEqual([x.tolist() for (x,) in tree.iterate("ai8", n, outputtype=tuple)], [expectation[x : x + n] for x in range(0, len(expectation), n)])

    def test_irregular_iterate(self):
        tree = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]
        expectation = [[], [-15], [-15, -13], [-15, -13, -11], [-15, -13, -11, -9], [], [-10], [-10, -8], [-10, -8, -6], [-10, -8, -6, -4], [], [-5], [-5, -3], [-5, -3, -1], [-5, -3, -1, 1], [], [0], [0, 2], [0, 2, 4], [0, 2, 4, 6], [], [5], [5, 7], [5, 7, 9], [5, 7, 9, 11], [], [10], [10, 12], [10, 12, 14], [10, 12, 14, 16]]
        for n in 1000, 5, 6, 7:
            self.assertEqual([x.tolist() for (x,) in tree.iterate("Ai8", n, outputtype=tuple)], [expectation[x : x + n] for x in range(0, len(expectation), n)])

    def test_strings_iterate(self):
        tree = uproot.open("tests/samples/sample-6.10.05-uncompressed.root")["sample"]
        expectation = [b"hey-0", b"hey-1", b"hey-2", b"hey-3", b"hey-4", b"hey-5", b"hey-6", b"hey-7", b"hey-8", b"hey-9", b"hey-10", b"hey-11", b"hey-12", b"hey-13", b"hey-14", b"hey-15", b"hey-16", b"hey-17", b"hey-18", b"hey-19", b"hey-20", b"hey-21", b"hey-22", b"hey-23", b"hey-24", b"hey-25", b"hey-26", b"hey-27", b"hey-28", b"hey-29"]
        for n in 1000, 5, 6, 7:
            self.assertEqual([x.tolist() for (x,) in tree.iterate("str", n, outputtype=tuple)], [expectation[x : x + n] for x in range(0, len(expectation), n)])

    ###################################################### old tests

    def test_branch_array(self):
        file = uproot.open("tests/samples/simple.root")
        repr(file)

        tree = file["tree"]
        repr(tree)
        repr(tree["one"])

        self.assertEqual(tree["one"].array().tolist(), [1, 2, 3, 4])
        self.assertEqual(tree["two"].array().tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(tree["three"].array().tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        self.assertEqual(tree["one"].array().tolist(), [1, 2, 3, 4])
        self.assertEqual(tree["two"].array().tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(tree["three"].array().tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        tree = file["tree"]
        self.assertEqual(tree["one"].array().tolist(), [1, 2, 3, 4])
        self.assertEqual(tree["two"].array().tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(tree["three"].array().tolist(), [b"uno", b"dos", b"tres", b"quatro"])

    def test_tree_arrays(self):
        file = uproot.open("tests/samples/simple.root")

        tree = file["tree"]
        arrays = tree.arrays()
        self.assertEqual(arrays[b"one"].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[b"two"].tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(arrays[b"three"].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        # get arrays again
        arrays = tree.arrays()
        self.assertEqual(arrays[b"one"].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[b"two"].tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(arrays[b"three"].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        # get tree again
        tree = file["tree"]
        arrays = tree.arrays()
        self.assertEqual(arrays[b"one"].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[b"two"].tolist(), numpy.array([1.1, 2.2, 3.3, 4.4], dtype=numpy.float32).tolist())
        self.assertEqual(arrays[b"three"].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

    def test_tree_iterator1(self):
        # one big array
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=1000):
            self.assertEqual(arrays[b"data"].tolist(), list(range(46)))

        # size is equal to basket size (for most baskets)
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=6):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 6, 46))))
            i += 6

        # size is smaller
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=3):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 3, 46))))
            i += 3
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=4):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 4, 46))))
            i += 4

        # size is larger
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=12):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 12, 46))))
            i += 12
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=10):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 10, 46))))
            i += 10

        # singleton case
        i = 0
        for arrays in uproot.open("tests/samples/foriter.root")["foriter"].iterate(entrysteps=1):
            self.assertEqual(arrays[b"data"].tolist(), list(range(i, min(i + 1, 46))))
            i += 1

    def test_tree_iterator2(self):
        words = [b"zero", b"one", b"two", b"three", b"four", b"five", b"six", b"seven", b"eight", b"nine", b"ten", b"eleven", b"twelve", b"thirteen", b"fourteen", b"fifteen", b"sixteen", b"seventeen", b"eighteen", b"ninteen", b"twenty", b"twenty-one", b"twenty-two", b"twenty-three", b"twenty-four", b"twenty-five", b"twenty-six", b"twenty-seven", b"twenty-eight", b"twenty-nine", b"thirty"]

        # one big array
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=1000):
            self.assertEqual(arrays[b"data"].tolist(), words)

        # size is equal to basket size (for most baskets)
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=6):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 6])
            i += 6

        # size is smaller
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=3):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 3])
            i += 3
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=4):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 4])
            i += 4

        # size is larger
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=12):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 12])
            i += 12
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=10):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 10])
            i += 10

        # singleton case
        i = 0
        for arrays in uproot.open("tests/samples/foriter2.root")["foriter2"].iterate(entrysteps=1):
            self.assertEqual(arrays[b"data"].tolist(), words[i:i + 1])
            i += 1

    def test_tree_iterator3(self):
        source = list(range(46))

        # one big array
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=1000):
            self.assertEqual(arrays[b"data"].tolist(), source)

        # size is equal to basket size (for most baskets)
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=6):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 6])
            i += 6
            if i > 45: i = 0

        # size is smaller
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=3):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 3])
            i += 3
            if i > 45: i = 0
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=4):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 4])
            i += 4
            if i > 45: i = 0

        # size is larger
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=12):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 12])
            i += 12
            if i > 45: i = 0
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=10):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 10])
            i += 10
            if i > 45: i = 0

        # singleton case
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter.root", "tests/samples/foriter.root"], "foriter", entrysteps=1):
            self.assertEqual(arrays[b"data"].tolist(), source[i : i + 1])
            i += 1
            if i > 45: i = 0

    def test_tree_iterator4(self):
        words2 = [b"zero", b"one", b"two", b"three", b"four", b"five", b"six", b"seven", b"eight", b"nine", b"ten", b"eleven", b"twelve", b"thirteen", b"fourteen", b"fifteen", b"sixteen", b"seventeen", b"eighteen", b"ninteen", b"twenty", b"twenty-one", b"twenty-two", b"twenty-three", b"twenty-four", b"twenty-five", b"twenty-six", b"twenty-seven", b"twenty-eight", b"twenty-nine", b"thirty"]

        # one big array
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=1000):
            self.assertEqual(arrays[b"data"].tolist(), words2)

        # size is equal to basket size (for most baskets)
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=6):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 6])
            i += 6
            if i > 30: i = 0

        # size is smaller
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=3):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 3])
            i += 3
            if i > 30: i = 0
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=4):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 4])
            i += 4
            if i > 30: i = 0

        # size is larger
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=12):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 12])
            i += 12
            if i > 30: i = 0
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=10):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 10])
            i += 10
            if i > 30: i = 0

        # singleton case
        i = 0
        for arrays in uproot.iterate(["tests/samples/foriter2.root", "tests/samples/foriter2.root"], "foriter2", entrysteps=1):
            self.assertEqual(arrays[b"data"].tolist(), words2[i : i + 1])
            i += 1
            if i > 30: i = 0

    def test_directories(self):
        file = uproot.open("tests/samples/nesteddirs.root")

        self.assertEqual([(n, cls._classname) for n, cls in file.classes()], [(b"one;1", b"TDirectory"), (b"three;1", b"TDirectory")])
        self.assertEqual([(n, cls._classname) for n, cls in file.allclasses()], [(b"one;1", b"TDirectory"), (b"one/two;1", b"TDirectory"), (b"one/two/tree;1", b"TTree"), (b"one/tree;1", b"TTree"), (b"three;1", b"TDirectory"), (b"three/tree;1", b"TTree")])

        self.assertEqual(list(file["one"]["tree"].keys()), [b"one", b"two", b"three"])
        self.assertEqual(list(file["one"].get("tree", 1).keys()), [b"one", b"two", b"three"])
        self.assertEqual(list(file["one/tree;1"].keys()), [b"one", b"two", b"three"])
        self.assertEqual(list(file["one/two/tree;1"].keys()), [b"Int32", b"Int64", b"UInt32", b"UInt64", b"Float32", b"Float64", b"Str", b"ArrayInt32", b"ArrayInt64", b"ArrayUInt32", b"ArrayUInt64", b"ArrayFloat32", b"ArrayFloat64", b"N", b"SliceInt32", b"SliceInt64", b"SliceUInt32", b"SliceUInt64", b"SliceFloat32", b"SliceFloat64"])
        self.assertEqual(list(file["three/tree;1"].keys()), [b"evt"])

        self.assertEqual(dict((name, array.tolist()) for name, array in file["one/tree"].arrays(["one", "two", "three"]).items()), {b"one": [1, 2, 3, 4], b"two": [1.100000023841858, 2.200000047683716, 3.299999952316284, 4.400000095367432], b"three": [b"uno", b"dos", b"tres", b"quatro"]})
        self.assertEqual(file["one/two/tree"].array("Int32").shape, (100,))
        self.assertEqual(file["three/tree"].array("I32").shape, (100,))

        file = uproot.open("tests/samples/nesteddirs.root")

        self.assertEqual(list(file["one/tree"].keys()), [b"one", b"two", b"three"])
        self.assertEqual(list(file["one/two/tree"].keys()), [b"Int32", b"Int64", b"UInt32", b"UInt64", b"Float32", b"Float64", b"Str", b"ArrayInt32", b"ArrayInt64", b"ArrayUInt32", b"ArrayUInt64", b"ArrayFloat32", b"ArrayFloat64", b"N", b"SliceInt32", b"SliceInt64", b"SliceUInt32", b"SliceUInt64", b"SliceFloat32", b"SliceFloat64"])
        self.assertEqual(list(file["three/tree"].keys()), [b"evt"])

        self.assertEqual(dict((name, array.tolist()) for name, array in file["one/tree;1"].arrays(["one", "two", "three"]).items()), {b"one": [1, 2, 3, 4], b"two": [1.100000023841858, 2.200000047683716, 3.299999952316284, 4.400000095367432], b"three": [b"uno", b"dos", b"tres", b"quatro"]})
        self.assertEqual(file["one/two/tree;1"].array("Int32").shape, (100,))
        self.assertEqual(file["three/tree;1"].array("I32").shape, (100,))

    def test_cast(self):
        tree = uproot.open("tests/samples/Zmumu.root")["events"]
        one = numpy.cast[numpy.int32](numpy.floor(tree.array("M")))
        two = tree.array("M", numpy.int32)
        self.assertEqual(one.dtype, two.dtype)
        self.assertEqual(one.shape, two.shape)
        self.assertTrue(numpy.array_equal(one, two))

        for (one,) in tree.iterate("M", 10000, outputtype=tuple):
            one = numpy.cast[numpy.int32](numpy.floor(one))
        for (two,) in tree.iterate({"M": numpy.int32}, 10000, outputtype=tuple):
            pass
        self.assertEqual(one.dtype, two.dtype)
        self.assertEqual(one.shape, two.shape)
        self.assertTrue(numpy.array_equal(one, two))

    def test_pass_array(self):
        tree = uproot.open("tests/samples/Zmumu.root")["events"]
        one = numpy.cast[numpy.int32](numpy.floor(tree.array("M")))
        two = numpy.zeros(one.shape, dtype=one.dtype)
        tree.array("M", two)
        self.assertTrue(numpy.array_equal(one, two))

        for (one,) in tree.iterate("M", 10000, outputtype=tuple):
            one = numpy.cast[numpy.int32](numpy.floor(one))
            two = numpy.zeros(one.shape, dtype=one.dtype)
            for (two,) in tree.iterate({"M": numpy.int32}, 10000, outputtype=tuple):
                self.assertTrue(numpy.array_equal(one, two))

    def test_outputtype(self):
        tree = uproot.open("tests/samples/simple.root")["tree"]

        arrays = tree.arrays(["three", "two", "one"], outputtype=dict)
        self.assertTrue(isinstance(arrays, dict))
        self.assertEqual(arrays[b"one"].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[b"three"].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        arrays = tree.arrays(["three", "two", "one"], outputtype=tuple)
        self.assertTrue(isinstance(arrays, tuple))
        self.assertEqual(arrays[2].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[0].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        arrays = tree.arrays(["three", "two", "one"], outputtype=namedtuple)
        self.assertEqual(arrays.one.tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays.three.tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        arrays = tree.arrays(["three", "two", "one"], outputtype=list)
        self.assertTrue(isinstance(arrays, list))
        self.assertEqual(arrays[2].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[0].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        class Awesome(object):
            def __init__(self, one, two, three):
                self.one = one
                self.two = two
                self.three = three

        arrays = tree.arrays(["one", "two", "three"], outputtype=Awesome)
        self.assertTrue(isinstance(arrays, Awesome))
        self.assertEqual(arrays.one.tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays.three.tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        class MyList(list):
            pass

        class MyTuple(tuple):
            pass

        arrays = tree.arrays(["three", "two", "one"], outputtype=MyList)
        self.assertTrue(isinstance(arrays, MyList))
        self.assertEqual(arrays[2].tolist(), [1, 2, 3, 4])
        self.assertEqual(arrays[0].tolist(), [b"uno", b"dos", b"tres", b"quatro"])

        arrays = tree.arrays(["three", "two", "one"], outputtype=MyTuple)
        self.assertTrue(isinstance(arrays, MyTuple))

        arrays = tree.lazyarrays(["three", "two", "one"], outputtype=MyList)
        self.assertTrue(isinstance(arrays, MyList))

        arrays = tree.lazyarrays(["three", "two", "one"], outputtype=MyTuple)
        self.assertTrue(isinstance(arrays, MyTuple))

    def test_tree_lazy(self):
        tree = uproot.open("tests/samples/sample-5.30.00-uncompressed.root")["sample"]

        def normalize(x):
            if isinstance(x, numpy.ndarray):
                return [normalize(y) for y in x]
            else:
                return x

        for branchname in b"u1", b"i8", b"Ai8", b"f4", b"af4":
            strict = tree[branchname].array()

            lazy = tree[branchname].lazyarray()
            for i in range(len(lazy)):
                self.assertEqual(normalize(lazy[i]), strict[i].tolist())

            lazy = tree[branchname].lazyarray()
            for i in range(len(lazy), 0, -1):
                self.assertEqual(normalize(lazy[i - 1]), strict[i - 1].tolist())

            lazy = tree[branchname].lazyarray()
            for i in range(len(lazy)):
                self.assertEqual(normalize(lazy[i : i + 3]), strict[i : i + 3].tolist())

            lazy = tree[branchname].lazyarray()
            for i in range(len(lazy), 0, -1):
                self.assertEqual(normalize(lazy[i - 1 : i + 3]), strict[i - 1 : i + 3].tolist())

    def test_tree_lazy_cached(self):
        tree = uproot.open("tests/samples/sample-5.30.00-uncompressed.root")["sample"]

        def normalize(x):
            if isinstance(x, numpy.ndarray):
                return [normalize(y) for y in x]
            else:
                return x

        keycache = {}
        basketcache = {}

        for branchname in b"u1", b"i8", b"Ai8", b"f4", b"af4":
            strict = tree[branchname].array()

            lazy = tree[branchname].lazyarray(keycache=keycache, basketcache=basketcache)
            for i in range(len(lazy)):
                self.assertEqual(normalize(lazy[i]), strict[i].tolist())

            lazy = tree[branchname].lazyarray(keycache=keycache, basketcache=basketcache)
            for i in range(len(lazy), 0, -1):
                self.assertEqual(normalize(lazy[i - 1]), strict[i - 1].tolist())

            lazy = tree[branchname].lazyarray(keycache=keycache, basketcache=basketcache)
            for i in range(len(lazy)):
                self.assertEqual(normalize(lazy[i : i + 3]), strict[i : i + 3].tolist())

            lazy = tree[branchname].lazyarray(keycache=keycache, basketcache=basketcache)
            for i in range(len(lazy), 0, -1):
                self.assertEqual(normalize(lazy[i - 1 : i + 3]), strict[i - 1 : i + 3].tolist())
