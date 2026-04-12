README File 
IS2209 Group Project: Our Random dog generator
We used: Flask, PostgreSQL, Dog API, Docker, GitHub, Render.

For our IS2209 group project, we created a web application that fetches random dog images from an external Dog API. Users can save their favourite dogs, which are stored in a Supabase PostgreSQL database. We have applied Agile, DevOps, and collaborative software development principles.

Deployment URL:
Our web application shows a random dog image with buttons for the options of "Save Dog" and "Load Another”. Dogs that have been saved appear in the saved Dogs section below.

Table of Contents:
Features
Tools and technologies 
Running the project 
Application settings
How the app works
CI/CD Pipeline
Architecture Overview
Team
External Sources

Features:
Get a random dog image from the Dog API.
Save and retrieve your favourite dogs from a PostgreSQL database, we used Supabase.
You can browse through your saved dogs.
There are health checks and status diagnostics endpoints.
Graceful error handling with retry/back-off when upstream API is unavailable. 
There is structured logging with request IDs and timing.


Tools and technologies :
We used Flask (Python) to run our app.
To store the saved dogs we used PostgreSQL (Supabase)
To get the dog images we used a Dog API.
We used DockerFile to package the app.
We used GitHub for version control, collaboration, and storing the project repository.
We used PyCharm as our location to write the code.
Render Deploys and hosts our application so that it can be found online.


Running the project: 
To run our project on your own computer, follow these steps:
Firstly, make sure you have Python(PyCharm) and Docker installed on your computer.
Download the project from GitHub by cloning the repository:
( git clone https://github.com/eabhacurran/Semester2IS209.git cd Semester2IS209 )
Create a .env file using the .env.example file as a template and fill in your own database and API details.
Install the required dependencies by running pip install -r requirements.txt into your terminal.
Start the app by running flask run in your local terminal. You can then open your browser and go to http://localhost:5000 to see it running.


Application settings: 
To run this app you will need to create a .env file in the project folder. This file stores all of the private information the application needs to run, such as your database password and API details.
We have included a .env.example file in the repository to show you what it should look like. Simply copy it, rename it to (.env) and fill in your own details.
Never upload your .env file to GitHub as it can include private information. It is already included in the .gitignore file so it can't be shared accidentally.




Our team: 
Eabha Curran: Coordinated the project while managing technical setup tasks. E.g. linking team members to the GitHub repository and handling deployment using Render.  (GitHub@eabhacurran)

Niamh 	McNabola: Focused on configuration and the development environment as she worked with Docker and managing project dependencies, ensuring consistency across systems. (  GitHub@niamhmcnabola )

Grace Nagle: Contributed through backend support and testing. Making the kanban board and README File ( GitHub@124430654-ctrl )	

Samio mainly focused on frontend development, including the CSS layout, responsiveness and UI improvements to enhance the usability and appearance of our application.( GitHub@123437232-sami ) 
 
Each team member contributed to pushing and pulling requests, collaboration and supporting each other throughout development of our application.  We worked together in lab sessions with help from our tutors and met up frequently 












