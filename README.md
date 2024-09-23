This is 

                   __         ______     ______    
                  /\ \       /\  ___\   /\  __ \   
                  \ \ \____  \ \  __\   \ \ \/\ \  
                   \ \_____\  \ \_____\  \ \_____\ 
                    \/_____/   \/_____/   \/_____/ 
                                
                              
Get an OpenAI Key from https://platform.openai.com/api-keys 

you need to put it in the Enviroment Variables 

For Windows:
Open System Properties:

Press Win + X, then click System.
On the left sidebar, click Advanced system settings.
Access Environment Variables:

In the System Properties window, click the Environment Variables button.
Create a New Environment Variable:

In the Environment Variables window, under User variables (for your user account) or System variables (for all users), click New.
Enter the Variable Name and Value:

For Variable name, enter: OPENAI_API_KEY
For Variable value, enter your OpenAI API key, e.g., sk-xxxxxx....
Save and Apply:

Click OK to save the new variable.
Click OK again in the Environment Variables window, and finally, click OK in the System Properties window.
Restart your Command Prompt:

Close any open Command Prompt or PowerShell windows for the new environment variable to take effect.

For macOS and Linux:
Open Terminal.

Edit the .bashrc or .zshrc file:

If you are using Bash, open the .bashrc file:
nano ~/.bashrc
If you are using Zsh, open the .zshrc file:
nano ~/.zshrc
Add the Environment Variable:

Add this line at the end of the file:
export OPENAI_API_KEY="sk-xxxxxx..."
Save and Exit:

Press Ctrl + O to save the file, then Ctrl + X to exit.
Apply the Changes:

Run the following command to apply the changes immediately:
source ~/.bashrc    # For Bash
source ~/.zshrc      # For Zsh
Verification:
To verify that the environment variable is set, you can run the following command in the terminal or command prompt:
echo $OPENAI_API_KEY    # For macOS/Linux
echo %OPENAI_API_KEY%   # For Windows

you need to install python also
to install python you need to do this 
1. Windows:
Step 1: Download Python
Visit the official Python website: https://www.python.org/downloads/
Click the Download Python button. This should automatically give you the latest stable version for Windows.
Step 2: Run the Installer
Once the installer is downloaded, open it.
On the first screen:
Check the box that says "Add Python to PATH" (very important).
Then, click Install Now.
Step 3: Verify Installation
After installation completes, open the Command Prompt (Win + R, type cmd, then press Enter).
Type the following to check if Python is installed and accessible:
python --version
If Python is installed correctly, it will display the Python version number.
Step 4: Install pip (if needed)
pip, the Python package manager, should be installed automatically with Python. To verify, run:
pip --version
If pip is not installed, you can follow this guide to manually install pip


If everything works You can open the app.py File

Have fun With  
**Leo**
