from collections import Counter

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def chunk(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def group_by(items, key):
    groups = {}
    for item in items:
        k = item[key] if isinstance(item, dict) else getattr(item, key)
        groups.setdefault(k, []).append(item)
    return groups

def most_common(items, n=5):
    return Counter(items).most_common(n)

def unique(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]
