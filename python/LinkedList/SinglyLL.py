


class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = next


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def traverse(head):
    current = head
    while current:
        print(str(current.data) + " -> ", end=" ")
        current = current.next
    print("None")

def insert_after_node(node, data):
    if node is None:
        print('Given node is None')
        return

    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node


if __name__ == "__main__":
    head = None
    head = insert_at_beginning(head, 4)
    head = insert_at_beginning(head, 3)
    head = insert_at_beginning(head, 2)
    head = insert_at_beginning(head, 1)

    insert_after_node(head, 54)
    traverse(head)