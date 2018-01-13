import os
import json
import facebook

if __name__ == "__main__":
    token = 'EAAEze9xMBS0BAKPw278VczENUG9ZB7zYRnnOZCHcZB1JLb8tkUFcWkinZBF6wn5Tzwb79WZBK1a9ZCbhWsIJsGPw3qJ0zO4gWSvZCyZBJrvHAqSmZCcOTaZA2yLiSrXLmPZACjuxHGf8KXaaZAIBn2E8nnBMZC0MKi1qxrd3ZCkZCBetB5lPzk3SJoHOCZAU0eqJ7DB92lQl4jl7PvtTggZDZD'

    graph = facebook.GraphAPI(token)
    fields = ['link', 'created_time']
    fields = ','.join(fields)
    print(fields)
    page = graph.get_object('wittyfeedIndia/posts', fields=fields)
    a = []
    for posts in page['data']:
        a.append((posts['created_time'], posts['id'], posts['link']))

    a.sort()

    print(json.dumps(page['data'], indent=4))
    print(a)
    print(a[:5])

