from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """

    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***********************
    * General controllers *
    ***********************
    """   

    def main_menu(self):
        o = '0'
        while o != '8':
            self.view.main_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.admin_menu()
            elif o == '2':
                self.user_menu()
            elif o == '3':
                self.movie_menu()
            elif o == '4':
                self.hall_menu()
            elif o == '5':
                self.seat_menu()
            elif o == '6':
                self.schedule_menu()
            elif o == '7':
                self.ticket_menu()
            elif o == '8':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals
    
    """
    ********************
    * General for admin's *
    ********************
    """

    def admin_menu(self):
        o = '0'
        while o != '7':
            self.view.admin_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_admin() 
            elif o == '3':
                self.read_all_admin()
            elif o == '4':
                self.read_admin_name()
            elif o == '5':
                self.update_admin()
            elif o == '6':
                self.delete_admin()
            else:
                self.view.not_valid_option()
        return

    
    def ask_admin(self):
        self.view.ask('Nombre: ')
        a_name = input()
        self.view.ask('Apellido: ')
        a_lastName = input()
        self.view.ask('Correo eléctronico: ')
        a_email = input()
        self.view.ask('Teléfono: ')
        a_phone = input()
        return [a_name, a_lastName, a_email, a_phone] 
    
    def create_admin(self):
        a_name,a_lastName,a_email,a_phone = self.ask_admin()
        out = self.model.create_admin(a_name,a_lastName,a_email,a_phone)
        if out == True:
            self.view.ok(a_name+' '+a_lastName +' Correo eléctronico: '+ a_email+' ',' agrego')
        else:
            self.view.error('No se pudo agregar el producto')
        return
    
    def read_admin(self):
        self.view.ask('ID Admin: ')
        id_admin = input()
        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header('Datos del administrador con id: '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if dir == None:
                self.view.error('El ID del administrador no existe')
            else:
                self.view.error('Hay un problema al leer el administrador')
        return
    
    def read_all_admin(self):
        admins = self.model.read_all_admin()
        if type(admins) ==  list:
            self.view.show_admin_header(' Todos los administradores ')
            for admin in admins:
                self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Hay un problema al leer los administradores ')
        
    
    def read_admin_name(self):
        self.view.ask('Nombre: ')
        a_name = input()
        a_names = self.model.read_admin_name(a_name)
        if type(a_names) == list:
            self.view.show_admin_header('Administradores con el nombre:  '+a_name+' ')
            for a_name in a_names:
                self.view.show_a_admin(a_name)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Hay un problema al leer los administradores ')
        return
    

    def update_admin(self):
        self.view.ask('Administrador a modificar: ')
        id_admin = input()
        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if admin == None:
                self.view.error('El administrador no exíste')
            else:
                self.view.error('Hay un problema al leer el administrador')
            return
        self.view.msg(' Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals =self.ask_admin()
        fields, vals = self.update_lists(['a_name','a_lastName','a_email','a_phone'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields,vals)
        if out == True:
            self.view.ok(id_admin, 'actualizo')
        else: 
            self.view.error('No se pudo actualizar el administrador')
        return

    def delete_admin(self):
        self.view.ask('Administrador a borrar: ')
        id_admin = input()
        count = self.model.delete_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'borro')
        else:
            if count == 0:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al borrar el administrador')
        return

    """
    *********************
    * General for users *
    *********************
    """

    def user_menu(self):
        o = '0'
        while o != '7':
            self.view.user_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_user() 
            elif o == '3':
                self.read_all_user()
            elif o == '4':
                self.read_user_lname()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            else:
                self.view.not_valid_option()
        return

    
    def ask_user(self):
        self.view.ask('Nombre: ')
        u_name = input()
        self.view.ask('Apellido: ')
        u_lastName = input()
        self.view.ask('Correo eléctronico: ')
        u_email = input()
        self.view.ask('Teléfono: ')
        u_phone = input()
        return [u_name, u_lastName, u_email, u_phone] 
    
    def create_user(self):
        u_name, u_lastName, u_email, u_phone = self.ask_user()
        out = self.model.create_user(u_name, u_lastName, u_email, u_phone)
        if out == True:
            self.view.ok(u_name+' '+u_lastName +' Correo eléctronico: '+ u_email+' ',' agrego')
        else:
            self.view.error('No se pudo agregar el producto')
        return
    
    def read_user(self):
        self.view.ask('ID User: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario con el id: '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if dir == None:
                self.view.error('El ID del usuario no existe')
            else:
                self.view.error('Hay un problema al leer el usuario')
        return
    
    def read_all_user(self):
        users = self.model.read_all_user()
        if type(users) ==  list:
            self.view.show_user_header(' Todos los usuarios ')
            for user in users:
                self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Hay un problema al leer los usuarios ')
        
    
    def read_user_lname(self):
        self.view.ask('Apellido: ')
        u_lastName = input()
        u_lastNames = self.model.read_user_lname(u_lastName)
        if type(u_lastNames) == list:
            self.view.show_user_header('Usuarios con el nombre:  '+u_lastName+' ')
            for u_lastName in u_lastNames:
                self.view.show_a_user(u_lastName)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Hay un problema al leer los usuarios ')
        return
    

    def update_user(self):
        self.view.ask('Usuario a modificar: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del administrador '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if user == None:
                self.view.error('El usuario no exíste')
            else:
                self.view.error('Hay un problema al leer el usuario')
            return
        self.view.msg(' Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals =self.ask_admin()
        fields, vals = self.update_lists(['u_name','u_lastName','u_email','u_phone'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields,vals)
        if out == True:
            self.view.ok(id_user, 'actualizo')
        else: 
            self.view.error('No se pudo actualizar el usuario')
        return

    def delete_user(self):
        self.view.ask('Usuario a borrar: ')
        id_usuario = input()
        count = self.model.delete_admin(id_usuario)
        if count != 0:
            self.view.ok(id_usuario, 'borro')
        else:
            if count == 0:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al borrar el usuario')
        return
    
    def movie_menu(self):
        o = '0'
        while o != '7':
            self.view.movie_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movie()
            elif o == '4':
                self.read_movie_name()
            elif o == '5':
                self.update_movie()
            elif o == '6':
                self.delete_movie()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    
    def ask_movie(self):
        self.view.ask('Nombre: ')
        m_name = input()
        self.view.ask('Duración: ')
        m_duration = input()
        self.view.ask('Lenguaje: ')
        m_language = input()
        self.view.ask('Subtitulos: ')
        m_subtitles = input()
        return(m_name,m_duration,m_language,m_subtitles)
    
    def create_movie(self):
        m_name,m_duration,m_language,m_subtitles = self.ask_movie()
        out = self.model.create_movie(m_name,m_duration,m_language,m_subtitles)
        if out == True:
            self.view.ok(m_name+' en '+ m_language +' ('+m_duration+')', 'agrego')
        else:
            self.view.error('No se pudo agregar la película')
        return
    
    def read_a_movie(self):
        self.view.ask('ID de la película: ')    
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        print(movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Id Película: '+id_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('La película no existe')
            else:
                self.view.error('Hay un problema al leer la película')
        return
    
    def read_all_movie(self):
        movies = self.model.read_all_movie()
        if type(movies) == list:
            self.view.show_movie_header(' Todos las películas ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer las películas')
        return
    

    def read_movie_name(self):
        self.view.ask('Nombre: ')
        name = input()
        movies = self.model.read_movie_name(name)
        if type(movies) == list:
            self.view.show_movie_header('Películas con el título: '+name+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer las películas con ese nombre')
        return
    

    def update_movie(self):
        self.view.ask('ID de la película a modificar: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        m_name  = movie[1]
        if type(movie) == tuple:
            self.view.show_movie_header(' Datos de la película ' +m_name+'(Id: '+id_movie+ ') ')
            self.view.show_a_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('La película no existe')
            else:
                self.view.error('Problema al leer la película')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['m_name','m_duration','m_language', 'm_subtitles'], whole_vals)
        vals.append(id_movie)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(m_name+' (ID:'+id_movie+')', ' acutalizado')
        else:
            self.view.error('Error no se pudo actualizar la película')
        return
    
    def delete_movie(self):
        self.view.ask('ID del de la película a borrar: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        m_name  = movie[1]
        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.ok(m_name+' (ID:'+id_movie+')', ' borro')
        else:
            if count == 0:
                self.view.error('La película no existe')
            else:
                self.view.error('Prblema al borrar la película')
        return

    
    """ 
    ***************************
    * Controllers for halls   *
    ***************************
    """

    def hall_menu(self):
        o = '0'
        while o != '7':
            self.view.hall_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_a_hall()
            elif o == '3':
                self.read_all_hall()
            elif o == '4':
                self.read_hall_seat()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_hall(self):
        self.view.ask('Total de asientos: ')
        h_totalSeat = input()
        return [h_totalSeat]
    
    def create_hall(self):
        h_totalSeat = self.ask_hall()
        out = self.model.create_hall(h_totalSeat)
        if out == True:
            self.view.ok('La sala ','agrego')
        else:
            self.view.error('No se pudo agregar la sala')
        return
        

    def read_a_hall(self):
        self.view.ask('ID de la sala: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Datos de la sala  '+id_hall+' ')
            self.view.show_a_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Hay un problema al leer la sala')
        return
    
    def read_all_hall(self):
        halls = self.model.read_all_hall()
        if type(halls) ==  list:
            self.view.show_hall_header(' Todos las salas ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error(' Hay un problema al leer las salas ')
    
    def read_hall_seat(self):
        self.view.ask('Número de asientos: ')
        h_totalSeat = input()
        seats = self.model.read_hall_seat(h_totalSeat)
        print(seats)
        if type(seats) == list:
            self.view.show_hall_header('Salas con '+h_totalSeat+' asientos')
            for seat in seats:
                self.view.show_a_hall(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer las salas')
        return
    
    def update_hall(self):
        self.view.ask('Sala a modificar: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header(' Datos de la sala '+id_hall+ ' ')
            self.view.show_a_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la sala')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['h_totalSeat'], whole_vals)
        vals.append(id_hall)
        vals = tuple(vals)
        out = self.model.update_hall(fields,vals)
        if out == True:
            self.view.ok(id_hall, 'actualizo')
        else:
            self.view.error('Error, no se pudo actualizar la sala')
        return

    
    def delete_hall(self):
        self.view.ask('ID de la sala a borrar: ')
        id_hall = input()
        count = self.model.delete_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, 'Borro')
        else:
            if count == 0:
                self.view.error('La sala no exite')
            else:
                self.view.error('Prblema al borrar la sala')
        return
    
    
    """ 
    ***************************
    * Controllers for seat    *
    ***************************
    """

    def seat_menu(self):
        o = '0'
        while o != '9':
            self.view.seat_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_seat()
            elif o == '2':
                self.read_a_seat()
            elif o == '3':
                self.read_all_seat()
            elif o == '4':
                self.read_disp_seat()
            elif o == '5':
                self.read_seats_hall()
            elif o == '6':
                self.update_seat()
            elif o == '7':
                self.reset_seats()
            elif o == '8':
                self.delete_seat()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_seat(self):
        disp = 0 # Se define con el valor binario en 0 indicando que el asiento esta disponible al momento de crearlo
        self.view.ask('Sala: ')
        se_id_hall = input()
        return [disp, se_id_hall]
    
    def create_seat(self):
        dis, se_id_hall = self.ask_seat()
        out = self.model.create_seat(dis, se_id_hall)
        if out == True:
            self.view.ok('El asiento ','agrego')
        else:
            self.view.error('No se pudo agregar el asiento')
        return

    def read_a_seat(self):
        self.view.ask('ID del asiento: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)
        if type(seat) == tuple:
            self.view.show_seat_header('Datos del asiento  '+id_seat+' ')
            self.view.show_a_seat(seat)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if seat == None:
                self.view.error('El asiento no existe')
            else:
                self.view.error('Hay un problema al leer el asiento')
        return
    
    def read_all_seat(self):
        seats = self.model.read_all_seat()
        if type(seats) ==  list:
            self.view.show_seat_header(' Todos los asientos ')
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error(' Hay un problema al leer los asientos')
    
    def read_disp_seat(self):
        self.view.ask('Sala: ')
        hall = input()
        self.view.ask('Disponiblidad (libre/ocupado): ')
        disp = input()
        
        if (disp == 'libre'):
            disp = 0x00
        elif (disp == 'ocupado'):
            disp = 0x01
        seats = self.model.read_disp_seat(disp, hall)        
        if type(seats) == list:
            if (disp == 0x00):
                self.view.show_seat_header('Asientos disponibles' )
            else:
                self.view.show_seat_header('Asientos ocupados' )
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer los asientos')
        return

    def update_seat(self):
        self.view.ask('Asiento a reservar: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)   
        if (seat[1] == 0x01):
            print('El asiento ya esta ocupado, 1). Intentar nuevamente  | 2). Cancelar')
            op = input()
            if (op == '1'):
                self.update_seat()
            else:
                return

        if type(seat) == tuple:
            self.view.show_seat_header(' Datos del asiento '+id_seat+ ' ')
            self.view.show_a_seat(seat)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if seat == None:
                self.view.error('El asiento no existe')
            else:
                self.view.error('Problema al leer el asiento')
        
        whole_vals = [1, str(seat[2])]
        fields, vals = self.update_lists(['se_status', 'se_id_hall'], whole_vals)
        vals.append(id_seat)
        vals = tuple(vals)
        out = self.model.update_seat(fields,vals)
        if out == True:
            self.view.ok(id_seat, 'actualizo')
        else:
            self.view.error('Error, no se pudo actualizar el asiento')
        return
###############
    
    def reset_seats(self):
        self.view.ask('Sala de asientos a restablecer: ')
        se_id_hall = input()
        seats = self.model.read_seats_hall(se_id_hall)
        if type(seats) == list:
            for seat in seats:
                id_seat = seat[0]
                seat = self.model.read_seat(id_seat)      
                whole_vals = [0, str(seat[2])]
                fields, vals = self.update_lists(['se_status', 'se_id_hall'], whole_vals)
                vals.append(id_seat)
                vals = tuple(vals)
                out = self.model.update_seat(fields,vals)
                if out != True:
                    self.view.error('Error, no se pudo actualizar el asiento')
            self.view.ok('Los asientos', 'restablecieron')
        else:
            self.view.error('Error al leer los asientos')
        return
    
    def delete_seat(self):
        self.view.ask('ID del asiento a borrar: ')
        id_seat = input()
        count = self.model.delete_seat(id_seat)
        if count != 0:
            self.view.ok(id_seat, 'Borro')
        else:
            if count == 0:
                self.view.error('El asiento no existe')
            else:
                self.view.error('Prblema al borrar el  asiento')
        return
    """
    **********************
    *  Schedules menu    *
    **********************
    """
    
    def schedule_menu(self):
        o = '0'
        while o != '8':
            self.view.schedule_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.read_a_schedule()
            elif o == '3':
                self.read_all_schedule()
            elif o == '4':
                self.read_schedule_movie()
            elif o == '5':
                self.read_schedules_date()
            elif o == '6':
                self.update_schedule()
            elif o == '7':
                self.delete_schedule()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    
    def ask_schedule(self):
        self.view.ask('Hora: ')
        s_time = input()
        self.view.ask('Fecha: ')
        s_date = input()
        self.view.ask('ID película: ')
        s_id_movie = input()
        self.view.ask('ID de la sala: ')
        s_id_hall = input()
        return(s_time,s_date,s_id_movie,s_id_hall)
    
    def create_schedule(self):
        s_time,s_date,s_id_movie,s_id_hall = self.ask_schedule()
        out = self.model.create_schedule(s_time,s_date,s_id_movie,s_id_hall)
        movie = self.model.read_movie(s_id_movie)
        if out == True:
            self.view.ok(movie[1]+' a las '+ s_time +' el dia '+s_date+' en la sala: '+s_id_hall, 'agrego')
        else:
            self.view.error('No se pudo agregar la película')
        return
    
    def read_a_schedule(self):
        self.view.ask('ID del horario: ')    
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header('Id horario: '+id_schedule+' ')
            self.view.show_a_schedule(schedule)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if schedule == None:
                self.view.error('El horario no existe')
            else:
                self.view.error('Hay un problema al leer el horario')
        return
    
    def read_all_schedule(self):
        schedules = self.model.read_all_schedule()
        if type(schedules) == list:
            self.view.show_schedule_header(' Todos los horarios ')
            for schedule in schedules:
                print(schedule)
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer los horarios')
        return
    

    def read_schedule_movie(self):
        self.view.ask('Nombre: ')
        name = input()
        schedules = self.model.read_schedule_movie(name)
        if type(schedules) == list:
            self.view.show_schedule_header('Horaios para: '+name+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer los horarios')
        return
    
    def read_schedules_date(self):
        self.view.ask('Fecha: ')
        date = input()
        schedules = self.model.read_schedule_date(date)
        if type(schedules) == list:
            self.view.show_schedule_header('Horaios para el : '+date+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('Problema al leer los horarios')
        return
    

    def update_schedule(self):
        self.view.ask('ID del horario a modificar: ')
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Datos del horario ' +id_schedule)
            self.view.show_a_schedule(schedule)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if schedule == None:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al leer el horario')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_schedule()
        fields, vals = self.update_lists(['s_time','s_date','s_id_movie', 's_id_hall'], whole_vals)
        vals.append(id_schedule)
        vals = tuple(vals)
        out = self.model.update_schedule(fields,vals)
        if out == True:
            self.view.ok('El horario'+' (ID:'+id_schedule+')', ' acutalizado')
        else:
            self.view.error('Error no se pudo actualizar la película')
        return
    
    def delete_schedule(self):
        self.view.ask('ID del del horario a borrar: ')
        id_schedule = input()
        count = self.model.delete_schedule(id_schedule)
        if count != 0:
            self.view.ok('El horario'+' (ID:'+id_schedule+')', ' borro')
        else:
            if count == 0:
                self.view.error('El horario no existe')
            else:
                self.view.error('Prblema al borrar el horario')
        return
