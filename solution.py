import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp, anderson_ksamp


chat_id = 749357762 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return anderson_ksamp([x, y]).significance_level < 0.09 # Ваш ответ, True или False
