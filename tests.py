import pytest

from main import Parser, ParserException


class Test:

    def test_fake_regular(self):
        regular = '*'
        k = 4
        x = Parser(regular, k)
        with pytest.raises(ParserException):
            x.get_answer(3)

    def test_sample_1(self):
        regular = 'ab+c.aba.*.bac.+.+*'
        k = 3
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == [0, 4, 2]

    def test_sample_2(self):
        regular = 'acb..bab.c.*.ab.ba.+.+*a.'
        k = 3
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == ['INF', 1, 'INF']

    def test_3(self):
        regular = 'aba.*.a.*ab1+..'
        k = 4
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == [4, 1, 2, 3]

    def test_4(self):
        regular = 'ab+'
        k = 4
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == ['INF', 1, 'INF', 'INF']

    def test_5(self):
        regular = 'aa.*'
        k = 4
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == [0, 'INF', 2, 'INF']

    def test_6(self):
        regular = 'ab.'
        k = 4
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == ['INF', 'INF', 2, 'INF']

    def test_7(self):
        regular = 'aa.bbb..+*'
        k = 10
        x = Parser(regular, k)
        assert [x.get_answer(i) for i in range(k)] == [0, 11, 2, 3, 4, 5, 6, 7, 8, 9]
