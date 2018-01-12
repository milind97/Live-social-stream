import os
import json
import facebook

if __name__ == "__main__":
    token = 'EAAEze9xMBS0BAJKadaCyf7bxetqQRUMVUJgwIQyx7tIPepY89ZBusNthGedHMha3HfnAPnPpzQkWFrYULkmShPnlUNWrpnhCFzmZAw4YwacRKfXMDRpb3ZAkGYXbwxEIc7qimTAarYjLx5Tnd1Co3kKZB7GdnHiMXNShg1EdW6xvbyVzfk57eNIXFp5l990U0PSZC3rnb1AZDZD'

    graph = facebook.GraphAPI(token)
    fields = ['link', 'creation_time']
    fields = ','.join(fields)
    print(fields)
    page = graph.get_object('wittyfeedIndia/posts', fields=fields)
    a = []
    for posts in page['data']:
        a.append((posts['id'], posts['link']))
    print(json.dumps(page['data'], indent=4))
    print(a)

