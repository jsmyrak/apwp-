import functools
from datetime import datetime
import time

def logger(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            
            result = func(*args, **kwargs)
            
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_message = (f"Data: {now} | Funkcja: {func.__name__} | "
                           f"Czas wykonania: {execution_time:.4f}s\n")

            with open(filename, "a", encoding="utf-8") as f:
                f.write(log_message)
            
            return result
        return wrapper
    return decorator

# Test:
@logger("wykonania_funkcji.log")
def slow_function(seconds):
    """Funkcja symulująca długą pracę."""
    time.sleep(seconds)
    print(f"Zakończono oczekiwanie przez {seconds}s")

@logger("wykonania_funkcji.log")
def add_numbers(a, b):
    return a + b

# Uruchomienie testowe
if __name__ == "__main__":
    slow_function(1.5)
    result = add_numbers(10, 20)
    print(f"Wynik dodawania: {result}")
    
    print("\nSprawdź plik 'wykonania_funkcji.log', aby zobaczyć zapisane logi.")