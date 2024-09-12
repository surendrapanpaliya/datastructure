import time
# Tuple
tuple_data = tuple(range(1000000))
# List
list_data = list(range(1000000))

# Timing tuple access
start_time = time.time()
_ = tuple_data[500000]
print(f"Tuple access time: {time.time() - start_time}")

# Timing list access
start_time = time.time()
_ = list_data[500000]
print(f"List access time: {time.time() - start_time}")
