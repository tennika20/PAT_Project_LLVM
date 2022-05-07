import csv
import matplotlib.pyplot as plt
file = open("outDriller.txt")
csvreader = csv.reader(file)



rows = []
names = []
tel = {}
for row in csvreader:
rows.append(row)
names.append(row[4])



for i in names:
if i in tel:
p = tel[i]
tel[i] = p + 1
else:
tel[i] = 1

x = []
y = []
for i in tel:
x.append(i)
y.append(tel[i])



plt.plot(x, y)
plt.title("Commit Frequency chart")

plt.xlabel('Developer')
plt.ylabel('Number of Actions')
plt.xticks(rotation = 90)
plt.savefig('commits.png')



sorted_names = sorted(tel.items(), key = lambda kv: kv[1])
sorted_names.reverse()
top_contributers = []
action_count = []



for i in range(0,5):
top_contributers.append(sorted_names[i][0])
action_count.append(sorted_names[i][1])



plt.bar(top_contributers, action_count)
plt.title("Top contributers")
plt.xlabel('Developer')
plt.ylabel('Number of Actions')
plt.xticks(rotation = 90)
plt.savefig('topcontributors.png')
