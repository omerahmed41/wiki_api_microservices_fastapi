from infrastructure.redis import redis_client


def add_new_suggestions(name):
    n = name.strip()
    for l in range(1, len(n)):
        prefix = n[0:l]
        redis_client.zadd('compl', {prefix: 0})
    redis_client.zadd('compl', {n + "*": 0})


def get_suggestions(prefix):
    results = []
    rangelen = 50  # This is not random, try to get replies < MTU size
    count = 5
    start = redis_client.zrank('compl', prefix)
    if not start:
        return []
    while (len(results) != count):
        range = redis_client.zrange('compl', start, start + rangelen - 1)
        start += rangelen
        if not range or len(range) == 0:
            break
        for entry in range:
            entry = entry.decode('utf-8')
            minlen = min(len(entry), len(prefix))
            if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
            if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])
    return results
