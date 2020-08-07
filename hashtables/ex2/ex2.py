#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    connections_table = {}

    route = [None] * length

    for ticket in tickets:
        connections_table[ticket.source] = ticket.destination

    starting_point = connections_table['NONE']

    ticket_pointer = starting_point

    for i in range(0, len(connections_table)):
        # print(i) 
        route[i] = ticket_pointer
        ticket_pointer = connections_table[ticket_pointer]
        
    print(route)
    return route
