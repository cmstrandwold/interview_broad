import requests


def main():
    api_key = '8beb0d894fe64fc0a7b68c61fcc89a92'

    # Question 1 error checking and running
    routes_url = f'https://api-v3.mbta.com/routes?filter[type]=0,1&api_key={api_key}&include=line'
    route_ids = get_subway(routes_url)

    # Question 2:
    stops, cross_stops = most_least_stops(route_ids, api_key)
    print("")

    # Question 3:
    print(get_stops(stops, cross_stops))

    # Error checking:
    # Checking spelling errors/ invalid stops
    # print(find_route(stops, cross_stops, "Harvard Avene", "Northeastern University"))
    # print(find_route(stops, cross_stops, "Harvard Avenue", "Northeastern"))
    # print(find_route(stops, cross_stops, "Harvard Avenue", "Northeastern University"))
    # Checking route with more than one change is not found
    # print(find_route(stops, cross_stops, "Central", "Aquarium"))
    # Checking valid inputs, with both same line and transfers
    # print(find_route(stops, cross_stops, "Davis", "Kendall/MIT"))
    # print(find_route(stops, cross_stops, "Ashmont", "Arlington"))
    # print(find_route(stops, cross_stops, "Riverway", "Wellington"))
    


# Question 1: Getting subway data and printing names of lines
def get_subway(url):
    """
    Getting subway data and printing names of lines
    :param url: API url to get filtered subway data
    :return: List of dictionaries containing the subway lines data
    """
    try:
        r = requests.get(url).json()['data']
        result = ''
        route_ids = {}
        for line in r:
            if len(result) == 0:
                result += line.get('attributes').get('long_name')
            else:
                result += f', {line.get("attributes").get("long_name")}'
            route_ids[line.get("id")] = line.get("attributes").get("long_name")
        print(f'Routes: {result}')
        return route_ids
    except requests.exceptions.RequestException:
        print(f'There was an issue with the API request, please check your URL or parameters: {url}')
    except KeyError:
        print(f'There was an issue with the API request, please check your URL or parameters: {url}')


# Question 2
def most_least_stops(route_ids, api_key):
    """
    Getting stop data and printing routes with the most and least stops,
    and printing all stops with 2 or more connecting routes
    :param api_key: API key for accessing MBTA data
    :param route_ids: dictionary associating route ids and route long names
    :return:
        stops: dictionary containing all stops and their respective lines
        cross_stops: dictionary containing only the stops with 2 or more lines
    """
    try:
        routes = {}
        stops = {}
        for id in route_ids.keys():
            current_stops = []
            stops_url = f'https://api-v3.mbta.com/stops?filter[route]={id}&include=route&api_key={api_key}'
            r = requests.get(stops_url).json()['data']
            for line in r:
                name = line.get('attributes').get('name')
                current_stops.append(name)
                stops.setdefault(name, [])
                stops.get(name).append(route_ids[id])

            routes[id] = len(current_stops)

        # Printing and processing data
        max_stops = max(routes, key=routes.get)
        print(f'\nRoute with most stops: {route_ids[max_stops]}, {routes[max_stops]}')
        min_stops = min(routes, key=routes.get)
        print(f'Route with least stops: {route_ids[min_stops]}, {routes[min_stops]}')
        pairs = stops.items()
        cross_stops = {key: value for key, value in pairs if len(value) > 1}
        print('\nStops that connect two or more subway routes:')
        for stop in cross_stops:
            result = ''
            for route in cross_stops[stop]:
                if len(result) == 0:
                    result += route
                else:
                    result += f', {route}'
            print(f'{stop}: {result}')

        return stops, cross_stops
    except requests.exceptions.RequestException:
        print(f'There was an issue with the API request, please check your URL or parameters')
    except KeyError:
        print(f'There was an issue with the API request, please check your URL or parameters')


# Question 3: Partial solution, only handles up to one line change
def find_route(stops, cross_stops, stop1, stop2):
    """
    Finds a possible route between two stops with up to one line change
    :param stops: dictionary containing all stops and the routes that go through them
    :param cross_stops: dictionary containing only stops with 2 or more routes
    :param stop1: stop 1 name
    :param stop2: stop 2 name
    :return: string of output for route between stops
    """
    both_exist, err = stop_exists(stop1, stop2, stops)
    if both_exist:
        for route1 in stops.get(stop1):
            for route2 in stops.get(stop2):
                if route1 == route2:
                    return f'{stop1} -> {stop2}: {route1}'
                elif find_cross(route1, route2, cross_stops):
                    return f'{stop1} -> {stop2}: {route1}, {route2}'
        return f'{stop1} -> {stop2}: No route, may need more than one line change'
    else:
        return err


def get_stops(stops, cross_stops):
    """
    Prompts the user for input to get two stop names, and then runs find_route with input
    :param stops: dictionary containing all stops and the routes that go through them
    :param cross_stops: dictionary containing only stops with 2 or more routes
    """
    print('Please enter the stop names you wish to find the connection between as prompted'
          ', or enter "Stop" to end the program')
    stop1 = input('Enter the first stop: ')
    if stop1 == "Stop":
        quit()
    stop2 = input('Enter the second stop: ')
    if stop2 == "Stop":
        quit()
    return find_route(stops, cross_stops, stop1, stop2)


def find_cross(route1, route2, cross_stops):
    """
    Finds if two lines share a stop, meaning that they cross
    :param route1: Route 1
    :param route2: Route 2
    :param cross_stops: Dictionary containing all stops that have multiple routes through them
    :return: Boolean value of whether the routes do cross anywhere
    """
    for stop in cross_stops:
        if route1 in cross_stops.get(stop) and route2 in cross_stops.get(stop):
            return True
    return False


def stop_exists(stop1, stop2, stops):
    """
    Error checking method that determines that both of the stops exist, and returns a message if they do not
    :param stop1: Stop 1 name
    :param stop2: Stop 2 name
    :param stops: dictionary containing all stops
    :return: Boolean value and error message string
    """
    if stop1 in stops and stop2 in stops:
        return True, ''
    elif stop1 in stops:
        return False, f'{stop2} was not found, please check again'
    else:
        return False, f'{stop1} was not found, please check again'


if __name__ == '__main__':
    main()
