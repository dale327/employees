import datetime
import sqlite3 as sl
import tkinter as tk


class Employee:

    def get_salary(ID):
        cursor.execute(f'SELECT Salary FROM employees WHERE ID={ID}')
        print(cursor.fetchone())

    def get_bonus(ID):
        cursor.execute(f'SELECT Bonus FROM employees WHERE ID={ID}')
        print(cursor.fetchone())

    def get_position(ID):
        cursor.execute(f'SELECT Position FROM employees WHERE ID={ID}')
        print(cursor.fetchone())

    def working_days(con, cursor, working_days_win, ID):
        cursor.execute(f'SELECT Date FROM employees WHERE ID = {ID} ')
        date = cursor.fetchone()
        date = date[0].split(',')
        for i in range(len(date)):
            date[i] = int(date[i])
        date = datetime.date(date[0], date[1], date[2])
        date2 = datetime.date.today()
        delta = date2 - date
        tk.messagebox.showinfo(title="", message=f"Сотрудник под номером {ID} работает в компании уже {delta}")
        working_days_win.destroy()

    def go_vacation(con, cursor, vacation_win, ID):
        global b
        cursor.execute(f'SELECT Vacation FROM employees WHERE ID = {ID}')
        a = cursor.fetchone()
        if a[0] == 1:
            tk.messagebox.showinfo(title="", message=f"Сотрудник под номером {ID} уже находится в отпуске!")
        else:
            cursor.execute(f'UPDATE employees SET Vacation = True WHERE ID = {ID}')
            con.commit()
            tk.messagebox.showinfo(title="", message=f"Сотрудник под номером {ID} отправлен в отпуск")
            vacation_win.destroy()

    def end_vacation(con, cursor, end_vacation_win, ID):
        cursor.execute(f'UPDATE employees SET Vacation = False WHERE ID = {ID}')
        con.commit()
        tk.messagebox.showinfo(title="", message=f'Вы отменили отпуск сотрудника {ID}')
        end_vacation_win.destroy()

    def add_employee(con, cursor, hire_win, ID, Surname, Name, Surname2, Salary, Bonus, Vacation, Date, Position,
                     DepartmentID):

        sql = 'INSERT INTO employees (ID, Surname, Name, Surname2, Salary, Bonus, Vacation, Date, Position, DepartmentID) values (?,?,?,?,?,?,?,?,?,?)'
        data = [(ID, Surname, Name, Surname2, Salary, Bonus, Vacation, Date, Position, DepartmentID)]
        if not isinstance(ID, int):
            print('Error')
            return
        if not isinstance(Surname, str):
            print('Error')
            return
        if not isinstance(Name, str):
            print('Error')
            return
        if not isinstance(Surname2, str):
            print('Error')
            return
        if not isinstance(Salary, int):
            print('Error')
            return
        if not isinstance(Bonus, int):
            print('Error')
            return
        if not isinstance(Vacation, bool):
            print('Error')
            return
        if not isinstance(Date, str):
            print('Error')
            return
        if not isinstance(Position, str):
            print('Error')
            return
        if not isinstance(DepartmentID, int):
            print('Error')
            return

        con.executemany(sql, data)
        con.commit()
        tk.messagebox.showinfo(title="", message=f"Сотрудник под номером {ID} успешно добавлен!")
        hire_win.destroy()

    def del_employee(con, cursor, fire_win, ID):
        cursor.execute(f'DELETE FROM employees WHERE ID = {ID}')
        con.commit()
        tk.messagebox.showinfo(title="", message=f"Сотрудник под номером {ID} успешно удален!")
        fire_win.destroy()


class Department:
    conn = sl.connect('departments.db')
    cursor = conn.cursor()

    def get_employees(ID):
        cursor.execute(f'SELECT numd, employees FROM departments WHERE numd = {ID}')
        a, b = cursor.fetchone()
        print(f'В {a} отделе {b} сотрудников')

    def financing(con, cursor, financing_win, ID):
        totalsalary = 0
        cursor.execute(f'SELECT Salary, Bonus FROM employees WHERE DepartmentID = {ID}')
        a = cursor.fetchall()
        for i in a:
            totalsalary += i[0]
            totalsalary += i[1]
        tk.messagebox.showinfo(title="", message=f"Отдел номер {ID} получает финансирование в размере {totalsalary}₽")
        financing_win.destroy()
