from functools import total_ordering
import priority_queue as q


@total_ordering
class Person(object):
    def __init__(self, name="No Name", age=0):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return '(' + str(self.name) + '; ' + str(self.age) + ')'


print("int MaxHeap:")
lst = []
q_int = q.PriorityQueue(lst, key=max, seq_type=int)

print("Checking is empty before assignment:", q_int.is_empty())

q_int.push(1)
q_int.push(2)
q_int.push(3)
q_int.push(4)
q_int.push(0)
q_int.push(100)

print("Checking is empty after assignment:", q_int.is_empty())
print("Heap size is", q_int.heap_size())
print(q_int, "is heap")
peeked = q_int.peek()
print(peeked, "is peeked element")

popped = q_int.pop()
print(q_int, "and", popped, "are heap and popped element")

# _________________________________

print('_' * 25, '\n')

# _________________________________

print("Person's MinHeap:")
lst = [Person("Name2", 2), Person("Name1", 1), Person("Name3", 3), Person("Name4", 4), Person("Name5", 0), Person("Name6", 100)]
q_person = q.PriorityQueue(lst, key=min)
q_person.push(Person("pushing", 40))
popped = q_person.pop()
print(q_person, 'and', popped)

peeked = q_person.peek()
print("\npeeked is", peeked)

print('_' * 25, '\n')

# _________________________________

q.christmas_tree(6)
