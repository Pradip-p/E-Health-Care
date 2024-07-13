# E-Health-Care

The web app is designed to reduce dependence on doctors, assist poor and helpless individuals with basic medical checkups, and help people avoid unnecessary medical expenses. This project is built with Django, machine learning algorithms, and deep learning (ANN and CNN).

## Overview

In today's world, there is a significant shortage of doctors, especially in Nepal. Many people suffer without proper medical checkups, and numerous cases lead to death due to the lack of timely medical intervention. This app aims to address these issues by providing an accessible solution for medical checkups, thus offering substantial benefits.

## Demo

![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/Ehealthcare.png)
![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/EhealthCare1.png)

## Application

- Remove dependence on doctors.
- Assist poor and helpless individuals with basic medical checkups.
- Help people avoid unnecessary medical expenses.
- Extend the role of technology in the medical field.

## Models

Various models used in the project:

- **Pneumonia model**: `pickle_model_pneumonia.pkl`
- **Diabetes model**: `pickle_model_diabetes.pkl`
- **Heart model**: `pickle_model_heart.pkl`
- **Disease model**: `pickle_model_disease.pkl`

## Kernels Used for Training Deep Learning Models

- **Kaggle Kernel for Malaria model**: [Link](https://www.kaggle.com/shobhit18th/malaria-cell)
- **Kaggle Kernel for Pneumonia model**: [Link](https://www.kaggle.com/shobhit18th/keras-nn-x-ray-predict-pneumonia-86-54)

## Datasets Used for Model Development

- **Heart**: `heart.csv` [In the repository]
- **Diabetes**: `diabetes.csv` [In the repository]
- **Disease**: `disease.csv` [In the repository]
- **Pneumonia**: [Link](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

## Tools Used for Project Development

- **Python (3.7 version)**
- **Django**
- **JavaScript**
- **Pandas**
- **NumPy**
- **HTML**
- **CSS**

## Installation

The code is written in Python 3.7.0. If you don't have Python installed, you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python, you can upgrade using the pip package, ensuring you have the latest version of pip.

1. `python manage.py migrate`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`

## Features

### Patient

- Sign up/Sign In
- Update and edit profile
- View list of specialist doctors
- Search specialist doctors by name, address, and specialty
- Search doctor by disease name and doctor
- Predict disease by entering provided symptoms
- Predict heart problem by entering parameters
- Predict pneumonia by uploading x-ray images
- Predict diabetes problem by entering parameters
- Suggest doctor after predicting any disease if a doctor is available
- Take appointments
- Cancel, view, and download appointment details
- Give feedback to the system

### Admin

- View total patients, predictions, doctors, and feedback from patients
- View new patients who predict disease
- Sign In and logout
- Add, edit, delete, and search all doctors
- Assign doctor to respective disease

### Doctor

- Sign up through provided username and password from admin
- View the list of all patients who predict diseases which they are assigned to take charge of
- Add, edit, and delete appointments
- View booked appointments
- Send disease precautions to patients through email

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
