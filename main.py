import uvicorn
import subprocess
import threading
from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# FastAPI route for the homepage
@app.get("/")
async def read_root():
    return {"message": "FastAPI + Streamlit Game is Running!"}

# Function to run the Streamlit app as a subprocess
def start_streamlit():
    subprocess.run(["streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    # Run FastAPI app with Uvicorn in a separate thread
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8000)).start()

    # Start Streamlit app
    start_streamlit()
