class Program():
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

    


n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

program = []

for i in range(n):
    program.append(Program(name[i], address[i], region[i]))


ans = program[0]
for p in program:
    if p.name > ans.name:
        ans = p

print(f"name {ans.name}")
print(f"addr {ans.address}")
print(f"city {ans.region}")