import matplotlib.pyplot as plt

plt.style.use('ggplot')

years = [2018, 2019, 2020, 2021, 2022, 2023]

python_position = [7, 4, 4, 3, 4, 3]

javascript_position = [1, 1, 1, 1, 1, 1]

sql_position = [ 4, 3, 3, 4, 3, 4 ]

typescript_position = [ 12, 10, 9, 7, 5, 5]

plt.plot(years, python_position)
plt.plot(years, javascript_position)
plt.plot(years, sql_position )
plt.plot(years, typescript_position)

plt.plot(years, python_position, label = "Python" , linestyle = "dashed")
plt.plot(years, javascript_position, label = "Javascript", linestyle = "dotted" )
plt.plot(years, sql_position, label = "SQL", linestyle = "dashed" )
plt.plot(years, typescript_position, label = "Typescript", linestyle = "dashdot" )
plt.title("Python Rankings in Stack Overflow Survey ")
plt.xlabel("Year")
plt.ylabel("Position in Survey")
plt.ylim(bottom = 13, top = 0)

plt.legend()

plt.show()
