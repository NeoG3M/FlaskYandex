from requests import post, get, delete

print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/1000').json())

resp = post('http://localhost:8080/api/v2/users', json={"surname": "Попкин",
                                                        "name": "Иван",
                                                        "age": 14,
                                                        "position": "Помошник",
                                                        "speciality": "Сталелитейник",
                                                        "address": "Земля, дом Василия",
                                                        "email": "kidEmail@pupkin.ru",
                                                        "password": "iirjhhdd[d##"})
new_id = resp.json()['id']
print(resp.json())
print(get(f'http://localhost:8080/api/v2/users/{new_id}').json())
print(delete(f'http://localhost:8080/api/v2/users/{new_id}').json())

print(post('http://localhost:8080/api/v2/users', json={"surname": "Попкин",
                                                       "name": "Иван",
                                                       "age": 14,
                                                       "position": "Помошник",
                                                       "speciality": "Сталелитейник"
                                                       }).json())

print(delete(f'http://localhost:8080/api/v2/users/1000').json())
