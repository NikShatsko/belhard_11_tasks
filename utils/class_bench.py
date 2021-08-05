from .func_bench import benchmark_decorator, client

benchmarks = client.benchmarks
functions_benchmark = benchmarks.functions_benchmark
class_functions_benchmark = benchmarks.class_functions_benchmark


@benchmark_decorator
class ClassDecorator:

    def add_function(self):
        class_functions_benchmark.insert_one({"class_name": ClassDecorator.__name__})





