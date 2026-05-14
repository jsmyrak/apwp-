import functools

def show_list_length(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        for arg in args:
            if isinstance(arg, list):
                print(f"Znaleziono listę (w argumentach pozycyjnych). Liczba elementów: {len(arg)}")
        
        for key, value in kwargs.items():
            if isinstance(value, list):
                print(f"Znaleziono listę (w parametrze '{key}'). Liczba elementów: {len(value)}")
                
        return func(*args, **kwargs)
    
    return wrapper

# Test:
@show_list_length
def process_data(data_list, name):
    print(f"Przetwarzanie {name}")

print("--- Test 1: Lista jako argument pozycyjny ---")
process_data([1, 2, 3, 4, 5], "Zestaw 1")

print("\n--- Test 2: Lista jako argument nazwany ---")
process_data(name="Zestaw 2", data_list=['a', 'b', 'c'])