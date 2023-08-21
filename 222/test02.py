# MAGIC %sql
# MAGIC SELECT * FROM shouce01

import sys
import os

# In the command below, replace <username> with your Databricks user name.
sys.path.append(os.path.abspath('/Workspace/Repos/Test/ADF/111'))

import test01
test01.ctbl()