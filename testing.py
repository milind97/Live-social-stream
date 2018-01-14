import os
import json
import facebook

if __name__ == "__main__":
    token = 'EAAEze9xMBS0BAEaSVRbqWYZCIUcgWQAJtucdKRak6ZCCY5wjgm2hSMf1sGK3Fx4NPjKu1ghCnsHDNo9CBwpes1gqsWX2HDt4HeZCEq9rdj2RkvTwFxaXc5OmN0SiTcn1DLsmPVGEpkYIlFc2m1JTTMtY2SZBDgxC749OV6hmxFqDZC3wUDZBHV70wz2n8zrcF8DzTi4h3SFgZDZD'

    graph = facebook.GraphAPI(token)
    fields = ['link', 'created_time']
    fields = ','.join(fields)
    print(fields)
    page = graph.get_object('wittyfeed/posts', fields=fields)
    a = []
    for posts in page['data'][:5]:
        a.append([posts['created_time'], posts['link']])

    a.sort(reverse=True)
    #print(json.dumps(page['data'], indent=4))
    print(a)
    b = list(map(lambda x: x[1], a))
    print(b)
    #print(a[:5])


