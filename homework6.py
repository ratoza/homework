from tkinter import *

size = 10

solution_text = []

start_list = list(range(size, 0, -1))

def hanoi(start, end, aux, n):
    if n == 1:
        solution_text.append("Moved from %s to %s" % (start, end))
        return
    hanoi(start, aux, end, n-1)
    solution_text.append("Moved from %s to %s" % (start, end))
    hanoi(aux, end, start, n-1)


def hanoi_graphic(start, end, aux, n):
    if n == 1:
        # print("Move from", start, "to", end)
        end.append(start.pop())
        solution.append(start_list.copy())
        solution.append(middle_list.copy())
        solution.append(end_list.copy())
        return
    hanoi_graphic(start, aux, end, n-1)
    # print("Move from", start, "to", end)
    end.append(start.pop())
    solution.append(start_list.copy())
    solution.append(middle_list.copy())
    solution.append(end_list.copy())
    hanoi_graphic(aux, end, start, n-1)


def next_move():
    global size
    global pos
    if pos >= len(solution):
        return
    start = solution[pos]
    middle = solution[pos+1]
    end = solution[pos+2]
    sol_lb.configure(text=solution_text[pos // 3])
    left_lb.configure(text="%s moves left" % ((len(solution) - pos - 1)//3))
    pos += 3

    for i in range(size):
        if i < len(start):
            start_lb[i].configure(width=(start[i]-1)*2 + 3, bg="blue", fg="white", text="%d" % (start[i]))
        else:
            start_lb[i].configure(width=1, bg="red", text="")
    for i in range(size):
        if i < len(middle):
            middle_lb[i].configure(width=(middle[i]-1)*2 + 3, bg="blue", fg="white", text="%d" % (middle[i]))
        else:
            middle_lb[i].configure(width=1, bg="red", text="")
    for i in range(size):
        if i < len(end):
            end_lb[i].configure(width=(end[i]-1)*2 + 3, bg="blue", fg="white", text="%d" % (end[i]))
        else:
            end_lb[i].configure(width=1, bg="red", text="")



hanoi("First", "Third", "Second", size)

solution = []

pos = 0



middle_list = []

end_list = []

hanoi_graphic(start_list, end_list, middle_list, size)



# print(solution)

window = Tk()

window.title("Hanoi")

window.geometry("830x750")



title = Label(master=window, text="Welcome to the Hanoi Tower Problem", font=("Arial", 20))

title.grid(row=0, column=0, columnspan=8, pady=20, padx=20)



button = Button(master=window, text="Next Move", command=next_move, font=("Arial", 20))

button.grid(row=size+4, column=0, columnspan=8, pady=50)



sol_lb = Label(master=window, text="", font=("Arial", 20))

sol_lb.grid(row=size+2, column=0, columnspan=6, pady=20, padx=20)



left_lb = Label(master=window, text="%s moves left" % (len(solution)//3 ), font=("Arial", 10), fg="green")

left_lb.grid(row=size+3, column=0, columnspan=6, pady=20, padx=20)





start_lb = []

middle_lb = []

end_lb = []



# fake1 fake2 just for display purposes

fake1 = []

fake2 = []

fake3 = []

for i in range(size):

    start_lb.append(Label(master=window, width=(size - 1 - i)*2+3, bg="blue", fg="white", text="%d" % (size-i)))

    middle_lb.append(Label(master=window, width=1, bg="red"))

    end_lb.append(Label(master=window, width=1, bg="red"))

    start_lb[i].grid(row=size+1-i, column=1)

    middle_lb[i].grid(row=size+1-i, column=3)

    end_lb[i].grid(row=size+1-i, column=5)



    fake1.append(Label(master=window, width=0))

    fake2.append(Label(master=window, width=0))

    fake3.append(Label(master=window, width=0))

    fake1[i].grid(row=size+1-i, column=0)

    fake2[i].grid(row=size+1-i, column=2)

    fake3[i].grid(row=size+1-i, column=4)





window.mainloop()