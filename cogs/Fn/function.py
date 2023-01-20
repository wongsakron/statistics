import os
from dotenv import load_dotenv
load_dotenv()


ID = os.getenv("ID")

def fncheck(chorice):
        if chorice == 'True':
            chorice = False
        else :
            chorice = True
        return chorice

print("Import\t"+__name__)
