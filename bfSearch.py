from collections import deque


def search(name, graph):
    search_queue = deque()  # Queue peoples for search.
    search_queue += graph[name]  # Add person to queue.
    searched = []  # Array fro checked peoples.

    while search_queue:
        person = search_queue.popleft()

        if not person in searched:  # If not checked earlier.
            if person_is_seller(person):  # Seller?
                print(person + " - is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # Add to "searched" and try again.
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

search("you", graph)
