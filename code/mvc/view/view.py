class View:
    """
    ***************************
    * A view for a library DB *
    ***************************
    """
    def start(self):
        print('==================================')
        print('= Bienvenido a nuestro cine      =')
        print('==================================')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('======================================')
        print('=        Menu Administradores        =')
        print('======================================')
        print('1. Administradores')
        print('2. Usuarios')
        print('3. Películas')
        print('4. Salas')
        print('5. Asientos')
        print('6. Horarios')
        print('7. Ticket')
        print('8. Regresar')

    def user_main_menu(self):
        print('============================================')
        print('=        Menu principal de usuario         =')
        print('============================================')
        print('1. Usuarios')
        print('2. Películas')
        print('3. Horarios')
        print('4. Ticket')
        print('5. Regresar')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    def show_midder(self):
        print('-'*156)
    
    def show_footer(self):
        print('-'*156)
    
    def admin_menu(self):
        print('************************')
        print('* -- Submenu Admins -- *')
        print('************************')
        print('1. Agregar un administrador')
        print('2. Mostrar un administrador')
        print('3. Mostrar todos los administradores')
        print('4. Mostrar los administradores por nombre')
        print('5. Actualizar un administrador')
        print('6. Borrar un administrador')
        print('7. Regresar')
    
    def show_a_admin(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')
    
    def show_admin_header(self, header):
        print(header.center(78,'*'))
        print('ID'.ljust(6)+'|'+'Nombre'.ljust(35)+'|'+'Apellido'.ljust(35)+'|'+'Correo electronico'.ljust(35)+'|'+'Teléfono'.ljust(35))
        print('-'*156)

    
    def user_admin_menu(self):
        print('**************************')
        print('* -- Submenu Usuarios -- *')
        print('**************************')
        print('1. Mostrar un usuario')
        print('2. Mostrar todos los usuarios')
        print('3. Mostrar los usuarios por apellido')
        print('4. Regresar')

    def user_menu(self):
        print('**************************')
        print('* -- Submenu Usuarios -- *')
        print('**************************')
        print('1. Agregar un usuario')
        print('2. Mostrar un usuario')
        #print('3. Mostrar todos los usuarios')
        #print('4. Mostrar los usuarios por apellido')
        print('3. Actualizar un usuario')
        print('4. Borrar un usuario')
        print('5. Regresar')
    
    def show_a_user(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')
    
    def show_user_header(self, header):
        print(header.center(78,'*'))
        print('ID'.ljust(6)+'|'+'Nombre'.ljust(35)+'|'+'Apellido'.ljust(35)+'|'+'Correo electronico'.ljust(35)+'|'+'Teléfono'.ljust(35))
        print('-'*156)

    def show_user_midder(self):
        print('-'*156)
    
    def show_user_footer(self):
        print('-'*156)


    def movie_menu(self):
        print('*********************')
        print('* -- Submenu Movie -- *')
        print('*********************')
        print('1. Agregar película')
        print('2. Mostrar película')
        print('3. Mostrar todos las películas')
        print('4. Mostrar películas por nombre')
        print('5. Actualizar película')
        print('6. Borrar película')
        print('7. Regresar')

    def user_main_menu_movie(self):
        print('***************************')
        print('* -- Menú de películas -- *')
        print('***************************')
        print('1. Mostrar película')
        print('2. Mostrar todos las películas')
        print('3. Mostrar películas por nombre')
        print('4. Regresar')
    
    def show_a_movie(self, record):
        print('ID película: ', record[0])
        print('Nombre:', record[1])
        print('Duración: ', record[2])
        print('Idioma: ', record[3])
        print('Subtitulos: ', record[4])

    def show_movie_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_movie_midder(self):
        print('-'*53)
    
    def show_movie_footer(self):
        print('*'*53)
        
    
    """
    ***********************
    * A view for halls   *
    ***********************
    """
    def hall_menu(self):
        print('**************************')
        print('* -- Submenu Salas    -- *')
        print('**************************')
        print('1. Agregar una sala')
        print('2. Mostrar una sala')
        print('3. Mostrar todos las salas')
        print('4. Mostrar salas por número total de asientos')
        print('5. Actualizar sala')
        print('6. Borrar sala')
        print('7. Regresar')

    def show_hall_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_hall(self, record):
        print('ID:', record[0])
        print('Número total de asientos:', record[1])


    """
    ***********************
    * A view for seats    *
    ***********************
    """
    def seat_menu(self):
        print('*****************************')
        print('* -- Submenu Asientos    -- *')
        print('*****************************')
        print('1. Agregar un asiento')
        print('2. Mostrar un asiento')
        print('3. Mostrar todos los asientos')
        print('4. Mostrar asientos por estado (disponible/ocupado):')
        print('5. Mostrar asientos por sala') #UPDATE
        print('6. Reservar un asiento')
        print('7. Restablecer asientos')
        print('8. Borrar asiento')
        print('9. Regresar')

    def show_seat_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_seat(self, record):
        if record[1] == 0x00:
            disp = 'libre'
        else:
            disp = 'ocupado'
        print('ID:', record[0])
        print('Disponibilidad: ', disp)
        print('Sala:', record[2])
    
    def show_a_seat_disp(self, record):
        print('ID del asiento:', record[0])

    
    def schedule_menu(self):
        print('******************************')
        print('* -- Submenu Horarios    -- *')
        print('******************************')
        print('1. Agregar un horario')
        print('2. Mostrar un horario')
        print('3. Mostrar todos los horarios')
        print('4. Mostrar horarios por película')
        print('5. Mostrar horarios por día')
        print('6. Actualizar un horario')
        print('7. Borrar un horario')
        print('8. Regresar')
    
    def user_main_menu_schedule(self):
        print('******************************')
        print('* -- Submenu Horarios    --  *')
        print('******************************')
        print('1. Mostrar un horario')
        print('2. Mostrar todos los horarios')
        print('3. Mostrar horarios por película')
        print('4. Mostrar horarios por día')
        print('5. Regresar')

    def show_schedule_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_schedule(self, record):
        print('ID:', record[0])
        print('Fecha y hora:', str(record[2]) +', '+ record[1])
        print(record[6]+' en '+ record[8]+' subtitulada en '+ record[9] + ' ('+record[7]+')')
        print('Sala: ',record[4])
        
    
    
    """
    **************************
    * A view for horarios    *
    **************************
    """
    def ticket_menu(self):
        print('****************************')
        print('* -- Submenu Boletos    -- *')
        print('****************************')
        print('1. Agregar un ticket')
        print('2. Mostrar un ticket')
        print('3. Mostrar todos los tickets')
        print('4. Mostrar tickets por usuario:') #USUARIO
        print('5. Mostrar tickets por horario') #UPDATE
        print('6. Regresar')
    
    def user_main_menu_tickets(self):
        print('****************************')
        print('* -- Submenu Tickets    -- *')
        print('****************************')
        print('1. Agregar un ticket')
        print('2. Mostrar un ticket')
        print('3. Mostrar tickets por usuario:') 
        print('4. Regresar')

    def show_ticket_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_ticket(self, record1,record2):
        print('ID:', record1[0])
        print('Usuario:', record1[10], ' '+ record1[11]+' Correo: ' +record1[12])
        print('Fecha: ', str(record1[6])+' Hora: '+record1[5])
        print(record2[1] +' en '+ record2[3]+ ' subtitulada en '+ record2[4])
        print('Sala: ',str(record1[8]) +' asiento: '+str(record1[3]))
       

    
    