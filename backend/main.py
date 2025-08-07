from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify frontend origin instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Simple response logic
    if "weather" in user_message.lower():
        reply = "Today's weather is sunny with a chance of rain."
    elif "crop" in user_message.lower():
        reply = "Based on your region, rice and maize are good options."
    elif "planting" in user_message.lower():
        reply = "You can start planting in early June for best yield."
    else:
        reply = "I can help with planting tips, crop suggestions, and weather updates."

    return {"reply": reply}


