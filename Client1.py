import requests

def send_request_to_client2(option, number, client2_address, server_address):
    url = f"http://{client2_address}/process_request"
    data = {
        'option': option,
        'number': number,
        'server_address': server_address
    }
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    # Prompt the user for inputs
    client2_address = input("Enter the address of client 2: ")
    server_address = input("Enter the server address: ")

    while True:
        # Prompt the user to choose an option
        print("\nChoose an option:")
        print("1. Check if a number is prime")
        print("2. Find the nth Fibonacci number")
        print("3. Find factors of a number")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '4':
            print("Exiting...")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter a valid option.")
            continue

        # Prompt the user to enter a number
        number = int(input("Enter a number: "))

        # Send the request to Client 2
        result = send_request_to_client2(choice, number, client2_address, server_address)

        # Print the result
        print("Result:", result)
