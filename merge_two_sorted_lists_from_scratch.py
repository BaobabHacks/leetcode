class Node():
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        if self.next_node:
            return f"{self.value}->{self.next_node}"
        return f"{self.value}"

first = Node(5, next_node=None)
second = Node(8, next_node=first)
# print(first)
# print(second)

# Input e.g. [1->2->4, 1->3->4]

def make_list(numbers):
    last_node = None
    for num in reversed(numbers):
        node = Node(
            value=num,
            next_node=last_node
        )
        last_node = node
    return last_node

input_ = [[1,2,4],[1,3,4]]
linked_lists = list()
for list_ in input_:
    linked_lists.append(
        make_list(list_)
    )

for ll in linked_lists:
    print(ll)

# Output: 1->1->2->3->4->4
def merged_linked_list(linked_lists):
    first_node = None
    last_node = None
    while True:
        if not linked_lists:
            break

        lowest_node = None
        print(f'linked_lists is now {linked_lists}')
        for node in linked_lists:
            if (
                lowest_node is None
                or
                lowest_node.value >= node.value
            ):
                lowest_node = node
        if not first_node:
            first_node = lowest_node
            last_node = lowest_node
        else:
            last_node.next_node = lowest_node
            last_node = lowest_node
        if lowest_node.next_node:
            linked_lists.append(lowest_node.next_node)
        linked_lists.remove(lowest_node)
        
    return first_node


merged = merged_linked_list(linked_lists)

print(f'Final result is: {merged}')
