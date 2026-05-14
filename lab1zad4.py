def collatz_generator(n):
    if n < 1:
        raise ValueError("Wartość początkowa musi być liczbą całkowitą dodatnią.")
        
    yield n
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n

if __name__ == "__main__":
    print("Ciąg Collatza dla liczby 10:")
    for status in collatz_generator(10):
        print(status)