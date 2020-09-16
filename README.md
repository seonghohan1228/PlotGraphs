Create a folder named 'data' and put the HDF5 data files in there.

In the terminal type:
virtualenv venv
source venv/bin/activate

To check if virtualenv is successfully activated, type:
which python3

Then the path should be:
current_folder/venv/bin/python3

To install the required packages, type:
pip3 install -r requirements.txt

When you are over, in the terminal and type:
deactivate
