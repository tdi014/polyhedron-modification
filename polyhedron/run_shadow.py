#!/usr/bin/env -S python3 -B
from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()
try:
    for name in ["test_good", "test_bad"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром \"{name}\"")
        start_time = time()
        poly = Polyedr(f"data/{name}.geom")
        poly.draw(tk)
        # Вывод суммы длин хороших рёбер
        print(poly.good_edges_sum())
        delta_time = time() - start_time
        print(f"Изображение полиэдра \"{name}\" заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
