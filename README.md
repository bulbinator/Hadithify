# Hadithify
Link to project: http://hadithify.us-east-1.elasticbeanstalk.com/?

Hadithify is a web-application that generates statements from religious scripture at random from a pool of thousands using the Thaqalayn API: https://github.com/MohammedArab1/ThaqalaynAPI

# Front-end

The front end was created using HTML and CSS with Bootstrap framework and a custom stylesheet, all of which can be seen inside of the "static" and "templates" folder.

# Back-end

The backend was developed with Python using the Flask framework. The file "functions.py" serves the purpose of requesting and filtering data from the API and "app.py" sends the useful data to the front-end to be displayed.
