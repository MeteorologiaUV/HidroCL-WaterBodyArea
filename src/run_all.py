import os
import subprocess
import dotenv

dotenv.load_dotenv()
wd = os.getenv('WATERBODY_PATH')

os.chdir(wd)

subprocess.call(['python', '1_get_data.py'])
subprocess.call(['python', '2_order_data.py'])
subprocess.call(['python', '3_clean_data.py'])
subprocess.call(['python', '4_get_hidrocl_variable.py'])
