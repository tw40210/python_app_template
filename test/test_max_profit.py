import pytest
import pickle
import logging

from src.api import max_profit
from src.modules.kernel import ProfitCalculator

logging.basicConfig(level=logging.DEBUG, filemode = 'a', format='%(levelname)s:%(asctime)s:  %(message)s'
                    , datefmt='%Y-%d-%m %H:%M:%S')

class TestMaxProfit:
    class FakeArgs:
        def __init__(self):
            self.input = "test/data/max_profit/test.txt"
            self.output = "test/data/max_profit/testOutput.txt"
            self.name_list = tuple("A,B,C,D".split(","))
            self.start = 0
            self.end = 0

    def test_kernel(self):
        profit_calculator = ProfitCalculator()
        args = self.FakeArgs()
        with open("test/data/max_profit/kernel/data_np.pkl", "rb") as file:
            data_np = pickle.load(file)
            val, steps = profit_calculator.get_max_profit_steps(data_np, args.start, args.end)

        with open("test/data/max_profit/kernel/max_profit_val.pkl", "rb") as file:
            golden_val = pickle.load(file)

        with open("test/data/max_profit/kernel/steps.pkl", "rb") as file:
            golden_steps = pickle.load(file)

        assert val == golden_val
        assert len(steps) == len(golden_steps) and all([steps[i] == golden_steps[i] for i in range(len(golden_steps))])

        print(val, steps)

    def test_end_to_end(self):
        max_profit(self.FakeArgs())
        with open("test/data/max_profit/testOutput.txt", "r") as file:
            output_str = file.read()
        with open("test/data/max_profit/golden_output.txt", "r") as file:
            golden_output_str = file.read()

        assert output_str == golden_output_str
