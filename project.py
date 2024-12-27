import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from EmpDep import Employee, Department
from tkinter import messagebox

def update_db(): 
    cursor.execute('SELECT * FROM departments')
    departments = cursor.fetchall()
    for department in departments:
        tree_departments.insert('', tk.END, values=department)

def item_selected(event):
    for department in tree_departments.selection():
        item = tree_departments.item(department)
        ID = item['values'][0]
        cursor.execute(f'SELECT * FROM employees WHERE DepartmentID={ID}')
        emps = cursor.fetchall()
        tree_employees.delete(*tree_employees.get_children())
        for emp in emps:
            tree_employees.insert('', tk.END, values=emp)

def click_fire():
    fire_win = tk.Toplevel()
    lb_id = tk.Label(fire_win, text='Введите ID сотрудника,\nкоторого хотите удалить из таблицы')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(fire_win, textvariable=ent_id_var)
    btn_fire = tk.Button(fire_win, text='Удалить', command=lambda: Employee.del_employee(conn, cursor,fire_win, int(ent_id_var.get())))
    lb_id.pack()
    ent_id.pack()
    btn_fire.pack()
    fire_win.deiconify()
    
def click_hire():
    hire_win = tk.Toplevel()
    hire_win.geometry('460x260')
    hire_win.resizable(False,False)
    lb_emp = tk.Label(hire_win, text='Введите данные сотрудника, \nкоторого хотите добавить')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(hire_win, textvariable=ent_id_var)
    ent_surname_var = tk.StringVar()
    ent_surname = tk.Entry(hire_win, textvariable=ent_surname_var)
    ent_name_var = tk.StringVar()
    ent_name = tk.Entry(hire_win, textvariable=ent_name_var)
    ent_surname2_var = tk.StringVar()
    ent_surname2 = tk.Entry(hire_win, textvariable=ent_surname2_var)
    ent_salary_var = tk.StringVar()
    ent_salary = tk.Entry(hire_win, textvariable=ent_salary_var)
    ent_bonus_var = tk.StringVar()
    ent_bonus = tk.Entry(hire_win, textvariable=ent_bonus_var)
    ent_vacation_var = tk.StringVar()
    ent_vacation = tk.Entry(hire_win, textvariable=ent_vacation_var)
    ent_date_var = tk.StringVar()
    ent_date = tk.Entry(hire_win, textvariable=ent_date_var)
    ent_position_var = tk.StringVar()
    ent_position = tk.Entry(hire_win, textvariable=ent_position_var)
    ent_depid_var= tk.StringVar()
    ent_depid = tk.Entry(hire_win, textvariable=ent_depid_var)
    lb_id1 = tk.Label(hire_win,text='ID')
    lb_surname = tk.Label(hire_win,text='Фамилия')
    lb_name = tk.Label(hire_win,text='Имя')
    lb_surname2 = tk.Label(hire_win, text='Отчество')
    lb_salary = tk.Label(hire_win,text='Зарплата')
    lb_bonus = tk.Label(hire_win,text='Премия')
    lb_vacation = tk.Label(hire_win,text='В отпуске ли сотрудник?')
    lb_vacation1 = tk.Label(hire_win,text='1 - Да, 0 - Нет')
    lb_date = tk.Label(hire_win,text='Дата приёма на работу')
    lb_date1 = tk.Label(hire_win,text='В формате "год,месяц,число"')
    lb_position = tk.Label(hire_win,text='Должность')
    lb_depid = tk.Label(hire_win,text='ID отдела')

    btn_hire = tk.Button(hire_win, text='Добавить', command=lambda: Employee.add_employee(conn, cursor,hire_win,int(ent_id_var.get()),ent_surname_var.get(),ent_name_var.get(),ent_surname2_var.get(),int(ent_salary_var.get()),int(ent_bonus_var.get()),bool(ent_vacation_var.get()),str(ent_date_var.get()),ent_position_var.get(),int(ent_depid_var.get())))
    lb_id1.place(x=125,y=33)
    lb_surname.place(x=80,y=53)
    lb_name.place(x=103,y=73)
    lb_surname2.place(x=80,y=93)
    lb_salary.place(x=80,y=113)
    lb_bonus.place(x=80,y=130)
    lb_vacation.place(x=1,y=150)
    lb_vacation1.place(x=290,y=150)
    lb_date.place(x=1,y=170)
    lb_date1.place(x=290,y=170)
    lb_position.place(x=60,y=188)
    lb_depid.place(x=70,y=208)

    lb_emp.pack()
    ent_id.pack()
    ent_surname.pack()
    ent_name.pack()
    ent_surname2.pack()
    ent_salary.pack()
    ent_bonus.pack()
    ent_vacation.pack()
    ent_date.pack()
    ent_position.pack()
    ent_depid.pack()
    btn_hire.pack()
    hire_win.deiconify()

def click_vacation():
    vacation_win = tk.Toplevel()
    lb_id = tk.Label(vacation_win, text='Введите ID сотрудника,\nкоторого хотите отправить в отпуск')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(vacation_win, textvariable=ent_id_var)
    btn_vacation = tk.Button(vacation_win, text='Отправить в отпуск', command=lambda: Employee.go_vacation(conn, cursor,vacation_win, ent_id_var.get()))
    lb_id.pack()
    ent_id.pack()
    btn_vacation.pack()
    vacation_win.deiconify()


