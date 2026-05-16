from fastapi import FastAPI 
import os
import subprocess
import shutil

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION")

if APP_VERSION is None:
    raise ValueError("APP_VERSION is not set")


#sys_uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()
def get_uptime():
    try:
        with open("/proc/uptime") as f:
            uptime_seconds = float(f.readline().split()[0])
            return f"{uptime_seconds:.2f} seconds"
    except:
        return "unknown"

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": APP_VERSION}

@app.get("/uptime")
def uptime():
    return {"uptime": get_uptime()}