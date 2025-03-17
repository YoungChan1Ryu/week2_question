from priority_queue import PriorityQueue

class TestPriorityQueue:

  def test_priority_queue_push_pop(self):
    pq = PriorityQueue()

    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)

    assert pq.pop() == "Task 2"
    assert pq.pop() == "Task 3"
    assert pq.pop() == "Task 1"
    assert pq.pop() is None

  def test_priority_queue_empty_pop(self):
    pq = PriorityQueue()

    assert pq.pop() is None

  def test_priority_queue_push_pop_order(self):
    pq = PriorityQueue()

    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    pq.push("Task 4", 4)
    pq.push("Task 5", 0)

    assert pq.pop() == "Task 5"
    assert pq.pop() == "Task 2"
    assert pq.pop() == "Task 3"
    assert pq.pop() == "Task 1"
    assert pq.pop() == "Task 4"
    assert pq.pop() is None

  def test_priority_queue_duplicate_push_pop(self):
    pq = PriorityQueue()

    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    pq.push("Task 1", 4)

    assert pq.pop() == "Task 2"
    assert pq.pop() == "Task 3"
    assert pq.pop() == "Task 1"
    assert pq.pop() is not None

  def test_priority_queue_negative_priority(self):
    pq = PriorityQueue()

    pq.push("Task 1", 3)
    pq.push("Task 2", -1)
    pq.push("Task 3", 2)

    assert pq.pop() == "Task 2"
    assert pq.pop() == "Task 3"
    assert pq.pop() == "Task 1"
    assert pq.pop() is None
    