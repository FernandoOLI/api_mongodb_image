import json
import os
from json import dumps

from enviroment.enviroment_variables import AZURE_BACKUP, AZURE_NAME
from enviroment.enviroment_variables import CLIENT_DATABASE, DATABASE, COLLECTION, CONTADOR, AZURE_CONNECTION, \
    AZURE_CONTAINER, TEMP_PATH

import pymongo

# def read_from_mongo():
#     return mycol.find_one()


# Variáveis de ambiente
myclient = pymongo.MongoClient(CLIENT_DATABASE)
mydb = myclient[str(DATABASE)]
mycol = mydb[str(COLLECTION)]
tmp_path = TEMP_PATH

contador = CONTADOR
azure = AZURE_CONNECTION
container = AZURE_CONTAINER
backup = AZURE_BACKUP
azure_name = AZURE_NAME


def read_from_mongo():
    print(str(mycol.find_one()))
    json_data = str(mycol.find_one())

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    result = json.dumps(json_data, default=set_default)
    return result
