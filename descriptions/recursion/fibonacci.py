"""
Solution: Recursion

Fibonacci:

Write a function fibonacci(n) that computes the Fibonacci number $F_n$, where $F_n$ is defined by the recurrence relation:

$$ F_n = F_{n-1} + F_{n-2}$$
with initial conditions of:
$$ F_1 = 1,  F_2 = 1$$

Example
```
f = 5
fib(1) => 1 == 1
fib(2) => fib(1) + fib(0) == 1
fib(3) => fib(2) + fib(1) => fib(1) + fib(0) + fib(1) == 2
fib(4) => fib(3) + fib(2) => fib(2) + fib(1) + fib(1) + fib(0) => fib(1) + fib(0) + fib(1) + fib(1) + fib(0) == 3
fib(5) => fib(4) + fib(3) => fib(3) + fib(2) + fib(2) + fib(1) => fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + fib(1) => fib(1) + fib(0) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + fib(1) == 5
```
"""