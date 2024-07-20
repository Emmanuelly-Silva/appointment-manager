from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from PIL import Image, ImageTk
from datetime import date, datetime
import re

from view import *


class Colors:
    def __init__(self):
        self.white = '#FEFFFF'
        self.blue = '#038CFC'
        self.red = '#DC2700'
        self.gray = '#808080'  
        self.light_green = '#04AA6D'
        self.light_gray = '#E9EDF5'
        self.black = '#000000'


class Fonts:
    def __init__(self):
        self.header = font.Font(family="Calibri", size=19, weight='bold')
        self.lb_form = font.Font(family="Calibri", size=14, weight='bold')
        self.info_form = font.Font(family="Arial", size=13)
        self.btn_form = font.Font(family='Calibri', size=14, weight='bold')


class Application:
    def __init__(self):
        root = Tk()
        self.root = root
        self.available_times = {}
        self.color = Colors()
        self.font = Fonts()

        self.screen()
        self.create_frames()
        self.create_widgets()
        self.show_table()
        self.root.mainloop()

    def screen(self):
        self.root.title('Gerenciamento de consultas')
        self.root.configure(background=self.color.light_gray)
        self.root.geometry('1250x550')
        self.root.resizable(False, False)

    def create_frames(self):
        self.top_left_frame = Frame(
            self.root, width=400, height=50, background=self.color.light_green, relief='flat'
        )
        self.top_left_frame.grid(row=0, column=0, sticky=NSEW)
        self.top_left_frame.grid_propagate(False)

        self.bottom_left_frame = Frame(
            self.root, width=400, height=500, background=self.color.white, relief='flat'
        )
        self.bottom_left_frame.grid(row=1, column=0, sticky=NSEW)
        self.bottom_left_frame.grid_propagate(False)

        self.right_frame = Frame(
            self.root, width=850, height=500, background=self.color.light_gray, borderwidth=3,
            highlightbackground=self.color.light_green, highlightthickness=2
        )
        self.right_frame.grid(row=0, column=1, rowspan=2, sticky=NSEW)
        self.right_frame.grid_propagate(False)

    def create_widgets(self):
        lb_app = Label(
            self.top_left_frame, text='Agendamento de Consulta', font=self.font.header,
            background=self.color.light_green, foreground=self.color.white
        )
        lb_app.grid(row=0, column=0, padx=(60, 55), pady=(8, 8))

        lb_name = Label(
            self.bottom_left_frame, text='Nome *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_name.grid(row=0, column=0, sticky='W', pady=(5, 5), padx=15)

        self.e_name = Entry(
            self.bottom_left_frame, width=40, justify='left', relief='solid', font=self.font.info_form,
            bg=self.color.white
        )
        self.e_name.grid(row=1, column=0, sticky='W', padx=(18, 4))

        lb_email = Label(
            self.bottom_left_frame, text='Email *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_email.grid(row=2, column=0, sticky='W', pady=(15, 5), padx=15)

        self.e_email = Entry(
            self.bottom_left_frame, width=40, justify='left', relief='solid', font=self.font.info_form,
            bg=self.color.white
        )
        self.e_email.grid(row=3, column=0, sticky='W', padx=(18, 4))

        lb_phone = Label(
            self.bottom_left_frame, text='Telefone *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_phone.grid(row=4, column=0, sticky='W', pady=(15, 5), padx=15)

        self.e_phone = Entry(
            self.bottom_left_frame, width=40, justify='left', relief='solid', font=self.font.info_form
        )
        self.e_phone.grid(row=5, column=0, sticky='W', padx=(18, 4))

        lb_cons_date = Label(
            self.bottom_left_frame, text='Data da Consulta *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_cons_date.grid(row=6, column=0, sticky='W', pady=(15, 5), padx=15)

        self.cal_cons_date = DateEntry(
            self.bottom_left_frame, width=15, background='darkblue', foreground='white', borderwidth=2,
            date_pattern='dd/mm/yyyy', font=self.font.info_form, locale='pt_BR'
        )
        self.cal_cons_date.grid(row=7, column=0, sticky='W', padx=20)

        lb_cons_time = Label(
            self.bottom_left_frame, text='Horário *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_cons_time.grid(row=6, column=0, sticky='W', pady=(15, 5), padx=220)

        self.cb_cons_time = ttk.Combobox(
            self.bottom_left_frame, width=15, state='disable', justify='left',
            font=self.font.info_form
        )
        self.cb_cons_time.grid(row=7, column=0, sticky='W', padx=224)
        
        lb_cons_specialty = Label(
            self.bottom_left_frame, text='Especialidade *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_cons_specialty.grid(row=8, column=0, sticky='W', pady=(15, 5), padx=15)
        
        self.values_specialty = [
            'Selecione',
            'Cardiologia',
            'Dermatologia',
            'Endocrinologia',
            'Neurologia',
            'Oftalmologia',
            'Ortopedia',
            'Pediatria'
        ]

        self.cb_cons_specialty = ttk.Combobox(
            self.bottom_left_frame, values=self.values_specialty, width=15, state='readonly', justify='left',
            font=self.font.info_form
        )
        self.cb_cons_specialty.set(self.values_specialty[0])
        self.cb_cons_specialty.grid(row=9, column=0, sticky='W', padx=(20, 4))
        self.cb_cons_specialty.bind('<<ComboboxSelected>>', self.update_times)

        lb_cons_priority = Label(
            self.bottom_left_frame, text='Prioridade *', font=self.font.lb_form, bg=self.color.white,
            fg=self.color.black
        )
        lb_cons_priority.grid(row=8, column=0, sticky='W', pady=(15, 5), padx=220)

        self.values_priority = [
            'Selecione',
            'Não Urgente', 
            'Pouco Urgente', 
            'Urgente', 
            'Muito Urgente', 
            'Emergência'  
        ]

        self.cb_cons_priority = ttk.Combobox(
            self.bottom_left_frame, values=self.values_priority, width=15, state='readonly', justify='left',
            font=self.font.info_form
        )
        self.cb_cons_priority.set(self.values_priority[0])
        self.cb_cons_priority.grid(row=9, column=0, sticky='W', padx=224)

        self.add_icon = ImageTk.PhotoImage(Image.open("images/add_icon_btn.png").resize((24, 24)))
        self.btn_add = Button(
            self.bottom_left_frame, text=' Agendar', bg=self.color.light_green, width=140, height=30,
            fg=self.color.white, font=self.font.btn_form, relief=RAISED, overrelief=RIDGE,
            highlightthickness=2, highlightbackground=self.color.light_green, image=self.add_icon,
            compound=LEFT, activebackground=self.color.light_green, activeforeground=self.color.white,
            command=self.insert_info
        )
        self.btn_add.grid(row=10, column=0, sticky='W', pady=(30, 5), padx=40)
        
        self.btn_state = False
        self.update_icon = ImageTk.PhotoImage(Image.open("images/edit_icon_btn.png").resize((24, 24)))
        btn_update = Button(
            self.bottom_left_frame, text=' Atualizar', bg=self.color.blue, width=140, height=30,
            fg=self.color.white, font=self.font.btn_form, relief=RAISED, overrelief=RIDGE,
            highlightthickness=2, highlightbackground=self.color.blue, image=self.update_icon,
            compound=LEFT, activebackground=self.color.blue, activeforeground=self.color.white,
            command=self.update_info
        )
        btn_update.grid(row=10, column=0, sticky='W', pady=(30, 5), padx=210)
        
        self.delete_icon = ImageTk.PhotoImage(Image.open("images/trash_icon_btn.png").resize((22, 22)))
        self.btn_delete = Button(
            self.bottom_left_frame, text=' Deletar', bg=self.color.red, width=140, height=30,
            fg=self.color.white, font=self.font.btn_form, relief=RAISED, overrelief=RIDGE,
            highlightthickness=2, highlightbackground=self.color.red, image=self.delete_icon,
            compound=LEFT, activebackground=self.color.red, activeforeground=self.color.white, 
            command=self.delete_info
        )
        self.btn_delete.grid(row=11, column=0, sticky='W', pady=(15, 5), padx=40)

        self.clear_icon = ImageTk.PhotoImage(Image.open("images/clear_icon_btn.png").resize((24, 24))) 
        btn_clear = Button(
            self.bottom_left_frame, text=' Limpar', bg=self.color.gray, width=140, height=30,
            fg=self.color.white, font=self.font.btn_form, relief=RAISED, overrelief=RIDGE,
            highlightthickness=2, highlightbackground=self.color.gray, image=self.clear_icon,
            compound=LEFT, activebackground=self.color.gray, activeforeground=self.color.white,
            command=self.clear_info
        )
        btn_clear.grid(row=11, column=0, sticky='W', pady=(15, 5), padx=210)

    def update_times(self, event):
        selected_specialty = self.cb_cons_specialty.get()
        selected_date = self.cal_cons_date.get_date()

        times = self.get_available_times(selected_specialty, selected_date)

        self.cb_cons_time['values'] = times
        self.cb_cons_time.state(["!disabled"])
        self.cb_cons_time.state(["readonly"])

    def get_available_times(self, selected_specialty, selected_date):
        weekday_times = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
        weekend_times = ['Indisponível']

        if selected_specialty not in self.available_times:
            self.available_times[selected_specialty] = {}

        if selected_date not in self.available_times[selected_specialty]:
            if selected_date.weekday() == 5 or selected_date.weekday() == 6:
                self.available_times[selected_specialty][selected_date] = weekend_times
            else:
                self.available_times[selected_specialty][selected_date] = weekday_times
        return self.available_times[selected_specialty][selected_date]

    def info_validations(self):
        def phone_validation(phone):
            regexp = re.compile(r'^(\(\d{2}\)|\d{2})\s?(\d{4,5})-?(\d{4})$')
            return bool(regexp.fullmatch(phone))

        def date_validation(date_info):
            try:
                current_day = date.today()
                calendar_date = datetime.strptime(date_info, '%d/%m/%Y').date()
                return current_day <= calendar_date
            except ValueError:
                return False

        def email_validation(email):
            regexp = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            return bool(regexp.fullmatch(email))

        email_info = self.e_email.get()
        phone_info = self.e_phone.get()
        date_info = self.cal_cons_date.get()
        time_info = self.cb_cons_time.get()
        specialty_info = self.cb_cons_specialty.get()
        errors = []

        if not phone_validation(phone_info):
            errors.append("Telefone inválido.")
        if not date_validation(date_info):
            errors.append("Data inválida ou no passado.")
        if not email_validation(email_info):
            errors.append("Email inválido.")
    
        if errors:
            messagebox.showerror("Erros de Validação", "\n".join(errors))
            return False
        else:
            selected_date = self.cal_cons_date.get_date()
            if time_info in self.available_times[specialty_info][selected_date]:
                self.available_times[specialty_info][selected_date].remove(time_info)
            return True

    def insert_info(self):
        name = self.e_name.get()
        email = self.e_email.get()
        phone = self.e_phone.get()
        date = self.cal_cons_date.get()
        time = self.cb_cons_time.get()
        priority = self.cb_cons_priority.get()
        specialty = self.cb_cons_specialty.get()
        insert_list = [name, email, phone, date, time, specialty, priority] 

        if any(info == '' for info in insert_list):
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchido.')
        else:
            if self.info_validations():
                create_form_data(insert_list)
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso.')
                self.clear_info()
                for widget in self.right_frame.winfo_children():
                    widget.destroy()
                self.show_table()
            else:
                messagebox.showerror('Erro', 'Informações inválidas')

    def update_info(self):
        if not self.btn_state:
            self.btn_add['state'] = 'disabled'
            self.btn_delete['state'] = 'disabled'
            try:
                treeview_data = self.tree.focus()
                treeview_dict = self.tree.item(treeview_data)
                tree_list = treeview_dict['values']
                self.id_value = tree_list[0]

                self.old_date = datetime.strptime(tree_list[4], '%d/%m/%Y').date()
                self.old_time = tree_list[5]
                self.old_specialty = tree_list[6]

                self.clear_info()

                self.e_name.insert(0, tree_list[1])
                self.e_email.insert(0, tree_list[2])
                self.e_phone.insert(0, tree_list[3])
                self.cal_cons_date.delete(0, 'end')
                self.cal_cons_date.insert(0, tree_list[4])

                self.cb_cons_time['values'] = self.get_available_times(
                    tree_list[6], self.cal_cons_date.get_date() 
                )
                self.cb_cons_time.set(tree_list[5])
                self.cb_cons_time.state(["!disabled"])
                self.cb_cons_time.state(["readonly"])

                self.cb_cons_specialty.set(tree_list[6])
                self.cb_cons_priority.set(tree_list[7])
                
                self.btn_state = True
            except IndexError:
                messagebox.showerror('Erro', 'Selecione um dos dados na tabela')
        else: 
            self.confirm_update()
            if self.old_time not in self.available_times[self.old_specialty][self.old_date]:
                self.available_times[self.old_specialty][self.old_date].append(self.old_time)
                self.available_times[self.old_specialty][self.old_date].sort()

    def confirm_update(self):
        self.btn_add['state'] = 'normal'
        self.btn_delete['state'] = 'normal'

        name = self.e_name.get()
        email = self.e_email.get()
        phone = self.e_phone.get()
        date = self.cal_cons_date.get()
        time = self.cb_cons_time.get()
        priority = self.cb_cons_priority.get()
        specialty = self.cb_cons_specialty.get()

        insert_list = [name, email, phone, date, time, specialty, priority, self.id_value]
        if any(info == '' for info in insert_list):
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchido.')
        else:
            if self.info_validations():
                update_form_data(insert_list)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso.')
                self.clear_info()
                for widget in self.right_frame.winfo_children():
                    widget.destroy()
                self.show_table()
                self.btn_state = False

    def delete_info(self):
        try:
            treeview_data = self.tree.focus()
            treeview_dict = self.tree.item(treeview_data)
            tree_list = treeview_dict['values']
            id_value = [tree_list[0]]

            delete_form_data(id_value)
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso.')
            for widget in self.right_frame.winfo_children():
                widget.destroy()
            self.show_table()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def clear_info(self):
        self.e_name.delete(0, 'end')
        self.e_email.delete(0, 'end')
        self.e_phone.delete(0, 'end')

        current_day = date.today()
        self.cal_cons_date.set_date(current_day)

        self.cb_cons_time['values'] = []
        self.cb_cons_time.set('')
        self.cb_cons_time.state(['disabled'])

        self.cb_cons_priority.set(self.values_priority[0])
        self.cb_cons_specialty.set(self.values_specialty[0])
        
    def show_table(self):
        users_values = read_form_data()

        list_header = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Horário', 'Especialidade', 'Prioridade']

        self.tree = ttk.Treeview(self.right_frame, columns=list_header, show='headings', selectmode='extended')
        self.tree.grid(row=0, column=0, sticky=NSEW)

        self.vsb = ttk.Scrollbar(self.right_frame, orient='vertical', command=self.tree.yview)
        self.vsb.grid(row=0, column=1, sticky=NS)
        self.hsb = ttk.Scrollbar(self.right_frame, orient='horizontal', command=self.tree.xview)
        self.hsb.grid(row=1, column=0, sticky=EW)

        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        col_sizes = [40, 160, 160, 110, 90, 90, 130, 130]
        for i, col in enumerate(list_header):
            self.tree.heading(col, text=col, anchor=W)
            self.tree.column(col, width=col_sizes[i], anchor=NW)

        for item in users_values:
            self.tree.insert('', 'end', values=item)


Application()
