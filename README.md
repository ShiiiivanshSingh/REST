<div align="center">
  
![REST API](https://capsule-render.vercel.app/api?type=transparent&height=100&color=gradient&text=REST%20API&animation=fadeIn&textBg=false)


A tiny REST API built from scratch using Python's `http.server`.

</div>


## CRUD

```text
GET     /tasks       → list tasks
GET     /tasks/<id>  → get task
POST    /tasks       → create task
PUT     /tasks/<id>  → update task
DELETE  /tasks/<id>  → delete task
```

## Server

```python
server = HTTPServer(("localhost", 3000), Handler)
server.serve_forever()
```

<div align="center">

<img width="625" height="309" alt="image" src="https://github.com/user-attachments/assets/fb11b659-a86c-4398-ba3c-08b85596e47f" />


</div>

## Requests

```bash
python3 server.py
```

```bash
curl http://localhost:3000/tasks
```

<div align="center">

<img width="1750" height="1158" alt="commands" src="https://github.com/user-attachments/assets/e6896626-cebb-47ae-806f-9d4014da32cd" />

</div>

## GET

```text
GET /tasks
GET /tasks/<id>
```

<div align="center">

<img width="5624" height="5207" alt="GET" src="https://github.com/user-attachments/assets/e589c491-45a1-41a5-b2a1-279303f40518" />

</div>

## POST

```text
POST /tasks
```

```json
{"title": "Learn Python"}
```

<div align="center">

<img width="5278" height="5134" alt="POST" src="https://github.com/user-attachments/assets/e49aabf7-c1ff-49ff-b29a-499f9fed0936" />

</div>

## PUT

```text
PUT /tasks/<id>
```

```json
{"done": true}
```

<div align="center">

<img width="5624" height="5207" alt="PUT" src="https://github.com/user-attachments/assets/18fdacf6-e54d-4943-bd97-559f470877d0" />

</div>

## DELETE

```text
DELETE /tasks/<id>
```

<div align="center">

<img width="5365" height="4503" alt="DELETE" src="https://github.com/user-attachments/assets/6ff289e9-1214-41dd-932f-2a859968f88b" />

</div>

## Implementation

```text
BaseHTTPRequestHandler
        │
        ├── do_GET()
        ├── do_POST()
        ├── do_PUT()
        └── do_DELETE()
                │
                ▼
          In-memory tasks
```

JSON request and response handling is done using Python's built-in `json` module.
