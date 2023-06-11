class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        return self._search_recursive(data, node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = self._find_min(node.right)
                node.right = self._delete_recursive(node.data, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.data

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Inorder Traversal:")
tree.inorder_traversal()  # Output: 2 3 4 5 6 7 8
print("\nPreorder Traversal:")
tree.preorder_traversal()  # Output: 5 3 2 4 7 6 8
print("\nPostorder Traversal:")
tree.postorder_traversal()  # Output: 2 4 3 6 8 7 5

# Searching for a value
search_value = 6
result = tree.search(search_value)
if result is not None:
    print(f"\nFound {search_value} not found}
    
    if result is not None:
        print(f"\nFound {search_value} in the tree.")
    else:
        print(f"\n{search_value} not found in the tree.")

# Deleting a node
delete_value = 4
print("\nDeleting node:", delete_value)
tree.delete(delete_value)
print("Inorder Traversal after deletion:")
tree.inorder_traversal()  # Output: 2 3 5 6 7 8
