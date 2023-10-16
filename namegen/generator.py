import random

def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Brown", "Wilson", "Taylor", "Lee", "Clark", "Moore", "Miller", "Hall"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"