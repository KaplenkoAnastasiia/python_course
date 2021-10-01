import time

def measure_elapsed_time(func):
  def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"calling {func_name}")
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = round(end_time - start_time, 1)
        print(f"{func_name} call took {run_time} seconds")
        if value != None:
          return value
  return wrapper

@measure_elapsed_time
def my_fn1(arg1, arg2):
   time.sleep(0.5)
   return arg1 + arg2
 
 
@measure_elapsed_time
def my_fn2():
   time.sleep(0.8)
   print("I do nothing! What a life")
 
@measure_elapsed_time
def my_fn3(arg1, **kwargs):
   time.sleep(0.3)
   print(f"I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}")

print("my_fn1 result:", my_fn1(1, 2))
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')
