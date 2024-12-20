# LittleLemon Restaurant Web Application

## Table of Contents
- [Installation Guide](#installation-guide)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Access Credentials](#access-credentials)
- [Project Preview](#project-preview)

## Installation Guide

### 1. Clone Repository
```bash
git init
git clone https://github.com/AlejandroLeonDev/LittleLemonn_AppWeb.git
cd little-lemon-django
```

### 2. Virtual Environment Setup
```bash
# Install pipenv
pip3 install pipenv

# Create and activate virtual environment
pipenv --python 3.10
pipenv shell
```

### 3. Dependencies Installation
```bash
# Core Framework
pipenv install django

# Additional Dependencies
pipenv install mysqlclient
pipenv install djangorestframework
pipenv install djoser
```

## Database Setup

### MySQL Configuration
```bash
mysql -u admin_littlelemon -p
create database reservations;

create user 'admin_littlelemon'@'localhost' identified by 'Admin@123456';
grant all on *.* to 'admin_littlelemon'@'localhost';
flush privileges;

exit
```

## Running the Application

### Initialize and Start Server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Access Credentials

### Django Accounts
```plaintext
Administrator:
  Username: admin_django
  Password: Admin@django123

Customer:
  Username: customer_user
  Password: Customer@123
```

### MySQL Access
```plaintext
Username: admin_littlelemon
Password: Admin@123456
```

### Closing Environment
```bash
exit
```

## Project Preview

### Home and About Pages
<table align='center'>
  <tr align='center'>
    <td>Home</td>
    <td>About</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen1.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen2.png' />
    </td>
  </tr>
</table>

### Menu Interface
<table align='center'>
  <tr align='center'>
    <td>Menu</td>
    <td>Menu item</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen3.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen4.png' />
    </td>
  </tr>
</table>

### Reservation System
<table align='center'>
  <tr align='center'>
    <td>Before Booking</td>
    <td>After Booking</td>
    <td>All Reservations</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen5.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen6.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon_Imagen7.png' />
    </td>
  </tr>
</table>