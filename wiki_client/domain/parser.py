import json

from domain.Exception import DomainException


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        raise DomainException("String find exception", 502, f"can not find data between {first}, {last}")


def parser(content: str = ""):
    result = json.loads(content)
    page = result['query']['pages'][0]
    if "revisions" not in page:
        raise DomainException("String parser exception", 502, "missing info")
    content = page['revisions'][0]['content']
    return find_between(content, "Short description|", "}}")
