# E-Health-Care

The web app is designed to reduce dependence on doctors, assist underserved individuals with basic medical checkups, and help people avoid unnecessary medical expenses. This project is built with Django, machine learning algorithms, and deep learning (ANN and CNN).

## Overview

In many regions, particularly in Nepal, there is a significant shortage of doctors. Many people lack access to proper medical checkups, and numerous cases lead to severe outcomes due to a lack of timely medical intervention. This app addresses these issues by providing an accessible solution for basic medical checkups.

## Demo

![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/Ehealthcare.png)
![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/screenshot/EhealthCare1.png)

## Application

- Reduce dependence on doctors.
- Assist underserved individuals with essential medical checkups.
- Minimize unnecessary medical expenses.
- Promote technology’s role in healthcare.

## Models

The project includes several models for disease prediction:

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

- **Python (3.7 or higher)**
- **Django**
- **JavaScript**
- **Pandas**
- **NumPy**
- **HTML**
- **CSS**

## Installation

This project requires Python 3.7 or higher. If Python is not installed, download it [here](https://www.python.org/downloads/).

### Step 1: Install Dependencies with UV

The project uses UV for Python dependency management, which allows for quick and efficient package resolution. Install UV by following instructions on their [official site](https://astral.sh/blog/uv).

1. Install dependencies using UV:
   Linux:-
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Windows:-
   ```bash
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Run initial database migrations:
   ```bash
   uv run python manage.py migrate
   ```

3. Create a superuser for accessing the admin interface:
   ```bash
   uv run python manage.py createsuperuser
   ```

4. Start the development server:
   ```bash
   un run python manage.py runserver
   ```

## User Setup

1. After creating the superuser, log in to the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
2. Create a user group named `ADMIN`.
3. Add new users, setting their `is_active` and `is_staff` to `True`, and assign them to the `ADMIN` group for admin privileges.
4. These users can now log in from the main dashboard with admin access.

## Features

### Patient

- Register and sign in
- Update and edit profile
- View and search specialist doctors
- Predict diseases based on symptoms or x-ray images
- Book, cancel, view, and download appointments
- Provide feedback to the system

### Admin

- View and manage total patients, predictions, doctors, and feedback
- Add, edit, delete, and assign doctors to respective diseases

### Doctor

- Register via provided username and password from the admin
- Manage appointments and view patient records
- Send disease precautions to patients via email

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.
