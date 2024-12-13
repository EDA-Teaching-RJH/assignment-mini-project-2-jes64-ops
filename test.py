import pytest
from Mangement import Customer, Order

def test_customer():
    customer = Customer("bob", "jesseofnaof@gmail.com")
#testing string from class Customer
    assert customer.name == "bob"
    assert customer.email == "jesseofnaof@gmail.com"
def test_customer_invalid():
    with pytest.raises(ValueError, match=r"invalid email"):  # match the exact error message which matches error response
        Customer("bob", "invalid email")

def test_order():
    order = Order()
 #testing string from class Order 
    assert order.name == "Jesse Sedzro"
    assert order.price == 5.50
    assert order.num_tickets == 10
    assert order.artist == "addel"
    assert order.ticket_id == 123

def test_order_invalid():
    with pytest.raises(ValueError, match=r"invalid artist"):# if addel is not in artist list it will raise a valueerror which match the error response 
        Order("Jesse Sedzro", "jesseofnaof@gmail.com", 5.50, 10, "addel", 123)
