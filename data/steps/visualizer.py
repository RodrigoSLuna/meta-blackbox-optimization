import matplotlib.pyplot as plt


with open("output-0", "r") as f:
    file = f.read()

file = file.split("\n")

max_value = float(file[0].split()[1])

step = []
y_value = []
for i in range(2, 52):
    s, y = file[i].split()

    step.append(int(s))
    y_value.append(float(y))


new_y_value = [y_value[0]]
low_value = y_value[0]
for i in range(1, len(y_value)):
    if y_value[i] < low_value:
        new_y_value.append(y_value[i])
        low_value = y_value[i]
    else:
        new_y_value.append(low_value)

horiz_line_data = [max_value for i in range(len(step))]
plt.plot(step, horiz_line_data, 'r--') 


plt.plot(step, new_y_value)

plt.show()