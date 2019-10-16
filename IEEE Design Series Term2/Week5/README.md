## To install all the required Python library, follow the following steps.

1. open "Terminal" or "Command Prompt"
2. 'cd' to this Week5 folder
e.g.
```bash
cd ~/Desktop/Week5/
```
3. install virtualenv if haven't
```bash
pip install virtualenv
```
4. create a virtual environment named "venv"
```bash
virtualenv venv
```
5. activate your virtual environment
for Mac
```bash
source venv/bin/activate
```
for Windows
```bash
venv/Scripts/activate
```
6. install required library in your virtual environment
```bash
pip install -r requirements.txt
```
7. run python Scripts
```bash
python index.py
```

**To deactivate virutal environment**
for both Mac and Windows
```bash
deactivate
```
