from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict


def create_data_model():
    """Stores the data for the problem."""
    data = {'time_matrix': [
        [0, 6, 9, 8, 7, 3, 6, 2, 3, 2, 6, 6, 4, 4, 5, 9, 7],
        [6, 0, 8, 3, 2, 6, 8, 4, 8, 8, 13, 7, 5, 8, 12, 10, 14],
        [9, 8, 0, 11, 10, 6, 3, 9, 5, 8, 4, 15, 14, 13, 9, 18, 9],
        [8, 3, 11, 0, 1, 7, 10, 6, 10, 10, 14, 6, 7, 9, 14, 6, 16],
        [7, 2, 10, 1, 0, 6, 9, 4, 8, 9, 13, 4, 6, 8, 12, 8, 14],
        [3, 6, 6, 7, 6, 0, 2, 3, 2, 2, 7, 9, 7, 7, 6, 12, 8],
        [6, 8, 3, 10, 9, 2, 0, 6, 2, 5, 4, 12, 10, 10, 6, 15, 5],
        [2, 4, 9, 6, 4, 3, 6, 0, 4, 4, 8, 5, 4, 3, 7, 8, 10],
        [3, 8, 5, 10, 8, 2, 2, 4, 0, 3, 4, 9, 8, 7, 3, 13, 6],
        [2, 8, 8, 10, 9, 2, 5, 4, 3, 0, 4, 6, 5, 4, 3, 9, 5],
        [6, 13, 4, 14, 13, 7, 4, 8, 4, 4, 0, 10, 9, 8, 4, 13, 4],
        [6, 7, 15, 6, 4, 9, 12, 5, 9, 6, 10, 0, 1, 3, 7, 3, 10],
        [4, 5, 14, 7, 6, 7, 10, 4, 8, 5, 9, 1, 0, 2, 6, 4, 8],
        [4, 8, 13, 9, 8, 7, 10, 3, 7, 4, 8, 3, 2, 0, 4, 5, 6],
        [5, 12, 9, 14, 12, 6, 6, 7, 3, 3, 4, 7, 6, 4, 0, 9, 2],
        [9, 10, 18, 6, 8, 12, 15, 8, 13, 9, 13, 3, 4, 5, 9, 0, 9],
        [7, 14, 9, 16, 14, 8, 5, 10, 6, 5, 4, 10, 8, 6, 2, 9, 0],
    ],
    'time_windows':[
        (0, 5),  # depot
        (7, 12),  # 1
        (10, 15),  # 2
        (16, 18),  # 3
        (10, 13),  # 4
        (0, 5),  # 5
        (5, 10),  # 6
        (0, 4),  # 7
        (5, 10),  # 8
        (0, 3),  # 9
        (10, 16),  # 10
        (10, 15),  # 11
        (0, 5),  # 12
        (5, 10),  # 13
        (7, 8),  # 14
        (10, 15),  # 15
        (11, 15),  # 16
    ],
    'locations': [
        (456, 320),  # location 0 - the depot
         (228, 0),  # location 1
         (912, 0),  # location 2
         (0, 80),  # location 3
         (114, 80),  # location 4
         (570, 160),  # location 5
         (798, 160),  # location 6
         (342, 240),  # location 7
         (684, 240),  # location 8
         (570, 400),  # location 9
         (912, 400),  # location 10
         (114, 480),  # location 11
         (228, 480),  # location 12
         (342, 560),  # location 13
         (684, 560),  # location 14
         (0, 640),  # location 15
         (798, 640)  # location 16
     ],
    'demands': [0, 1, 1, 3, 6, 3, 6, 8, 8, 1, 2, 1, 2, 6, 6, 8, 8], 'vehicle_capacities': [12, 14, 16, 18],
        'num_vehicles': 4, 'depot': 0,"dropped":[],"route": [],"solution": {}}
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console"""
    dropped_nodes = 'Dropped nodes:'
    for node in range(routing.Size()):
        if routing.IsStart(node) or routing.IsEnd(node):
            continue
        if solution.Value(routing.NextVar(node)) == node:
            dropped_nodes += ' {}'.format(manager.IndexToNode(node))
            data["dropped"].append(node)
    print(dropped_nodes)
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        nodes_in_route = []
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_load = 0
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            node_index = manager.IndexToNode(index)
            nodes_in_route.append(node_index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Time({1},{2}) Load({3})-> '.format(node_index, solution.Min(time_var), solution.Max(time_var), route_load)
            data["solution"][node_index] = (solution.Min(time_var), solution.Max(time_var))
            print("route_load",route_load)
            index = solution.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        data["route"].append(nodes_in_route)

        plan_output += '{0} Time({1},{2}) Load({3})\n'.format(manager.IndexToNode(index), solution.Min(time_var), solution.Max(time_var), route_load)
        plan_output += 'Time of the route: {}min\n'.format(solution.Min(time_var))
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_time += solution.Min(time_var)
        total_load += route_load
    print('Total time of all routes: {}min'.format(total_time))
    print('Total load of all routes: {}'.format(total_load))

def plot_solution(data):
    """plot solution ."""

    di_graph = nx.DiGraph()
    fig, ax = plt.subplots(figsize=(20, 10))
    # index 0 is for depot & dropped node
    vehicle_color_map = ['black','blue', 'orange', 'yellow', 'green']
    node_color_dict = OrderedDict()
    vehicle_edges_dict = OrderedDict()

    # draw dropped nodes
    for idx,dropped_node in enumerate(data['dropped']):
        di_graph.add_node(dropped_node, pos=data['locations'][dropped_node],
                          demand=data['demands'][dropped_node],
                          time_window='time:' + str(data['time_windows'][dropped_node]),
                          )
        node_color_dict[dropped_node] = vehicle_color_map[0]

    for vehicle_id, vehicle_route in enumerate(data['route']):
        previous_node = 0

        for idx, node in enumerate(vehicle_route):
            # add node with its demand attribute
            di_graph.add_node(node, pos=data['locations'][node],
                              demand=data['demands'][node],
                              time_window='time:' + str(data['time_windows'][node]),
                              solution='sol:' + str(data['solution'][node]))
            edge = (previous_node, node)
            di_graph.add_edge(previous_node,node,color = vehicle_color_map[vehicle_id+1], loaded=data['demands'][previous_node])
            node_color_dict[node] = vehicle_color_map[vehicle_id+1]
            previous_node = node

        # back to depot
        di_graph.add_edge(previous_node, 0, color = vehicle_color_map[vehicle_id+1],loaded=data['demands'][previous_node])


    # set depot color
    node_color_dict[0] = vehicle_color_map[0]
    node_color_list = list(node_color_dict.values())

    # draw nodes
    pos_nodes = nx.get_node_attributes(di_graph, 'pos')
    nodes = nx.draw_networkx_nodes(di_graph, pos_nodes, node_size=1500, node_color='white',node_shape='s')
    nodes.set_edgecolor(node_color_list)

    # draw edges for each vehicle
    edges_color = nx.get_edge_attributes(di_graph, 'color')
    nx.draw_networkx_edges(di_graph, pos_nodes,width=3, alpha=0.9, arrowstyle='simple',
                           arrowsize=20, node_size=1500,
                           arrows=True, edge_color=edges_color.values())

    # draw labels for nodes (name and attributes)
    node_time_window_labels = nx.get_node_attributes(di_graph, 'time_window')
    node_solution_labels = nx.get_node_attributes(di_graph, 'solution')
    edges_loaded_labels = nx.get_edge_attributes(di_graph, 'loaded')

    #clear time from depot
    node_time_window_labels[0] = ''
    node_solution_labels[0] = ''

    pos_time_window_labels = {}
    for node, coords in pos_nodes.items():
        pos_time_window_labels[node] = (coords[0], coords[1] - 50)

    pos_solution_labels = {}
    for node, coords in pos_nodes.items():
        pos_solution_labels[node] = (coords[0], coords[1] - 35)

    nx.draw_networkx_labels(di_graph, pos_nodes, font_size=12, cmap=node_color_list, font_weight="bold")
    nx.draw_networkx_labels(di_graph, pos_time_window_labels, font_size=10, font_color='b', labels=node_time_window_labels)
    nx.draw_networkx_labels(di_graph, pos_solution_labels, font_size=10, font_color='b', labels=node_solution_labels)

    nx.draw_networkx_edge_labels(di_graph, pos_nodes,font_size=10,edge_labels=edges_loaded_labels )

    ax.axis('off')
    
    plt.gca().invert_yaxis()
    plt.show()  # display

def main():
    """Solve the CVRP problem"""
    # Instantiate the data problem
    data = create_data_model()

    # Create the routing Model.
    manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']), data['num_vehicles'], data['depot'])

    parameters = pywrapcp.DefaultRoutingModelParameters()
    #parameters.solver_parameters.trace_propagation = True
    #parameters.solver_parameters.trace_search = True

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager,parameters)

    # Create and register a transit callback.
    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['time_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterPositiveUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    penelty = 1000
    for node in range(1, len(data['time_matrix'])):
        routing.AddDisjunction([manager.NodeToIndex(node)], penelty)

    # Add Time Windows constraint.
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        0,  # allow waiting time
        30,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == 0:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    # Add time window constraints for each vehicle start node.
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(data['time_windows'][0][0],
                                                data['time_windows'][0][1])

    # Instantiate route start and end times to produce feasible times.
    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))


    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH

    #search_parameters.solution_limit = 5
    search_parameters.time_limit.seconds = 10
    search_parameters.log_search = True


    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    ov = solution.ObjectiveValue()

    print(routing.DebugOutputAssignment(solution, 'Any'))


    print(ov)


    if solution:
        print_solution(data, manager, routing, solution)
        plot_solution(data)


if __name__ == '__main__':
    main()
