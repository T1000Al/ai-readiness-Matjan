print("Hello, I am Alex Matjan, and my student ID is R02351612.")

def calculate_stats(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

numbers = [10, 20, 30, 40, 50]

mean, maximum = calculate_stats(numbers)

print("Mean:", mean)
print("Maximum:", maximum)