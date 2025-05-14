# flynn_taxonomy.py
"""
Demostración de SISD, SIMD, MISD y MIMD.
"""
import threading
import multiprocessing
import numpy as np

def sisd_example(data):
    # Un único flujo de control y dato
    print("SISD:", [x * 2 for x in data])

def simd_example(data):
    # Una instrucción, múltiples datos (vectorizado con NumPy)
    arr = np.array(data)
    print("SIMD:", arr * 2)

def misd_example(data):
    # Varias instrucciones, un solo dato (dos funciones distintas sobre el mismo dato)
    def inc(x): return x + 1
    def sqr(x): return x * x
    for func in [inc, sqr]:
        print(f"MISD con {func.__name__}:", [func(x) for x in data])

def mimd_example(data1, data2):
    # Varias instrucciones, múltiples datos usando procesos
    def task1(n): return n + 10
    def task2(n): return n * 10
    with multiprocessing.Pool(2) as pool:
        r1 = pool.map(task1, data1)
        r2 = pool.map(task2, data2)
    print("MIMD task1:", r1)
    print("MIMD task2:", r2)

if __name__ == "__main__":
    datos = [1, 2, 3, 4]
    sisd_example(datos)
    simd_example(datos)
    misd_example(datos)
    mimd_example(datos, datos)
