This Python code is designed to show the main concepts and operations of two fundamental data structures: Stacks (LIFO - Last-In, First-Out) and Queues (FIFO - First-In, First-Out), using Python.


The script uses practical examples to show how Stacks and Queues operate:

1. Stack Operations (LIFO)
Undo Functionality (Portal): Simulates a portal application's undo feature where the last two actions (Trancript and Download) are removed from the stack using the pop() operation.

Financial Transaction (Momo Pay): Simulates a mobile payment process where the final action (Confirm) is removed/undone.

LIFO Challenge: Demonstrates pushing elements (X, Y, Z), popping (Z), pushing a new element (W), and accessing the Top element (the last one added).

Reflection: Includes a text explanation of why the Stack is suitable for undoing financial transactions (only the most recent transaction can be easily reversed).

2. Queue Operations (FIFO)
Bank ATM Line (BK ATM): Simulates a bank line where the first two people (jean, alain) are served (removed from the front) using pop(0).

Bus Departure: Simulates buses departing from a park, where the first three buses are removed from the front of the list (pop(0)).

Voting Line (Election): Simulates a fair voting process where voters are removed in the exact order they arrived (ngenzi first, then manzi, etc.) using pop(0).

Reflection: Includes a text explanation of why the Queue ensures a fair election process (First-Come, First-Voted).

Key Python List Methods Used 
Data Structure	Concept	Python Method	Description
Stack	Push (Add)	list.append()	Adds an element to the end (top) of the stack.
Stack	Pop (Remove)	list.pop()	Removes and returns the element from the end (top) of the stack.
Queue	Enqueue (Add)	list.append()	Adds an element to the end (back) of the queue.
Queue	Dequeue (Remove)	list.pop(0)	Removes and returns the element from the beginning (front) of the queue.



