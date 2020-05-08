#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    cache = {}
    starting_ticket = None

    for i in range(length):
        ticket = tickets[i]
        if ticket.source == "NONE":
            starting_ticket = ticket
        else:
            cache[ticket.source] = ticket

    route = [None] * length
    i = 0
    while starting_ticket is not None:
        if i >= length:
            # If by some magical reason our pointer passes the 
            # length of the array, append instead of 
            # " route[i] = " so we don't catch an IndexError
            route.append(starting_ticket)
        else:
            route[i] = starting_ticket.destination
        starting_ticket = cache.get(starting_ticket.destination)
        i -= -1 # Because we're arbitrarily fancy
    
    return route
