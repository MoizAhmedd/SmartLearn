<p align="center">
  </br>
  <img src="frontend/src/logo.png"/>
</p>

# SmartLearn

## Inspiration
Students in high schools and universities nowadays are very familiar with interactive learning technologies, like iClickers and Kahoot. While they definitely provide a relief from hours of sitting and trying to pay attention, many studies have found that interactive learning “enhances student interest in lecture content and improves student performance on exams” (Wu and Gao, 2011).
While iClickers and Kahoot are mainly limited to in-person classroom experiences, we wanted to provide a platform for teachers to be able to incorporate interactive elements to remote teaching, such as teachers who teach under-served communities. And with the ever-expanding reach of the Internet across the world, and also with the meteoric rise in popularity of e-learning platforms like Coursera and Khan Academy, we felt like something like SmartLearn is sorely needed.

## What it does
SmartLearn is a platform that lets educators livestream lectures to students anywhere in the world, and creates interactive polls to engage the students during the lecture. This also allows instructors to receive immediate feedback about students’ understanding and customize their delivery of the subject accordingly.

## How we built it
We used Django to create the backend, building the authentication system from the ground up, and using Firebase as our database to store much of our data, such as users (Teachers and Students) and all the information on them, courses, livestream IDs and more. We used the SurveyMonkey API to provide polling power, allowing teachers to create surveys within our web app, and then embedding them within our program.

## Challenges we ran into
Our frontend teammates spent a lot of time trying to align divs and center elements (the usual CSS headache), and trying to use Bootstrap to our advantage while also defining SmartLearn’s brand design.

## Accomplishments that we’re proud of
We’re proud of our clean and functional design, and getting to refine our front-end development skills. Although half of us were solely backend developers and the other half frontend, we’re extremely happy that we were able to effectively delegate tasks, work on our own components, and integrate everything together successfully at the end. We didn’t know each other going into Hack the North, and we all had varying skill sets, yet we learned a lot from each other and had a great time doing it.

## What we learned
We all learned a lot; on the back end we learned a ton about Django, how to use it effectively, and what makes it take. We also learned a lot about handling and storing data through Firebase, and it definitely made us appreciate the merits of well-planned code and following good OOP principle.
On the front end we learned a lot about creating well styled documents using Figma to make mock-ups, and HTML, CSS, and JS for the final product.

## What’s next for SmartLearn
We'd love to host SmartLearn on popular social media platforms that have livestreaming (eg: Facebook), so that more individuals can benefit from quality education. We'd also like to include analytics of student answers and feedback from previous lectures; the ability to view analytics would allow instructors to see trends in student learning so that they can refine their teaching for the future. 
