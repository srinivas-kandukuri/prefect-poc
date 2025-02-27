from prefect import flow, task

@task
def say_hello():
    """A simple task to test ECS execution."""
    print("Hello from the low-memory ECS pool!")

@flow
def test_low_memory_flow():
    """A test flow to verify the low-memory ECS pool."""
    say_hello()

if __name__ == "__main__":
    test_low_memory_flow()
