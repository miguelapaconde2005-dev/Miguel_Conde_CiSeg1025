nums = []
for i in range(3):
    nums.append(int(input(f"Digite o {i+1}º número: ")))

crescente = sorted(nums)
decrescente = sorted(nums, reverse=True)

print(f"Crescente: {crescente}")
print(f"Decrescente: {decrescente}")
