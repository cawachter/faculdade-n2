def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Ola, administrador')
    else: 
        print('Ola, usuario')

loginUsuario('ADMIN')
loginUsuario('Admin')
loginUsuario('User')
loginUsuario('Usuario')
loginUsuario('teste')
loginUsuario('Camila')
