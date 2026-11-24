from fastapi import FastAPI

app = FastAPI(title="Practice Tracker")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {
        "project": "Personal Tracker",
        "version": 1,
        "purpose": "Track coding practice"
    }

@app.get("/problems/{problem_id}")
def get_problem(problem_id:int):
    return {"requested_problem":problem_id}

@app.get("/search")
def search(topic:str,difficulty:str="easy"):
    return{
        "topic":topic,
        "difficulty":difficulty
    }