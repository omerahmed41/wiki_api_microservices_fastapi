import json


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        raise Exception(f"can not find data between {first}, {last}")


def parser(content: str = ""):
    result = json.loads(content)
    page = result['query']['pages'][0]
    if "revisions" not in page:
        raise Exception('missing info for title')
    content = page['revisions'][0]['content']
    return find_between(content, "Short description|", "}}")
