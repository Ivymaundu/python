lsc = [i for i in range(0,100) if i%2==0]

blogs = [
    {"id":1, "title":"PCI", "description":"starting..", "status":0},
    {"id":2, "title":"TSI", "description":"starting..", "status":0},
    {"id":3, "title":"VS", "description":"starting..", "status":1},
    {"id":4, "title":"K4", "description":"starting..", "status":0},
    {"id":5, "title":"ZX", "description":"starting..", "status":1},
]
# lsc = [blog for blog in blogs if blog["status"]==1]
# print(lsc)
active_blogs = [blog for blog in blogs if blog["status"]==1]


def turn_titlecase(x):
    w = x["title"].title('.')
    x["title"] = w
    return x

newblog={"id":5, "title":"ZX", "description":"starting..", "status":1}
print (newblog)


clean_blog = list(map(turn_titlecase,active_blogs))
print(clean_blog)

