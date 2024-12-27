class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        print(f"Inserting {key}...")
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted {key} as root.")
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        print(f"At node {node.key}.")
        if key < node.key:
            print(f"{key} < {node.key}, going left.")
            if node.left is None:
                node.left = Node(key)
                print(f"Inserted {key} to the left of {node.key}.")
            else:
                self._insert(node.left, key)
        elif key > node.key:
            print(f"{key} > {node.key}, going right.")
            if node.right is None:
                node.right = Node(key)
                print(f"Inserted {key} to the right of {node.key}.")
            else:
                self._insert(node.right, key)
        else:
            print(f"Error: Duplicate value {key} not allowed in BST.")

    def search(self, key):
        print(f"Searching for {key}...")
        result = self._search(self.root, key)
        print(f"Search result for {key}: {'Found' if result else 'Not Found'}.")
        return result

    def _search(self, node, key):
        if node is None:
            print("Reached a leaf node, key not found.")
            return False
        print(f"At node {node.key}.")
        if node.key == key:
            print(f"Key {key} found.")
            return True
        if key < node.key:
            print(f"{key} < {node.key}, going left.")
            return self._search(node.left, key)
        print(f"{key} > {node.key}, going right.")
        return self._search(node.right, key)

    def delete(self, key):
        print(f"Deleting {key}...")
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print("Key not found in the tree.")
            return node
        print(f"At node {node.key}.")
        if key < node.key:
            print(f"{key} < {node.key}, going left.")
            node.left = self._delete(node.left, key)
        elif key > node.key:
            print(f"{key} > {node.key}, going right.")
            node.right = self._delete(node.right, key)
        else:
            print(f"Found node with key {key}.")
            if node.left is None:
                print(f"Node {key} has no left child, replacing with right child.")
                return node.right
            elif node.right is None:
                print(f"Node {key} has no right child, replacing with left child.")
                return node.left
            min_larger_node = self._find_min(node.right)
            print(f"Replacing {node.key} with smallest key {min_larger_node.key} in the right subtree.")
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        print("Finding minimum value...")
        while node.left is not None:
            print(f"At node {node.key}, going left.")
            node = node.left
        print(f"Found minimum value: {node.key}.")
        return node

    def inorder_traversal(self):
        print("Performing inorder traversal...")
        result = self._inorder_traversal(self.root, [])
        print("Inorder traversal result:", result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            print(f"Visited node {node.key}.")
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

# Console-based interaction
def main():
    bst = BinarySearchTree()
    while True:
        print("\nOptions: \n1. Insert\n2. Search\n3. Delete\n4. Display Inorder Traversal\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            try:
                key = int(input("Enter value to insert: "))
                bst.insert(key)
            except ValueError:
                print("Error: Please enter a valid integer value.")
        elif choice == '2':
            try:
                key = int(input("Enter value to search: "))
                bst.search(key)
            except ValueError:
                print("Error: Please enter a valid integer value.")
        elif choice == '3':
            try:
                key = int(input("Enter value to delete: "))
                bst.delete(key)
            except ValueError:
                print("Error: Please enter a valid integer value.")
        elif choice == '4':
            bst.inorder_traversal()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

