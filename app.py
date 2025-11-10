from flask import Flask
import json
import os
import platform
import psutil

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {
            'integrantes':[
            "Erick Maestri de Souza",
            "Cecilia Lucchesi Mardegan"
            ] 
        }
    ])


@APP.get("/metricas")
def metricas():
    processo = psutil.Process(os.getpid())
    pid = processo.pid

    # Memória (MB)
    mem = psutil.virtual_memory().used / 1024**2

    # Uso médio de CPU
    cpu = psutil.cpu_percent(interval=0.1)

    # Sistema operacional
    sis = platform.platform()

    return (
        f"| Nome: Erick Maestri de Souza\n"
        f"| PID: {pid}\n"
        f"| Memória usada: {mem:.2f} MB\n"
        f"| CPU: {cpu:.2f}%\n"
        f"| Sistema Operacional: {sis}\n"
    )


