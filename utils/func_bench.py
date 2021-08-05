import time
import inspect
from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017)
benchmarks = client.benchmarks
functions_benchmark = benchmarks.functions_benchmark
class_functions_benchmark = benchmarks.class_functions_benchmark


def benchmark_decorator(func):
    def get_module_name(func):
        return inspect.getmodule(func)

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        functions_benchmark.insert_one({
            "module": get_module_name(func).__name__,
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
            "start_time": str(start_time),
            "end_time": str(time.time()),
            "duration": str(start_time - time.time())
        })
        return result

    return wrapper


@benchmark_decorator
def some_function():
    print("ABCD")
