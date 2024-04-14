import sys
import requests

def check_if_prime(number, server_address):
    url = f"http://{server_address}/prime/{number}"
    response = requests.get(url)
    print(response.text)

def find_nth_fibonacci(n, server_address):
    url = f"http://{server_address}/fibonacci/{n}"
    response = requests.get(url)
    print(response.text)

def find_factors(number, server_address):
    url = f"http://{server_address}/factors/{number}"
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_address>")
        sys.exit(1)

    server_address = sys.argv[1]

    while True:
        print("\nChoose an option:")
        print("1. Check if a number is prime")
        print("2. Find the nth Fibonacci number")
        print("3. Find factors of a number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            number = int(input("Enter a number to check if it's prime: "))
            check_if_prime(number, server_address)
        elif choice == '2':
            n = int(input("Enter the value of n to find nth Fibonacci number: "))
            find_nth_fibonacci(n, server_address)
        elif choice == '3':
            number = int(input("Enter a number to find its factors: "))
            find_factors(number, server_address)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
