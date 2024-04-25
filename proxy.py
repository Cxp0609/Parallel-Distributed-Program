from aiohttp import web
import asyncio
import requests

async def handle_request(request):
    data = await request.json()
    option = data.get('option')
    number = data.get('number')
    server_address = data.get('server_address')
    
    # Perform logic based on the option
    if option == '1':
        result = await check_if_prime(number, server_address)
    elif option == '2':
        result = await find_nth_fibonacci(number, server_address)
    elif option == '3':
        result = await find_factors(number, server_address)
    else:
        result = "Invalid option"
    
    return web.json_response({'result': result})

async def check_if_prime(number, server_address):
    # Make a request to the server to check if the number is prime
    response = requests.get(f"http://{server_address}/prime/{number}")
    return response.text

async def find_nth_fibonacci(number, server_address):
    # Make a request to the server to find the nth Fibonacci number
    response = requests.get(f"http://{server_address}/fibonacci/{number}")
    return response.text

async def find_factors(number, server_address):
    # Make a request to the server to find the factors of the number
    response = requests.get(f"http://{server_address}/factors/{number}")
    return response.text

async def start_server():
    app = web.Application()
    app.router.add_post('/process_request', handle_request)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, '172.20.212.108', 8000)  # Listening on all interfaces, port 8000
    await site.start()
    print("Client 2 server started")

# Start the web server
loop = asyncio.get_event_loop()
loop.create_task(start_server())
loop.run_forever()
