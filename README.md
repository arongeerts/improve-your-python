# poetry-demo
An example project used to explain the most important features of Poetry

## Windows
How to run on windows:
0.  For the bellow commands I use powershell. CMD should work as well but is not recomended.
1.  Make sure python3.9 or higher is installed on your machine. (https://www.python.org/downloads/)
2.  Prepare your environment by running ```.\prep_win_env.ps1``` 
    It will install Poetry on your system, together with a windows wrapper to make a virtual environment.
    Poetry will also be installed in that virtual environment.
3.  You have now entered a virtual environment provisioned with the Poetry dependancys needed for you project.
4.  You can add or remove dependancys by running ```poetry add <packagename>``` or ```poetry remove <packagename>``` .
5.  Poetry will resolve dependancys for you while also preventing package conflicts.
6.  To reload your environment after you added/removed dependancys first run ```deactivate``` , remove the "venv" folder and then run step 2 again.
7.  Included in this project is basicscript.py - it will use the dependacys managed by poetry. 
    Execute the file to see it's output. (It needs valid AWS creds)