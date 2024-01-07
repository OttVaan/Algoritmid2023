#Loome uue sõlme
def create_node(key):
    return {"key": key, "left": None, "right": None}

#Sisestame uue väärtuse, salvestame info sõnastikku.
def insert(root, key):
    if root is None:
        return create_node(key)
    else:
        if root["key"] < key:
            root["right"] = insert(root["right"], key)
        else:
            root["left"] = insert(root["left"], key)
    return root

#Prindime kõik liikmed rekursiivselt välja
def inorder_traversal(root):
    if root:
        inorder_traversal(root["left"])
        print(root["key"], end=' ')
        inorder_traversal(root["right"])

# Test:
root = None
keys = [15, 10, 20, 8, 12, 17, 25]

for key in keys:
    root = insert(root, key)

print("Inorder Traversal:")
inorder_traversal(root)
