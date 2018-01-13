import os
import json
import facebook

if __name__ == "__main__":
    token = 'EAAEze9xMBS0BAMCQy0xL4gwXsmnZCGfReBpvTQdvORR1EG0MpKo28c427jHY2OYWoWX4ItZBZAhKsnVNGx85fNikQgjHV3rAelYSaRHctXfmZAR1ni1ZCAxEbSIpHGSyBZCamvZCGiZCKBNaWMnFu4IOEZCj6E4r9wVQU3YXj8lZAUjhb4gLVMkxmEdyxcbMD9RwQdQklrBed2ugZDZD'

    graph = facebook.GraphAPI(token)
    fields = ['link', 'created_time']
    fields = ','.join(fields)
    print(fields)
    page = graph.get_object('wittyfeed/posts', fields=fields)
    a = []
    for posts in page['data']:
        a.append([posts['created_time'], posts['link']])

    a.sort(reverse=True)
    #print(json.dumps(page['data'], indent=4))
    print(a)
    b = list(map(lambda x: x[2], a))
    print(b)
    #print(a[:5])


