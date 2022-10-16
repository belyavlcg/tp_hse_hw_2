import random
all_digits = range(1, 1000)
for quantity in 10, 1000, 100_000, 1_000_000, 10_000_000:
    num = [str(g) + " " for g in random.choices(all_digits, k=quantity)]
    fh = open(f"test_file_{quantity}", "w")
    for now in num:
        fh.write(now)
    fh.close()
