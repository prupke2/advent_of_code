# def buildDB():
#     db = dict()
#     for l in open('data.txt').read().split("\n"):
#         if l != '':
#             l = l.replace(',','').split()
#             key = "{} {}".format(l[0],l[1])
#             t = list()
#             l = l[4:]
#             if (l != ['no','other','bags.']):
#                 for i in range(len(l)):
#                     if(i % 4 == 0):
#                         t.append((int(l[i]),"{} {}".format(l[i+1],l[i+2])))
#                 if (key not in db):
#                     db[key] = t
#     return db

# db = buildDB()

# def part1():
#     search = ['shiny gold']
#     outer,start = set(),0
#     while True:
#         for i in db.keys(): #
#             for j in db[i]:
#                 if (j[1] in outer or j[1] in search):
#                     outer.add(i)
#         if (len(outer) > start):
#             start = len(outer)
#         else:
#             break
#     print(len(outer))

# def part2():
#     def getContent(bag):
#         c = 1
#         if (bag in db):
#             for i in db[bag]:
#                 c += i[0]*getContent(i[1])
#         return c
#     print(getContent('shiny gold')-1)

# part1()
# part2()

bags = {}
count = 0
def count_shiny(key):
  global count
  count += sum(bags[key].values())
  for bag, times in bags[key].items():
    for _ in range(times):
      count_shiny(bag)

count_shiny("shiny gold")
print(f"Part Two: {count}")
