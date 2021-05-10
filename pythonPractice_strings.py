print(len("My name is Chaitanya"))

print("Chaitanya" + "Priya")

colors = ';'.join(["kdj","ie","oie"])
print(colors)

print(colors.split(';'))

print("unforgetable".partition("forget"))
# partitions it into 3 blocks, one part before the seperator, the seperator and after the seperator

departure,seperator, arrival = "London:India".partition(":")
print(departure)
print(arrival)

print(" My {} is {}".format('name','Chaitanya'))

value = 4*20
print(f'The value is {value}')
