from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == '__main__':
    input_list = [1, 1, 2]
    input_linked_list = list_to_linked_list(input_list)

    expected_output_list = [1, 2]
    expected_output_linked_list = list_to_linked_list(expected_output_list)

    result_linked_list = delete_duplicates(input_linked_list)

    assert linked_list_to_list(result_linked_list) == expected_output_list
