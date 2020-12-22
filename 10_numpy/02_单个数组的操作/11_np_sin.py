import numpy as np

nda = np.arange(0, 10)
print("nda:", nda)

ret_nda = np.sin(nda)  # 返回的依旧是ndarray
print("ret_nda:\n", ret_nda)
