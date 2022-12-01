import time

N_TESTS = 10
timings = []

for i in range(N_TESTS):
    start = time.time()

    # прогу сюда

    delta = start - time.time()
    timings.append(delta)

avg_time = sum(timings) / len(timings)
print(f'execution time of manual_parser:{avg_time}')

for i in range(N_TESTS):
    start = time.time()

    # прогу сюда

    delta = start - time.time()
    timings.append(delta)

avg_time = sum(timings) / len(timings)
print(f'execution time of parser_with_libs:{avg_time}')

for i in range(N_TESTS):
    start = time.time()

    # прогу сюда

    delta = start - time.time()
    timings.append(delta)

avg_time = sum(timings) / len(timings)
print(f'execution time of parser_with_regex:{avg_time}')
