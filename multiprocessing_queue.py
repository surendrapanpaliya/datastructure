
import multiprocessing
import time
import random

def producer(queue):
    """Function to generate data and put it in the queue."""
    for _ in range(5):
        item = random.randint(1, 100)
        print(f"Producer put: {item}")
        queue.put(item)
        time.sleep(random.random())  # Simulate work by sleeping for a random time

    queue.put(None)  # Sentinel value to indicate end of production

def consumer(queue):
    """Function to consume data from the queue."""
    while True:
        item = queue.get()  # Retrieve data from the queue
        if item is None:  # Check for sentinel value
            break
        print(f"Consumer got: {item}")
        time.sleep(random.random())  # Simulate processing time

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    # Create producer and consumer processes
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for both processes to finish
    producer_process.join()
    consumer_process.join()

    print("Processing complete.")
