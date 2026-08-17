"""Small math helpers promoted from job pipeline experiments."""

from __future__ import annotations


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """Return n! for n >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fib(n: int) -> int:
    """Return the n-th Fibonacci number (n >= 0)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (case-insensitive, alphanumeric only)."""
    t = "".join(ch.lower() for ch in s if ch.isalnum())
    return t == t[::-1]
