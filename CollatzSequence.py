def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    num = int(input("Enter a number: "))
    sequence = collatz_sequence(num)
    print(sequence)
    print(f"Sequence length: {len(sequence)}")

if _name_ == "_main_":
    main()
