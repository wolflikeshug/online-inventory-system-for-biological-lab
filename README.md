# CITS3200-repo

**Contributors**: Daniel Hu (wolflikeshug), Joe Lao (joe-potato), Leyton Hilmer (Leyton-Hilmer), Luke Bowies (Bowles777), Peter Taylor (ptaylo), Simon McGee (RunSeven)

Here is the temp readme file for CITS3200
The first meeting setted at 18:00 26/07/2022.

**Useful Link:**[CITS3200 Homepage](https://teaching.csse.uwa.edu.au/units/CITS3200/index.html)

### NOTE: After installation, if you receive issues about `import fcntl`. Make sure you run 
###    
### pip uninstall gunicorn

## Setup  
Windows:  
  
1.Make sure your terminal is is in the repo's directory (C:\blah\blah\CITS3200-repo).  
2.To create virtual environment, type in terminal:
```bash
python -m venv venv
```
3.To activate virtual environment, type in terminal:
```bash
.\venv\Scripts\activate
```
4.Install requirements with:
```bash
pip install -r requirements.txt
```
5.Run site with:
```bash
python wsgi.py
```

6.Go to [http://localhost:5000/](http://localhost:5000/)
  

Linux/Mac: 
   
Replace 2. command with:
```bash
python3 -m venv venv
```
Replace 3. command with:
```bash
source venv/bin/activate
``` 
  
Let me (Joe) know if you have troubles.  

