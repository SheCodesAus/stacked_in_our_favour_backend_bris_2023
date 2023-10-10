# WinStack - Backend

WinStack is a platform for the SheCodes community to share their successes, acknowledgements and thoughts related to the one-day coding workshops hosted by SheCodes by posting digital sticky notes onto an event board. 

It provides a safe space for collaboration and reflection within the SheCodes program.

## 👥 Target Audience - HEY

WinStack is intended for anyone who is a member of the SheCodes program, be it a mentor, volunteer or cohort member. 

It is also open to the general public who is interested in attending a SheCodes workshops, as long as they create a WinStack account.

## ⭐ Features

### Must Haves

| FEATURE | DESCRIPTION 
| :----- | :----------
| Account Creation | Anyone can create an account
| Log In/ Log Out | Registered users can log in and log out of their accounts. 
| Permissions | Users will have different access and functionalities based on their privileges or permissions.
| Home Page | Landing page for the WinStack application. Open to general public and will display all events in the SheCodes program.
| Organiser |  Mentor or Volunteer hosting SheCodes workshops.
|           |  Can create events where sticky notes can be posted.
|           |  Can edit or delete events they own.
|           |  Can create, edit or delete sticky notes.
| Attendee  |  Member of SheCodes cohort who attended the workshop.
|           |  Can create sticky notes within the event board.
|           |  Can edit or delete sticky notes they own. 
| Superuser |  User with administration privileges
|           |  Can create, edit or delete any events.
|           |  Can create, edit or delete any sticky notes.


### Stretch Goals (Nice to Have)

* Tagging users with a @ symbol if an account exists to be able to mention them in a note
* Filter workshops on dashboard (based on date, topic)
* About page - what are the sticky notes about
* Contact Us page
* Profile page
* Error handling (e.g. if nearing character limit for sticky notes)
* Forgot password on login page

## 🔧 Languages and Frameworks
|        | Tool
| :----- | :----------
| *BACKEND* |  Django Rest Framework (DRF) API
| *DATABASE* | SQLite 
| *DEPLOYMENT* | Fly.io
| *TESTING* | Insomnia

## 📑 Database and API Specification

## 💻 Installing and Execution

### FIRST, One Person In The Group Should:
1. Clone this repo down using `git clone insert_quick_setup_link_here`
2. Create and activate a `venv` as normal
3. Run `pip install -r requirements.txt` to install dependencies
4. Create a Django project with `django-admin startproject <your_app_name>`
5. Check you're happy with the files to stage, using `git status` 
6. Stage each file in turn with `git add <filename_here>`
7. Create the initial commit with `git commit -m "initial commit"`
8. Push to origin/main, using `git push origin main`

### THEN, All Other Group Members Should:
1. Clone the repo down with `git clone insert_quick_setup_link_here`
2. Create and activate a `venv`
3. Install dependencies with `pip install -r requirements.txt`

### Finally:
1. One group member should make a push replacing this readme text with the skeleton of your readme document.
2. All other group members should pull down this change (`git pull origin main`)

> For next steps, take a look back at the "Project Setup" lesson in the DRF content.
>
> Try and get the most minimal possible app deployed ASAP, using the DRF "Deployment" lesson. Even just an endpoint that only returns "Hello world" is a good way to start. Only one person needs to get the deployment set up, and after that other people should be able to merge feature branches into `main` as described on the Thinkific notes.


## Contributors

* [Yara Fe Tuguinay](https://github.com/yara-fe)
* [Emily Martin](link)
* [Pauline Segi](link)
* [Maddy Mengel](link)
* [Claire Delosa](link)


## Acknowledgments


