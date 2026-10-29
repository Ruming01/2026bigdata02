import pandas as pd
import numpy as np
import scipy.stats as stats

s = pd.Series([1, 2, 3, np.nan, np.nan, 6, 7, np.nan, np.nan])
print(s)

# interpolation 메서드를 이용한 결측치 내삽
# s = s.interpolate(method="spline", order=1, limit_direction="forward", limit=2)
s = s.interpolate(method="spline", order=1, limit_direction="backward", limit=2)
print(s)