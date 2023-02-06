# TaskManager

### ✅&nbsp; Features
1. Add event with these inputs
- task name
- description
- from date to date 
- time duration
- link for website (optional)
2. arrange event in inrease order of its priority which will decide on the basis of time limit
3. Signin / sign up page 
4. Forgot password feature 
5. Can change the password when required
6. send notification through mail or sms
7. payment gateway (buy me a coffee)

### 💻 Tech Stack


### Front-End:
<img alt="HTML5" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>  <img alt="CSS3" src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/> <img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> 
<img alt="BootStrap" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/> 

### Back-End:
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>    

### Data-Base:
<img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?&style=for-the-badge&logo=sqlite&logoColor=white"/> 


### Other:
<img alt="Progressive Web Apps" src="https://img.shields.io/badge/Progressive Web Apps%20-%2300C4CC.svg?&style=for-the-badge&logo=ProgressiveWebApps&logoColor=white"/>

### Project Structure 💁‍♀️
  
```
TaskManager
│   
├───TaskManager                  # Main Project Directory
│       
├───home                       # Project Main App Directory
│   │   
│   └───migrations              # Migrations
│           
├───static          
|   |                           # Static Directory
│   └───| 
│       ├───assets              # Image Files  
|       |
│       ├───css                 # CSS Files  
|       |
|       ├───fonts               # Fonts Used
│       │       
|       ├───JS                  # js Files                      
│       │       
│       ├───favicons            # favicons
│       |    
│       
│         
|           
├───templates                   # Root Template Directory (all html templates)
|
├───db.sqlite3                  # Database  File
|
├───manage.py                   # For running django server
|
├───requirements.txt            # All modules which are used in project

```            

## 🚀 Quick Start :

#### Step 1: Forking the repository :

To work on an open-source project, you will first need to make your copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

Get your own Fork/Copy of repository by clicking `Fork` button right upper corner.<br><br>

#### Step 2: Clone the Forked Repository

After the repository is forked, you can now clone it so that you have a local working copy of the codebase.

To make your local copy of the repository follow the steps:
- Open the Command Prompt
- Type this command:
  
```bash
$ git clone https://github.com/<your-github-username>/pixelvibe
```


#### Step 3: Creating a new branch (IMP)
This is one of the very important step that you should follow to contribute in Open Source. A branch helps to manage the workflow, isolate your code and does not creates a mess. To create a new branch:
  
```bash
$ git branch <name_of_branch>
$ git checkout -b <name_of_branch>
```

Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
```bash
git pull origin main
```

#### Step 4: Setting up Project

##### For Django:
**1. Create a Virtual Environment**

- *Windows*
  ```bash
    py -m venv env
  ````

- *On macOS and Linux:*
  ```bash
    python3 -m venv env
  ```


**2. Activate the Virtual Environment**
  - *On Windows*
    ```bash
    .\env\Scripts\activate
    ```
  - *On macOS and Linux:*
    ```bash
    source env/bin/activate
    ```

**3. Install dependencies using**
```bash
pip install -r requirements.txt
```

**4. Make Migrations**

```bash
  python manage.py makemigrations
  python manage.py migrate
```
**5. Run Server**

```bash
  python manage.py runserver
```
**6. Create admin**

```bash
  python manage.py createsuperuser
```

**5.** Go to ` http://127.0.0.1:8000/` and enjoy the application.
