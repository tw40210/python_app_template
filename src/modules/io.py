import numpy as np
import json
import logging


class IOProcessor:
    def __init__(self, input_path, output_path, currencies_name_tup):
        self.input_path = input_path
        self.output_path = output_path
        self.currencies_name_tup = currencies_name_tup
        self.matrix_len = -1

    def _check_data(self, data_np):
        if len(data_np.shape) != 3:
            raise ValueError(f"The data should be 3 dimensions but not only {len(data_np.shape)}."
                             f"Please check the data validity.")

        n = data_np.shape[0]
        m = data_np.shape[1]

        if data_np.shape[1] != data_np.shape[2]:
            raise ValueError(f"The matrix should be square but not."
                             f"Please check the data validity.")

        for i in range(n):
            for j in range(m):
                for k in range(j, m):
                    if k == j:
                        if abs(data_np[i][k][j] - 1) > 1e-10:
                            raise ValueError(f"The diagonal of matrix should be 1 but not in {i + 1}th matrix."
                                             f"Please check the data validity.")

    def get_input_numpy(self):
        try:
            with open(self.input_path, 'r', encoding='utf-8-sig') as file:
                lines = file.read()
                lines = json.loads(lines)
                data_np = np.array(lines)
        except Exception as e:
            logging.error(e)
            raise ValueError(f"Input data is invalid."
                             f"Please check the file path is correct and the content is wrote in utf-8-sig and json format.")

        return data_np

    def set_config(self, data_np):
        self._check_data(data_np)
        self.matrix_len = data_np.shape[1]

        if len(self.currencies_name_tup) != self.matrix_len:
            logging.warning(f"The length of input name list is not equal to the length of matrix_len:"
                            f"{len(self.currencies_name_tup)} {self.matrix_len},"
                            f"The name list was reset to default!")
            self.currencies_name_tup = tuple(range(self.matrix_len))

    def gen_output_file(self, max_profit_val, steps):
        with open(self.output_path, 'w', encoding='utf-8-sig') as file:
            file.write(f'Max profit: {max_profit_val}\n')
            file.write(f'================\n')
            file.write(f'steps:\n')

            for i in range(len(steps) - 1):
                file.write(
                    f'{i + 1}. {self.currencies_name_tup[steps[i]]} -> {self.currencies_name_tup[steps[i + 1]]}\n')
