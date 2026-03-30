from fastapi import FastAPI

app = FastAPI()


rooms = [
    {"room_number": 101, "type": "Enkelrum", "price": 800},
    {"room_number": 102, "type": "Dubbelrum", "price": 1200},
    {"room_number": 103, "type": "Svit", "price": 2500}
]


@app.get("/rooms")
def get_all_rooms():
    return rooms  