#-------------------------------------------------------------------------------
# Name:        loadbalancer
# Purpose:
#
# Author:      pc
#
# Created:     13/04/2020
# Copyright:   (c) pc 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

#Begin Part 1
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections['connection_id'] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections['connection_id']

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total+=load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#End of part 1

#Begin Part 2

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        self.ensure_availability()
        server = random.choice(self.servers)
        self.connections['connection_id'] = server
        server.add_connection(connection_id)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        server = self.connections['connection_id']
        server.close_connection(connection_id )
        del self.connections['connection_id']

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        result = 0

        sum_of_all = []
        for server in self.servers:
            sum_per_server = 0
            for id_con, load in server.connections.items():
                sum_per_server+= load
            sum_of_all.append(sum_per_server)
        for load in sum_of_all:
            result+=load
        return result/len(sum_of_all)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >= 0.5:
             self.servers.append(Server())


    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

#End of part 2




