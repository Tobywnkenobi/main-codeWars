import time

# Define Kirby characters for each step
kirby_steps = [
    "<( o.o )>",  # Step 1
    "<( -.- )>",  # Step 2
    "<(>.<)>",    # Step 3
    "<( -.- )>",  # Step 4
    "<( o.o )>",  # Step 5
]

# Number of times to repeat the animation
num_repeats = 5

# Delay between steps in seconds (adjust as needed)
delay_seconds = 0.5

# Animation loop
for _ in range(num_repeats):
    for step in kirby_steps:
        print(step)
        time.sleep(delay_seconds)
