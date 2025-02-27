import random
import matplotlib.pyplot as plt

num_throws = 10000
sums_count = {i: 0 for i in range(2, 13)}


for _ in range(num_throws):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    sums_count[roll_sum] += 1

for key in sums_count:
    sums_count[key] /= num_throws

theoretical_probs = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
                     8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}


plt.bar(sums_count.keys(), sums_count.values(), width=0.4,
        label="Симуляція", color='blue', alpha=0.7)
plt.bar([s + 0.4 for s in theoretical_probs.keys()], theoretical_probs.values(),
        width=0.4, label="Теоретичні", color='red', alpha=0.7)
plt.xlabel("Сума")
plt.ylabel("Ймовірність, %")
plt.title(f"Ймовірності сум при {num_throws} кидках кубиків")
plt.legend()
plt.show()
