It is a Q&A/Discussion platform Web App built using Django Framework with following functionalities:
Authentication
a.	Here I used Nav bar by which guest user will get the functionality of Login and Signup while Logged In user will see his user id and Logout functionality.
b.	Signup- New user can create his account using his E-mail and password.
c.	Login- Registered user can log in to app using his registered email and password on app.
d.	Logout-Registered user can log out from app and can view the app as guest.

Authorization
a.	Guest user can view questions and their answers but can’t perform any other operation on them.
b.	Registered user can only create the post.
c.	Registered user can only edit or delete their own post.

Question
a.	Registered users can create a question with title, description and tags and Title and Description are validated i.e., they can't be empty.
b.	Questions can be edited / deleted only by the creator from actions.
c.	Questions are listed according to the date of creation in descending order with proper pagination 
d.	Each question is listed with the number of views associated with it which is basically count of how many times a question has been viewed
e.	Search functionality has been provided on Navbar by which users can search results from title and tags of questions.

Answer
a.	Guest user and registered user both can view answers of questions by clicking on them.
b.	Only registered users can answer the questions by clicking on questions.
c.	Answers are listed according to the date of creation in descending order.
d.	Answers can be edited / deleted only by the creator from actions.

