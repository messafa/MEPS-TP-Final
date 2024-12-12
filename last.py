import numpy as np
import matplotlib.pyplot as plt

class Station:
    def __init__(self, num_servers, mu):
        self.num_servers = num_servers   # Number of servers in the station
        self.mu = mu                     # Service rate
        self.busy_servers = 0            # Number of busy servers
        self.queue = []                  # Queue of waiting customers
    
    def service_time(self):
        # Generates an exponentially distributed service time
        return np.random.exponential(1 / self.mu)
    
    def add_client(self, current_time):
        # A client arrives and either starts service or waits in queue
        if self.busy_servers < self.num_servers:
            self.busy_servers += 1
            return current_time + self.service_time()
        else:
            self.queue.append(current_time)
            return None  # Client is waiting in the queue

    def release_client(self, current_time):
        # Releases a server and serves the next client from the queue if any
        if self.queue:
            next_client_time = self.queue.pop(0)
            self.busy_servers += 1
            return current_time + self.service_time()
        else:
            self.busy_servers -= 1
            return None

class MMSSimulation:
    def __init__(self, num_stations, lambd, mu_list, servers_list, num_clients, language):
        self.num_stations = num_stations  # Number of stations
        self.lambd = lambd                # Arrival rate (clients per unit of time)
        self.mu_list = mu_list            # List of service rates for each station
        self.servers_list = servers_list  # List of servers for each station
        self.num_clients = num_clients    # Number of clients to simulate
        self.language = language          # Selected language for messages
        
        self.stations = [Station(servers_list[i], mu_list[i]) for i in range(num_stations)]
        self.arrival_times = []           # Arrival times of clients
        self.departure_times = []         # Departure times of clients
        self.wait_times = []              # Waiting times of clients
        self.system_times = []            # Total time spent in the system for each client

    def run(self):
        current_time = 0
        for i in range(self.num_clients):
            # Generate an exponentially distributed inter-arrival time
            inter_arrival_time = np.random.exponential(1 / self.lambd)
            arrival_time = current_time + inter_arrival_time
            self.arrival_times.append(arrival_time)
            
            # The client visits all stations in order
            client_departure_time = arrival_time
            for station in self.stations:
                client_departure_time = station.add_client(client_departure_time)
                while client_departure_time is None:  # Waiting in the queue
                    client_departure_time = station.release_client(current_time)
                    current_time += 1  # Move time forward
            
            self.departure_times.append(client_departure_time)
            self.wait_times.append(client_departure_time - arrival_time)
            self.system_times.append(client_departure_time - arrival_time)
        
        # Calculate average metrics
        L = len(self.arrival_times) / current_time  # Average number of customers in the system
        W = np.mean(self.wait_times)                # Average waiting time in the system
        
        return L, W

    def print_results(self, L, W):
        # Messages in different languages
        messages = {
            'en': {
                'L': f"Average number of customers L in the system: {L:.2f}",
                'W': f"Average waiting time W in the system: {W:.2f} units of time",
                'plot_title': "Arrival and Departure Times of Clients in the System"
            },
            'fr': {
                'L': f"Nombre moyen de clients L dans le système: {L:.2f}",
                'W': f"Temps d'attente moyen W dans le système: {W:.2f} unités de temps",
                'plot_title': "Temps d'arrivée et de départ des clients dans le système"
            },
            'ar': {
                'L': f"متوسط عدد العملاء L في النظام: {L:.2f}",
                'W': f"متوسط وقت الانتظار W في النظام: {W:.2f} وحدة زمنية",
                'plot_title': "أوقات وصول العملاء ومغادرتهم من النظام"
            }
        }
        
        # Print results in selected language
        print(messages[self.language]['L'])
        print(messages[self.language]['W'])
        
        # Plot results with appropriate title in selected language
        plt.figure(figsize=(10, 6))
        plt.plot(self.departure_times, label="Departure times of clients", color="b")
        plt.plot(self.arrival_times, label="Arrival times of clients", color="r", linestyle="--")
        plt.xlabel("Client")
        plt.ylabel("Time")
        plt.legend()
        plt.title(messages[self.language]['plot_title'])
        plt.show()

def choose_language():
    print("Choose your language / Choisissez votre langue :")
    print("1. English")
    print("2. Français")
    # print("3. العربية")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'fr'
    # elif choice == '3':
    #     return 'ar'
    else:
        print("Invalid choice. Defaulting to English.")
        return 'en'

def main():
    # Language selection
    language = choose_language()
    
    # Simulation parameters
    num_stations = 3  # Number of stations
    lambd = 2         # Arrival rate (clients per unit of time)
    mu_list = [3, 2, 1]   # Service rates for each station
    servers_list = [2, 2, 1]  # Number of servers for each station
    num_clients = 10000  # Number of clients to simulate

    # Create and run the simulation
    sim = MMSSimulation(num_stations, lambd, mu_list, servers_list, num_clients, language)
    L, W = sim.run()

    # Print results and plot
    sim.print_results(L, W)

if __name__ == "__main__":
    main()