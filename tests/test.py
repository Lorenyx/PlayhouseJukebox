from urllib.parse import urlparse, parse_qs


def parse_url(url: str):
    "Takes a youtube link and returns the ID"
    #TODO parse URLS
    schema = urlparse(url)

    if schema.netloc == 'youtu.be': # For shortened URLs
        return schema.path[1:] # [1:] removes '/' from path

    query = parse_qs(schema.query)
    if 'v' in query:
        return query['v'][0]
    return query['list'][0]
        

urls = [ 
    'https://www.youtube.com/watch?v=KoU-s08g5Hc',
    'https://www.youtube.com/watch?v=KoU-s08g5Hc',
    'https://youtu.be/KoU-s08g5Hc',
    'https://youtu.be/KoU-s08g5Hc?t=55',
    'https://www.youtube.com/playlist?list=PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El',
    'https://www.youtube.com/watch?v=0OmfowGG-AM&list=PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El&index=2',
    'https://www.youtube.com/watch?v=Efv_rmEcBC8&list=PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El&index=4'
   
]

for url in urls:
    print(parse_url(url))
    # scheme = urlparse(url)
    # print(parse_qs(scheme.query))
