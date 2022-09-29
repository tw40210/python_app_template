import numpy as np
from collections import deque


class ProfitCalculator:
    def __init__(self):
        pass

    def get_max_profit_steps(self, data_np, start_idx, end_idx):
        n = data_np.shape[0]
        m = data_np.shape[1]
        steps = deque([])

        steps_max_np = np.zeros([n, m])

        steps_max_np[0] = data_np[0][start_idx]

        for i in range(1, n):
            next_mat = data_np[i]
            cur_mat = np.tile(steps_max_np[i - 1], (m, 1)).T
            next_mat = cur_mat * next_mat
            steps_max_np[i] = np.max(next_mat, axis=0)

        tmp_end_idx = end_idx
        for i in range(n - 1, 0, -1):
            next_mat = data_np[i]
            cur_mat = np.tile(steps_max_np[i - 1], (m, 1)).T
            next_mat = cur_mat * next_mat
            tmp_end_idx = np.argmax(next_mat[:, tmp_end_idx])
            steps.appendleft(tmp_end_idx)

        steps.appendleft(start_idx)
        steps.append(end_idx)

        return steps_max_np[-1][end_idx], list(steps)
