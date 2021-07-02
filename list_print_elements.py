# list: print new line and enumerate() example.

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# print("seasons: ", type(seasons))
# print(list(enumerate(seasons)), end="\n")
# print(list(enumerate(seasons, start=1)))

for i in range(0, len(seasons)):
    print(seasons[i])

print("----------------")

start_idx = 6
for idx, val in enumerate(seasons, start_idx):
    print(idx, val)

print("----------------")

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

for n, (x, y) in enumerate(data):
    print("index: {}, (x,y): ({}, {})".format(n, x, y))

    

