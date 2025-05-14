# parallel_example.py
"""
Demostración de computación paralela usando multiprocessing.Pool.
"""
import multiprocessing
import time

def task(n):
    """Función que simula una tarea intensiva."""
    print(f"Procesando {n} en PID {multiprocessing.current_process().pid}")
    time.sleep(1)
    return n * n

def main():
    nums = list(range(1, 9))
    print("Inicio de procesamiento paralelo...")
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(task, nums)
    print("Resultados:", results)

if __name__ == "__main__":
    main()
