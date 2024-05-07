# Introduction and Review

## Notations of Complexity
In terms of time complexity there are 3 main notations. Big-O is most important because in our terms it gives us a worst case scenario
- **Big-O (Big-Oh)**: upper-bound on the number of operations performed
    - f(n) is O(g(n)) as some constant Ag(n) ≥ f(n) as n moves to ∞ infinity
    - f(n) is O(n)
- *Big-Omega (Big-Ω)*: lower-bound on the number of operations performed
    - f(n) is Ω(g(n)) if Bg(n) ≤ f(n) as n -> ∞
- *Big Theta (Big-ϴ)*: both upper and lower bound
    - f(n) is ϴ(g(n)) if f(n) is O(g(n)) AND f(n) is Ω(g(n))
    - f(n) is ϴ(g(n)) if Bg(n) ≤ f(n) ≤ Ag(n)

Here's another example: say I have an algorithm that, given a list of n students, prints out 5 header lines (independent of n) and then prints the n students' names and grades on separate lines. This algorithm will perform 2n + 5 operations total: 2 operations per student (print name, print grade) and 5 operations independent of the number of students (print 5 header lines). The time complexity of this algorithm in Big-O notation would be O(2n + 5), which we would simplify to O(n) because we drop the constant (2n becomes n) and drop all lower terms (5 < n as n becomes large).

## Good Time Complexities
- **"Constant Time"** = **O(1)**
- **"Logarithmic Time"** = "Scales/Increases Logarithmically" = **O(log n)**
- **"Polynomial Time"** = "Scales/Increases Polynomially" = **O(nk) (for any constant k)**
## Bad Time Complexities
- **"Exponential Time"** = "Scales/Increases Exponentially" = **O(kⁿ)** (for any constant k)
- **"Factorial Time"** = **O(n!)**

![](images/time-complexities.png)