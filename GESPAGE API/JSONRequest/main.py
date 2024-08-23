import requests

#Funcion generar Token
def get_credentials(api_base_url, api_id, api_secret,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/credentials/{api_id}/{api_secret}"

        # Realizar la consulta GET a la API
        response = requests.get(url, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener la respuesta JSON
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error si el estado no es 200 OK
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Manejar cualquier excepción que ocurra durante la solicitud
        print(f"Request failed: {e}")
        return None

#Funcion informacion usuario
def put_user_get_info(api_base_url, token, json_body,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/user_get_info/{token}"

        # Realizar la consulta PUT a la API
        response = requests.put(url,json=json_body, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            print(f"CODE: {response.status_code}")
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Manejar cualquier excepción
        print(f"Request failed: {e}")
        return None

#Funcion agregar usuario
def post_user_add(api_base_url, token, json_body,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/user_add/{token}"

        #Realizar la consulta POST a la API
        response = requests.post(url, json=json_body, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            print(f"CODE: {response.status_code}")
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        #Manejar cualquier excecpion
        print(f"Reques failed: {e}")
        return None

#Funcion editar usuario
def put_user_edit(api_base_url, token, json_body,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/user_edit/{token}"

        #Realizar la consulta POST a la API
        response = requests.put(url, json=json_body, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            print(f"CODE: {response.status_code}")
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        #Manejar cualquier excecpion
        print(f"Reques failed: {e}")
        return None

#Funcion eliminar usuario
def put_user_delete(api_base_url, token, json_body,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/user_delete/{token}"

        #Realizar la consulta POST a la API
        response = requests.put(url, json=json_body, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            print(f"CODE: {response.status_code}")
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        #Manejar cualquier excecpion
        print(f"Reques failed: {e}")
        return None

#Funcion actualizar creditos
def post_user_upd_balance(api_base_url, token, json_body,headers=None):
    try:
        # Construir la URL completa con los parámetros de ruta
        url = f"{api_base_url}/pserver/rs/public/user_upd_balance/{token}"

        #Realizar la consulta POST a la API
        response = requests.post(url, json=json_body, headers=headers)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            print(f"CODE: {response.status_code}")
            data = response.json()
            return data
        else:
            # Imprimir un mensaje de error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        #Manejar cualquier excecpion
        print(f"Reques failed: {e}")
        return None

#Datos
api_base_url = "URL HERE"
api_id = "ID HERE"
api_secret = "SECRET HERE"

#Json Bodys
json_body_userGetInfo = {
    "username":"",
    "cardid":""
}

json_body_userAdd = {
    "username":"TestAPIV21000",
    "password":"223553112",
    "cardid":"12111223",
    "printcode":"4433323",
    "display_name":"TestV2",
    "email":"test@google.com",
    "comment":"testAPI",
    "limited": True,
    "department":"TI",
}

json_body_userEdit = {
    "username":"Api Test", #Identificar usuario a modificar
    "password":"",
    "cardid":"",
    "display":"",
    "email":"",
    "comment":"",
    "printcode":"12",
    "department":"servicios profesionales"
}

json_body_userDelete = {
    "username":"Test"
}

json_body_userUpdBalance = {
    "username":"TestAPIV21000",
    "cardid":"",
    "add_balance": -10,
    "log":"testBalance"
}

#Obtener TOKEN
credentials = get_credentials(api_base_url, api_id, api_secret)
api_token = credentials.get("token")
#print(credentials)
print(f"TOKEN: {api_token}")

#Obtener informacion de un usuario
#userInfo = put_user_get_info(api_base_url, api_token,json_body_userGetInfo)
#print(userInfo)

#Crear nuevo usuario
#userAdd = post_user_add(api_base_url,api_token,json_body_userAdd)
#print(userAdd)

#Editar un usuario
#userEdit = put_user_edit(api_base_url, api_token, json_body_userEdit)
#print(userEdit)

#Eliminar un usuario
#userDelete = put_user_delete(api_base_url, api_token, json_body_userDelete)
#print(userDelete)

#Actualizar creditos de un usuario
#userUpdBalance = post_user_upd_balance(api_base_url,api_token,json_body_userUpdBalance)
#print(userUpdBalance)



