namespaces = []


def find_namespace(name):
    for n in namespaces:
        if n['name'] == name:
            return n


def create_namespace(name, parent):
    namespaces.append({
        'name': name,
        'parent': parent,
        'vars': []
    })


def add(namespace, var):
    find_namespace(namespace)['vars'].append(var)


create_namespace('t', 'main')
create_namespace('a', 't')

add('a', 'hello')
add('a', 'lalka')

print(namespaces)
print(find_namespace('a')['vars'])
