import logging

from .modules.io import IOProcessor
from .modules.kernel import ProfitCalculator
def max_profit(args):
    io_processor = IOProcessor(args.input, args.output, args.name_list)
    profit_calculator = ProfitCalculator()

    data_np = io_processor.get_input_numpy()
    io_processor.set_config(data_np)
    max_profit_val, steps = profit_calculator.get_max_profit_steps(data_np, args.start, args.end)
    io_processor.gen_output_file(max_profit_val, steps)

    logging.info(f'Max profit: {max_profit_val}\n')
    logging.info(f'================\n')
    logging.info(f'steps:\n')

    for i in range(len(steps) - 1):
        logging.info(f'{i + 1}. {io_processor.currencies_name_tup[steps[i]]} -> '
                     f'{io_processor.currencies_name_tup[steps[i + 1]]}\n')
