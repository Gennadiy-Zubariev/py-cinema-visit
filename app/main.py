from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaner: Cleaner,
    movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar().sell_product(customer, customer.food)
    CinemaHall(hall_number).moovie_session(movie, customers, cleaner)
