from func_bench import benchmark_decorator, client

benchmarks = client.benchmarks
functions_benchmark = benchmarks.functions_benchmark
class_functions_benchmark = benchmarks.class_functions_benchmark


def for_all_public(cls):
    for key, item in cls.__dict__.items():
        if not key.startswith('_') and callable(item):
            setattr(cls, key, benchmark_decorator(item))


@for_all_public
class ClassDecorator:
    def _some_function(self):
        print("Hello")

    def add_function(self):
        class_functions_benchmark.insert_one({"class_name": ClassDecorator.__name__})



