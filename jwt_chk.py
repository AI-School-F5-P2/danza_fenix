import jwt

# Datos del payload (información que deseas incluir en el token)
payload = {'user_id': 123, 'username': 'root'}

# Clave secreta para firmar el token
secret_key = 'mi_clave_secreta'

# Generar el token JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)


# Token JWT a verificar
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoicm9vdCJ9.IrYxsvjvySTEv1mn7m0fjCghNu_0EijhCC2HNTHnrjU'

# Clave secreta utilizada para firmar el token
secret_key = 'mi_clave_secreta'

try:
    # Decodificar y verificar el token JWT
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    
    # El token es válido, se puede acceder a los datos del payload
    user_id = payload['user_id']
    username = payload['username']
    
    print('Token válido')
    print('user_id:', user_id)
    print('username:', username)
except jwt.InvalidTokenError:
    # El token es inválido o ha expirado
    print('Token inválido')
