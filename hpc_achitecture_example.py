# hpc_architecture_example.py
"""
Simulación de uso de arquitectura de altas prestaciones (multinúcleo).
"""
import concurrent.futures
import time
import os

def heavy_compute(n):
    print(f"Procesando {n} en CPU {os.getpid()}")
    time.sleep(1)
    return n ** 3

def main():
    cores = os.cpu_count() or 1
    print(f"Usando {cores} núcleos para computación intensiva...")
    with concurrent.futures.ProcessPoolExecutor(max_workers=cores) as executor:
        resultados = list(executor.map(heavy_compute, range(1, cores + 1)))
    print("Completado HPC:", resultados)

if __name__ == "__main__":
    main()
