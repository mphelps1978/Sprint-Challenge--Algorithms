#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This one is deceptively `O(n)` as it is coded to look like it's `O(n^3)` or `O(n^2)`

b) This one is `O(n^2)` - The outer loop has a complexity of `O(n)` and the inner runs for `n/2` iterations. `O(.5 * n^2)` becomes `O(n^2)`

c) `O(n)` over the number of bunnies

## Exercise II

`Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.`

First we need to set some variables:

- The `Current` Floor we are on
- the `lowest` possible floor
- the `highest` possible floor
- the `total` number of floors

`lowest` will be 0
`highest` will be n
`Current` will be n / 2
`Total`Floors will be the length of n

Now we drop

if the egg breaks:

- `highest` = `current - 1`
- `current` = `(current + lowest) / 2`

If the egg doesn't break:

- `lowest` = `current - 1`
- `current` = `(current + highest) / 2`

We then will repeat this process until `lowest` and `highest` are the same (the floors have converged)

If the egg doesn't break at this converged floor, `f` is the value of this floor, otherwise `f` is the value of this floor - 1

RTC `O(n)`
