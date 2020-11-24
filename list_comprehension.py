temps = [213, 346, 870, 981, 717]

# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)

# new_temps = [temp / 10 for temp in temps]

new_temps = [temp / 10 for temp in temps if temp > 500]

print(new_temps)