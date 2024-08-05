from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum2(self):
        assert sum_solution.compute(2, 3) == 5

    def test_sum3(self):
        assert sum_solution.compute(3, 4) == 7

    def test_sum4(self):
        assert sum_solution.compute(-5, 6) == 1
    
    def test_sum5(self):
        assert sum_solution.compute(52, 60) == 112




