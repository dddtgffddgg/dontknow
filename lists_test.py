import pytest

from list_node import ListNode
from my_list import MyList


@pytest.mark.listnode
@pytest.mark.parametrize("value", [0, 1, 69, 420])
def test_single_node_init(value):
    n = ListNode(value)
    assert isinstance(n, ListNode)
    assert n.value == value
    assert n.next == None


@pytest.mark.listnode
def test_wrong_init_raises_exception():
    with pytest.raises(TypeError):
        ListNode(1, 2)


@pytest.mark.listnode
@pytest.mark.parametrize("value1, value2", [(0, 1), (7, 3), (69, 420)])
def test_double_node_init(value1, value2):
    n2 = ListNode(value2)
    n1 = ListNode(value1, n2)
    assert isinstance(n1, ListNode)
    assert n1.value == value1
    assert n1.next == n2

    assert isinstance(n2, ListNode)
    assert n2.value == value2
    assert n2.next == None


@pytest.mark.listnode
@pytest.mark.parametrize("value", [0, 1, 69, 420])
def test_single_node_str(value):
    n = ListNode(value)
    assert str(n) == f"({value}) -> None"


@pytest.mark.listnode
@pytest.mark.parametrize(
    "values, str_values", [([0, 1], "(0) -> (1) -> None"), ([7, 3], "(7) -> (3) -> None")]
)
def test_double_node_str(values, str_values):
    nodes = ListNode(values[0], ListNode(values[1]))
    assert str(nodes) == str_values


@pytest.mark.listnode
def test_multi_node_str():
    nodes = ListNode(11, ListNode(22, ListNode(33, ListNode(69, ListNode(420)))))
    assert str(nodes) == "(11) -> (22) -> (33) -> (69) -> (420) -> None"


@pytest.mark.listnode
@pytest.mark.parametrize("value", [0, 1, 69, 420])
def test_single_node_eq(value):
    node1 = ListNode(value)
    node2 = ListNode(value)
    assert node1 == node2


@pytest.mark.listnode
@pytest.mark.parametrize("value1, value2", [(0, 1), (7, 3), (69, 420)])
def test_double_node_eq(value1, value2):
    node1 = ListNode(value1, ListNode(value2))
    node2 = ListNode(value1, ListNode(value2))
    assert node1 == node2


@pytest.mark.listnode
def test_multi_node_eq():
    node1 = ListNode(11, ListNode(22, ListNode(33, ListNode(69, ListNode(420)))))
    node2 = ListNode(11, ListNode(22, ListNode(33, ListNode(69, ListNode(420)))))
    assert node1 == node2


@pytest.mark.mylist
def test_list_init_empty():
    lst1 = MyList()
    assert lst1.head == None
    lst2 = MyList(None)
    assert lst2.head == None


@pytest.mark.mylist
@pytest.mark.parametrize("value", [0, 1, 69, 420])
def test_list_init_nonempty(value):
    lst = MyList(value)
    assert isinstance(lst.head, ListNode)
    assert lst.head.value == value
    assert lst.head.next == None
