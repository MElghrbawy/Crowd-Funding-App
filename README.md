# Crowd Funding

## Demo

https://user-images.githubusercontent.com/33490779/189488707-358b3082-c8c3-490f-b8cd-16cea292abc0.mp4


## Table of Contents

-  [Demo](#demo)
-  [Description](#description)
-  [Installation](#installation)
-  [Usage](#usage)
-  [Contributors](#contributors)

## Description

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. Crowdfunding is a form of crowd sourcing and alternative finance. In 2015, over US$34 billion was raised worldwide by crowdfunding. The aim of the project: Create a web platform for starting fundraiser projects in Egypt.

## Features

CrowdFunding Web App that allow user to:

-  Signup and login
-  Create and modify his profile data or delete his account
-  Create or Delete funding projects
-  show all projects details
-  Donate, Rate, Report, and Comment other projects

## Installation

```bash
git clone https://github.com/MElghrbawy/Gym-System
cd Crowd-Funding-App
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
touch .env
	DB_NAME = 'crowd_funding'
	DB_PASSWORD = 'password'
	DB_HOST = 'localhost'
	DB_USER = 'root'
psql -U YOUR_POSTGRES_USERNAME -p
	CREATE DATABASE crowd_funding;
python manage.py makemigrations
python manage.py migrate
```

## Usage

```bash
python manage.py runserver
```

## Contributors

<table>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/33490779?v=4" />
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97922599?v=4" />
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97697512?v=4" />
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/MohamedShehata15">Mohamed Shehata</a>
    </td>
      <td>
      <a href="https://github.com/MElghrbawy">Mohamed Elghrbawy</a>
    </td>
     <td>
      <a href="https://github.com/nadareffat98">Nada Reffat</a>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/83234154?v=4" />
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97697351?v=4" />
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97316532?v=4" />
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/khloud44">Khloud Elsaid</a>
    </td>
      <td>
      <a href="https://github.com/shoroukalkalla">Shorouk Alkalla</a>
    </td>
     <td>
      <a href="https://github.com/YaraMohammed98">Yara Mohammed</a>
    </td>
  </tr>
</table>
