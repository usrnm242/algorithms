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
lst = [1, 2, 3, 4, 0, 100]
q_int = q.PriorityQueue(lst, key=max)
q_int.push(5)
popped = q_int.pop()
print(q_int, 'and', popped)

print('_' * 25, '\n')

print("Person's MinHeap:")
lst = [Person("Name2", 2), Person("Name1", 1), Person("Name3", 3), Person("Name4", 4), Person("Name5", 0), Person("Name6", 100)]
q_person = q.PriorityQueue(lst, key=min)
q_person.push(Person("pushing", 40))
popped = q_person.pop()
print(q_person, 'and', popped)

print('_' * 25, '\n')

q.christmas_tree(6)
