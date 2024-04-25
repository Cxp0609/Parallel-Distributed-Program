import asyncio
from aiohttp import web
import threading
import math

class PrimeThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
        self.result = None

    def run(self):
        self.result = self.is_prime(self.number)

    def is_prime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

class FibonacciThread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
        self.result = None

    def run(self):
        self.result = self.fibonacci(self.n)

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_list = [0, 1]
            for i in range(2, n + 1):
                fib_list.append(fib_list[-1] + fib_list[-2])
            return fib_list[-1]

async def calculate_prime(number):
    thread = PrimeThread(number)
    thread.start()
    thread.join()
    return thread.result

async def find_fibonacci(n):
    thread = FibonacciThread(n)
    thread.start()
    thread.join()
    return thread.result

def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    factors.sort()
    return factors

async def http_server(host,port):
    app = web.Application()
    app.router.add_route('GET', '/prime/{number}', handle_prime_request)
    app.router.add_route('GET', '/fibonacci/{n}', handle_fibonacci_request)
    app.router.add_route('GET', '/factors/{number}', handle_factors_request)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, host, port)
    await site.start()

    print(f"Server running at http://{host}:{port}")
    print("Example usage: http://192.168.12.114:443/prime/17 will check if 17 is prime.\nhttp://192.168.12.114:443/fibonacci/10 will find the 10th Fibonacci number.\nhttp://192.168.12.114:443/factors/30 will find the factors of 30.")

async def handle_prime_request(request):
    number = int(request.match_info['number'])
    result = await calculate_prime(number)
    return web.Response(text=f"{number} is prime: {result}")

async def handle_fibonacci_request(request):
    n = int(request.match_info['n'])
    result = await find_fibonacci(n)
    return web.Response(text=f"The {n}th Fibonacci number is: {result}")

async def handle_factors_request(request):
    number = int(request.match_info['number'])
    factors = find_factors(number)
    return web.Response(text=f"The factors of {number} are: {factors}")

if __name__ == '__main__':
    host, port = '172.20.212.108', 443 # Change to current IP Address

    # Run the HTTP server in the event loop
    loop = asyncio.get_event_loop()
    loop.create_task(http_server(host, port))
    loop.run_forever()
