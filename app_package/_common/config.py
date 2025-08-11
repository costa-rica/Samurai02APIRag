import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv()
print(f"- .env: {find_dotenv()}")
print(f"- FSW_CONFIG_TYPE: {os.environ.get('FSW_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")


with open(os.path.join(os.environ.get('CONFIG_ROOT'), os.environ.get('CONFIG_FILE_NAME'))) as config_json_file:
    config_json_dict = json.load(config_json_file)

class ConfigBase:

    def __init__(self):

        self.SECRET_KEY = config_json_dict.get('SECRET_KEY')
        self.WEB_ROOT = os.environ.get('WEB_ROOT')
        self.DB_ROOT = os.environ.get('DB_ROOT')
        self.DESTINATION_PASSWORD = config_json_dict.get('DESTINATION_PASSWORD')
        self.PROJECT_RESOURCES_ROOT = os.environ.get('PROJECT_RESOURCES_ROOT')
        self.DIR_ASSETS = os.path.join(self.PROJECT_RESOURCES_ROOT,"assets")# website files like icons, favicons, other images
        self.DIR_ASSETS_IMAGES = os.path.join(self.DIR_ASSETS,"images")
        self.DIR_ASSETS_FAVICONS = os.path.join(self.DIR_ASSETS,"favicons")
        self.PATH_TO_RAG_CONTEXT_DATA = os.environ.get('PATH_TO_RAG_CONTEXT_DATA')
        self.PATH_TO_RAG_INDEX = os.environ.get('PATH_TO_RAG_INDEX')


class ConfigWorkstation(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
            

class ConfigDev(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
            

class ConfigProd(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = False


match os.environ.get('FSW_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- Samurai02APIRag/app_pacakge/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- Samurai02APIRag/app_pacakge/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- Samurai02APIRag/app_pacakge/config: Workstation')