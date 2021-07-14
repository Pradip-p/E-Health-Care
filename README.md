# E-Health-Care
The web app which is used to remove the dependencies on the doctors, to help out the poor and helpless people with the normal medical checkup and to help people avoid paying huge amount to doctor unnecessarily. This project is made with Django, machine learning algorithms and deep learning (ANN and CNN).
## Overview
In todays time we see a lot of the shortage of the doctors in the world especially in NEPAL.A lot of people are suffering a lot without the help of the proper medical checkup.Also most of the cases many cases arise leading to dealth due to lack of timely medical checkup
So to cope up with all of those problems this app is designed which would prove its benefits upto much extent.
## Demo
![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/Ehealthcare.png)
![](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/EhealthCare1.png)
## Application
* To remove the dependencies on the doctors.
* To help out the poor and helpless people with the normal medical checkup.
* To help people avoid paying huge amount to the doctors unnecessarily.
* To extend the role of the technology in the medical field.

<hr>
<h3> Down below are the names of the various model files used:</h3>
<ul>
<li><p><b> pneumonia model = pickle_model_pneumonia.pkl</b></p></li>
<li><p><b>Diabetes model = pickle_model_diabetes.pkl</b></p></li>
<li><p><b>Heart model = pickle_model_heart.pkl</b></p></li>
<li><p><b>Disease model = pickle_model_disease.pkl</b></p></li>
</ul>
<hr>

<h3> Kernals used for training deep learning model </h3>
<ul>
<li><p><b>Kernal for Malaria model :</b>https://www.kaggle.com/shobhit18th/malaria-cell</p></li>

<li><p><b>Kernal for Pneumonia model :</b>https://www.kaggle.com/shobhit18th/keras-nn-x-ray-predict-pneumonia-86-54</p></li>
<hr>
</ul>

<h3> Details of various datasets used for model development : </h3>
<ul>
<li><p><b>Heart</b> : heart.csv [In the repository]</p></li>
<li><p><b>Diabetes</b> : diabetes.csv [In the repository]</p></li>
<li><p><b>Disease</b> : disease.csv [In the repository]</p></li>
<li><p><b>Pneumonia: </b> https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia </p></li>
</ul>

<hr>

<h3> Tools used for project development: </h3>
<ul>
<li><p><b>Python ( 3.7 version)</b></p></li>
<li><p><b>Django</b></p></li>
<li><p><b>Javascript</b></p></li>
<li><p><b>Pandas</b></p></li>
<li><p><b>Numpy</b></p></li>
<li><p><b>HTML</b></p></li>
<li><p><b>CSS</b></p></li>
</ul>

## Installation
The Code is written in Python 3.7.0. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
Use the  [docker](https://docs.docker.com/docker-for-windows/install/) to install requirements file.

<ul>
<li><p><b>python manage.py migrate</b></p></li>
<li><p><b>python manage.py makemigrations</b></p></li>
<li><p><b>manage.py migrate</b></p></li>
<li><p><b>python manage.py createsuperuser</b></p></li>
<li><p><b>python manage.py runserver</b></p></li>
</ul>

# Features

## Patient

<ul>
<li><p><b>Sign up/ sign In</b></p></li>
<li><p><b>Can update and edit profile</b></p></li>
<li><p><b>Can view list of Specialist doctor</b></p></li>
<li><p><b>Can search specialist doctor by name, address and speciality<b><p></li>
<li><p><b>Can search doctor by disease name and doctor</b></p></li>
<li><p><b>Can predict Disease by entering provided symptoms</b></p></li>
<li><p><b>Can predict heart problem by entering parameters</b></p></li>
<li><p><b>Can predict pneumonia by uploading x-ray images</b></p></li>
<li><p><b>Can predict diabetes problem by entering </b></p></li>
<li><p><b>Suggest doctor after predicting any disease if doctor is available<b></p></li>
<li><p><b>Patient can take appointment</b></p></li>
<li><p><b>Patient can cancel, view and download appointment details</b></p></li>
<li><p><b>Patient can give feedback to system</b></p></li>
</ul>

## Admin
<ul>
<li><p><b>Can view total patients, predictions, Doctors and feedback from patient</b></p></li>
<li><p><b>Can view new patient who predicts disease</b></p></li>
<li><p><b>Sign In and logout</b></p></li>
<li><p><b>Can add, edit and delete and search all doctor</b></p></li>
<li><p><b>Assign doctor to respective disease </b></p></li>
</ul>

## Doctor

<ul>
<li><p><b>Sign up through provided username and password from admin</b></p></li>
<li><p><b>View the list of all patients who predicts disease which he was assign to take charge of it(Disease)</b></p></li>
<li><p><b>Can add, edit and delete the appointment </b></p></li>
<li><p><b>Can view booked appointment</b></p></li>
<li><p><b>Can send disease precaution to patient through email</b></p></li>
</ul>




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
