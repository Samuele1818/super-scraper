import os
from datetime import datetime

from mdutils.mdutils import MdUtils


def create_log():
    """
    Create the log file and the "logs" if not exists
    :return: Log file
    """
    try:
        # Create log folder if not exists
        if not os.path.exists("./logs/"):
            os.makedirs("./logs/")

        # Get the current date that will be the name of the log
        dt_string = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

        file_name = f"./logs/{dt_string}"

        # Create the md file
        mdAcme = MdUtils(file_name=file_name)
        print(f"Log {file_name} created")
        return mdAcme.create_md_file()

    except Exception as e:
        print(e)
        return None
