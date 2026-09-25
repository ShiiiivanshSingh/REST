import json
from http.server import BaseHTTPRequestHandler, HTTPServer

tasks = [
    {"id": 1, "title": "Hello my name is Shivansh", "done": False},
    {"id": 2, "title": "Здравствуйте, меня зовут Шиванш.", "done": False}
]
next_id = 3

#   GET    /tasks       list everything
#   GET    /tasks/<id>  get one
#   POST   /tasks        create
#   PUT    /tasks/<id>  update
#   DELETE /tasks/<id>  delete


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        body = json.dumps(data).encode() if data is not None else b""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def path(self):
        p = self.path.strip("/").split("/")
        return p[0], int(p[1]) if len(p) > 1 and p[1].isdigit() else None

    def body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n)) if n else {}

    def do_GET(self):
        resource, id = self.path()
        if resource != "tasks":
            return self.send_json(404, {"error": "Not found"})

        if id is None:
            return self.send_json(200, tasks)

        task = next((t for t in tasks if t["id"] == id), None)
        return self.send_json(200, task) if task else \
            self.send_json(404, {"error": "Task not found"})

    def do_POST(self):
        global next_id
        resource, id = self.path()

        if resource != "tasks" or id is not None:
            return self.send_json(404, {"error": "Not found"})

        try:
            data = self.body()
        except:
            return self.send_json(400, {"error": "Invalid JSON body"})

        if not data.get("title"):
            return self.send_json(400, {"error": "title is required"})

        task = {"id": next_id, "title": data["title"], "done": False}
        next_id += 1
        tasks.append(task)
        self.send_json(201, task)

    def do_PUT(self):
        resource, id = self.path()

        if resource != "tasks" or id is None:
            return self.send_json(404, {"error": "Not found"})

        task = next((t for t in tasks if t["id"] == id), None)
        if not task:
            return self.send_json(404, {"error": "Task not found"})

        try:
            data = self.body()
        except:
            return self.send_json(400, {"error": "Invalid JSON body"})

        if "title" in data:
            task["title"] = data["title"]
        if "done" in data:
            task["done"] = data["done"]

        self.send_json(200, task)

    def do_DELETE(self):
        global tasks
        resource, id = self.path()

        if resource != "tasks" or id is None:
            return self.send_json(404, {"error": "Not found"})

        old = len(tasks)
        tasks = [t for t in tasks if t["id"] != id]

        if len(tasks) == old:
            return self.send_json(404, {"error": "Task not found"})

        self.send_json(204, None)


server = HTTPServer(("localhost", 3000), Handler)
print("http://localhost:3000")
server.serve_forever()
