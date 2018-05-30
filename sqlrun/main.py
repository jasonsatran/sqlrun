import yaml
import os
from sqlrun.container import Container
from sqlrun.redshift_processor import RedshiftProcessor
from sqlrun.redshift_process_factory import RedshiftFileProcessFactory

stream = open("redshift_config.yaml", "r")
data = yaml.load(stream)

def main():
    
    port = get_config_val("port")
    user = get_config_val("user")
    password = get_config_val("password")
    database = get_config_val("database")
    path_to_files = get_config_val("path_to_files")

    print("in main")



    
def get_config_val(key):
    value = data.get(key)
    if value == None:
        errStr = "key not found: " + key
        raise Exception(errStr)
    return value


if __name__ == "__main__":
    main()
