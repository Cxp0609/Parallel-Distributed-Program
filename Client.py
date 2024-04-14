import requests

def check_if_prime(number):
    url = f"http://192.168.12.114:443/prime/{number}"
    response = requests.get(url)
    print(response.text)

def find_nth_fibonacci(n):
    url = f"http://192.168.12.114:443/fibonacci/{n}"
    response = requests.get(url)
    print(response.text)

def find_factors(number):
    url = f"http://192.168.12.114:443/factors/{number}"
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Check if a number is prime")
        print("2. Find the nth Fibonacci number")
        print("3. Find factors of a number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            number = int(input("Enter a number to check if it's prime: "))
            check_if_prime(number)
        elif choice == '2':
            n = int(input("Enter the value of n to find nth Fibonacci number: "))
            find_nth_fibonacci(n)
        elif choice == '3':
            number = int(input("Enter a number to find its factors: "))
            find_factors(number)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
