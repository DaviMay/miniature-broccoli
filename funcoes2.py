def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem vindo Administrador')
    else:
        print('bem vindo Usuário')

loginUsuario('Admin')
loginUsuario('admin')    
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('user')
loginUsuario('Usuário')
loginUsuario('usuario')
loginUsuario('Usuario')