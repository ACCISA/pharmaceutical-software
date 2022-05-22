import os
import ast
import shutil
from datetime import datetime
import asyncio
from pathlib import Path


day = datetime.today()
now = datetime.now()

prescriptions = os.listdir('Prescriptions/')
with open(f'Process/batch.txt', 'w') as f:
    for i in range(len(prescriptions)):

        content = open(f'Prescriptions/{prescriptions[i]}',"r")
        data = (content.read())
        data = ast.literal_eval(data)
        data = [n.strip() for n in data]

        f.write(f'{str(data)}\n')
        f.close()
        Path(f'Prescriptions/{prescriptions[i]}').rename(Path('Prescriptions Logs/{prescriptions[i]}'))


