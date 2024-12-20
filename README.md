# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/little-lemon-django.git
cd little-lemon-django
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & frameworks
```bash
# Django
pipenv install django

# Frameworks
pipenv install mysqlclient
pipenv install djangorestframework
pipenv install djoser
```

## Connect to MySQL
```bash
mysql -u root -p
create database reservations;

create user 'adminlittlelemon'@'localhost' identified by 'admin123$%^';
grant all on *.* to 'adminlittlelemon'@'localhost';
flush privileges;

exit
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Account required
```bash
Django
  Admin
    admin
    adminuser123$%^

  Customer
    johndoe
    johndoeuser123$%^

MySQL
  adminlittlelemon
  admin123$%^
```

## Deactivate virtual environment
```bash
exit
```

# Preview project
<table align='center'>
  <tr align='center'>
    <td>Home</td>
    <td>About</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-1.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-2.png' />
    </td>
  </tr>
</table>

<table align='center'>
  <tr align='center'>
    <td>Menu</td>
    <td>Menu item</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-3.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-4.png' />
    </td>
  </tr>
</table>

<table align='center'>
  <tr align='center'>
    <td>Before Booking</td>
    <td>After Booking</td>
    <td>All Reservations</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-5.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-6.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/little-lemon-django/blob/main/little-lemon-django/little-lemon-django-pic-7.png' />
    </td>
  </tr>
</table>
