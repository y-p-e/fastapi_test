from fastapi import FastAPI
import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/users")
def read_root():
	random = randomname(5)
	random_email = random + "@example.com"
	return [
		{"username": "user1", "email": "user1@example.com"},
		{"username": "random-user", "email": random_email},
		]
