import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 1841341924 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pval = anderson_ksamp([x, y])[2]
    return pval < 0.02
