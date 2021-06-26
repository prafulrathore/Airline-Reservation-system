# Intoduction

```
This project is based on airline reservation system using Django rest framework for booking a flights which provide a REST API to perform CRUD operations on the airline fleet. There is a airline, flight, booking, BookingInfo, Passenger records for storing a data of it.
```

# Technology Stack

```
1. Python 3
2. Django REST Framework
3. sqlite3 Database

```

# Feature

```
1. Booking a flight according to the schedules.
2. Perform the CRUD opertations for airline, flight, booking, BookingInfo, Passenger.
```

```
Create administrator/super user:
```

python manage.py createsuperuser

Note: It will prompt to enter username, email and password one by one. Please remember the username and password,
it will be used to login admin area or to hit an API to scrap/refresh the linkedin profiles.

```


Finally, run the development server:

```

python manage.py runserver

```

` The site will be available at 127.0.0.1:8000. `

`Install the Requirements`:

pip install -r requirements.txt

``

## APIs Details
Base URL for all API endpoints : `http://127.0.0.1:8000/` <br />

ENDPOINT     METHOD     QUERY_PARAMS     DATA
 |ENDPOINT | METHOD | QUERY_PARAS | DATA |
 | -------- | ------ | ----------- | ----|
 | fleet/api/aircraft/list/create/  | GET | jgh| [
    {
        "serial_no": "B71699",
        "manufacturer": "Indigo",
        "total_seats": 100
    },
    {
        "serial_no": "943FEC",
        "manufacturer": "Airbus",
        "total_seats": 100
    },
    {
        "serial_no": "19382E",
        "manufacturer": "Beingo",
        "total_seats": 100
    }
]
Content  | Content Cell

```
url : 
Method : 
Query : 
Data :