def click_end_vacation():
    end_vacation_win = tk.Toplevel()
    lb_id = tk.Label(end_vacation_win, text='Введите ID сотрудника,\nотпуск которого хотите завершить')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(end_vacation_win, textvariable=ent_id_var)
    btn_end_vacation = tk.Button(end_vacation_win, text='Завершить отпуск', command=lambda: Employee.end_vacation(conn, cursor,end_vacation_win, ent_id_var.get()))
    lb_id.pack()
    ent_id.pack()
    btn_end_vacation.pack()
    end_vacation_win.deiconify()

def click_working_days():
    working_days_win = tk.Toplevel()
    lb_id = tk.Label(working_days_win,text='Введите ID сотрудника, \nчтобы узнать, сколько он работает в компании')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(working_days_win, textvariable=ent_id_var)
    btn_working_days = tk.Button(working_days_win,text='Узнать время работы', command=lambda: Employee.working_days(conn,cursor, working_days_win,ent_id_var.get()))
    lb_id.pack()
    ent_id.pack()
    btn_working_days.pack()
    working_days_win.deiconify()

def click_financing():
    financing_win = tk.Toplevel()
    lb_id = tk.Label(financing_win,text='Введите ID отдел, \nфинансирование которого хотите узнать.')
    ent_id_var = tk.StringVar()
    ent_id = tk.Entry(financing_win,textvariable=ent_id_var)
    btn_financing = tk.Button(financing_win,text='Рассчитать',command=lambda: Department.financing(conn,cursor,financing_win,ent_id_var.get()))
    lb_id.pack()
    ent_id.pack()
    btn_financing.pack()
    financing_win.deiconify()

# Подключение к базе данных
##conn = sqlite3.connect(r'C:\Users\T-IT17\Desktop\Даниил Ермолов\БАЗА ДАННЫХ\departments.db')
conn = sqlite3.connect('departments.db')
cursor = conn.cursor()

# Создание главного окна приложения
root = tk.Tk()
root.geometry('1490x700')
root.title('Отделы и сотрудники')
root.resizable(False, False)

fr_back = tk.Frame(root, width=1500, height=700)
fr_back.place(x=0, y=0)

# Создание таблицы отделов
tree_departments = ttk.Treeview(fr_back, columns=('id', 'count', 'name'), height=15)
tree_departments.heading('id', text='ID')
tree_departments.heading('count', text='Кол-во сотрудников')
tree_departments.heading('name', text='Название')
tree_departments.column('#0', width=10)
tree_departments.column('id', width=40)
tree_departments.column('count', width=50)
tree_departments.column('name', width=200)
tree_departments.place(x=0, y=0)
tree_departments.bind("<<TreeviewSelect>>", item_selected)


update_db()
    

# Создание таблицы сотрудников
tree_employees = ttk.Treeview(fr_back, columns=('id', 'surname', 'name', 'surname2', 'salary', 'bonus', 'vacation', 'date', 'position', 'department_id'), height=15)
tree_employees.heading('id', text='ID')
tree_employees.heading('surname', text='Фамилия')
tree_employees.heading('name', text='Имя')
tree_employees.heading('surname2', text='Отчество')
tree_employees.heading('salary', text='Зарплата')
tree_employees.heading('bonus', text='Премия')
tree_employees.heading('vacation', text='Отпуск')
tree_employees.heading('date', text='Дата приёма на работу ')
tree_employees.heading('position', text='Должность')
tree_employees.heading('department_id', text='ID отдела')
tree_employees.column('#0', width=10)
tree_employees.column('id', width=40)
tree_employees.column('surname', width=100)
tree_employees.column('name', width=100)
tree_employees.column('surname2', width=150)
tree_employees.column('salary', width=100)
tree_employees.column('bonus', width=100)
tree_employees.column('vacation', width=50)
tree_employees.column('date', width=160)
tree_employees.column('position', width=200)
tree_employees.column('department_id', width=80)
tree_employees.place(x=400, y=0)


frame_buttons = tk.Frame(root, width=1430, height=300)
frame_buttons.place(x=0, y=350)



button_fire_employee = tk.Button(frame_buttons, text='Уволить сотрудника', command=click_fire)
button_fire_employee.place(x = 100, y = 150)

button_send_to_vacation = tk.Button(frame_buttons, text='Отправить в отпуск', command=click_vacation)
button_send_to_vacation.place(x=300, y=150)

button_end_vacation = tk.Button(frame_buttons, text='Завершить отпуск', command=click_end_vacation)
button_end_vacation.place(x=500, y=150)

button_add_employee = tk.Button(frame_buttons, text='Добавить сотрудника',command=click_hire)
button_add_employee.place(x=700,y=150)

button_working_days = tk.Button(frame_buttons,text='Узнать время работы сотрудника',command=click_working_days)
button_working_days.place(x=900,y=150)

button_financing = tk.Button(frame_buttons, text='Рассчитать финансирование отдела',command=click_financing)
button_financing.place(x=1150,y=150)

# Запуск главного цикла приложения
root.mainloop()

