num = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024

k = 0
while num > 0:
    if num % 25 > 10: k += 1
    num //= 25

print(k)
