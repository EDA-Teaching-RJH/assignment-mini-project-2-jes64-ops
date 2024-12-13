from artist_data import artists
import re
class Customer:# here a class called customer is given 
    def __init__(self, name, email):
        if not name:
            raise ValueError("Invalid name") # it will raise value error if name is not met
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email): # if email dont match pattern it will raise an error
            raise ValueError("invalid email")
        self.name = name
        self.email = email
    def __str__(self): 
        return f"Name: {self.name}\nEmail: {self.email}\n" #name and email here is returned as a string 

class Order(Customer):
    def __init__(self, name, email, price, num_tickets, artist, ticket_id): # class created
        super().__init__(name, email) # super class from inherited class customer
        if artist not in artists:
            raise ValueError("invalid artist") # if artist is not in artists from thelist in artist_data appliaction it will raise value error
        self.price = price
        self.artist = artist
        self.num_tickets = num_tickets
        self.ticket_id = ticket_id

    def __str__(self):
        return f"Artist: {self.artist}\n Tickets: {self.num_tickets}\n Price: £{self.price}\nTicket ID: {self.ticket_id}" # artist , tickets , price, ticket id is returned as a string. 