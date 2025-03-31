from requests import post

print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 1, 'job': 'very smart job', 'work_size': 23, 'is_finished': False,
                 'collaborators': '2, 3'}).json())

print(post('http://localhost:8080/api/jobs', json={'team_leader': 1, 'work_size': 30}).json())
print(post('http://localhost:8080/api/jobs', json={"id": 3}).json())
print(post('http://localhost:8080/api/jobs', json={}).json())
