1. set up the project to set up the django on your local machine follow these steps:
   a. clone the repository, using git clone https://github.com/yourusername/your-repo-name.git
2.Set up a virtual environment, use   'python -m venv env command'
 a.activate the virtual environment
3.Install dependencies listed in the requirements.txt use the 'pip freeze requirements.txt'
4.set up the database: run the following commands 'python manage.py makemigrations' or 'python manage.py migrate'
5.create super userpython manage.py createsuperuser
6.run the development server,'python manage.py runserver


 Description of models, serializers, views and urls:
 1. models; Flight model -flight_number: a unique identifier for each flight.-depature: the date and time when the flight departs.
     -arrival: the date and time when the flight arrives. -origin: the airport of depature. - destination: the airport of arrival. -capacity: the total number of seats available
    Passenger model -first_name: the first name of the passenger.- last_name: the last name of the passenger. -email: the passenger's email address(mustbe unique)
    -phone_number: the contact number for the passenger. -flight: a foreign key linking the passenger to a specific flight. A flight can have multiple passengers.
2.Serializers; they help convert complex data types like Querysets and model instances to native python data types that can be rendered into JSON or other content types. -FlightSerializer and -passengerSerializer.
These serializers automatically handle the creation, update and retrieval of 'flight' and 'passenger'  instances using the fields specified in the  'Meta' class.
3.Views handle logic behind the requests and responses. For this project , we are using django rest framework's generic views to simplify CRUD operations -FlightListcreateView : handles GET(list all flights) and POST(create a new flight) requests. - FlightretrieveUpdateDestroyView : Handles GET(retrieve a flight by ID), PUT/PATCH(update a flight by ID),and DELETE (delete a flight byID) requests
 -PassengerListCreateView -handles GET (lists all passengers) and POST (create a new passenger) requests. -PassengeretrieveUpdatedestroyView : handles GET (retrieve a passenger by ID), PUT/PATCH (Update a passenger by id), and DELETE (delete a passenger by ID) requests.    
