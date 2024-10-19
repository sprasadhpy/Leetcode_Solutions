## Summary of Why This Is Greedy:

- **Local decisions**: At each index, the algorithm makes a local decision to jump as far as possible from that index.
- **Global solution**: These local decisions are sufficient to determine if the last index can be reached.
- **No backtracking**: Once the algorithm updates the farthest reachable index, it never revisits earlier steps or recalculates anything.
- **Efficiency**: The algorithm runs in linear time because it only considers each element once, making it a classic greedy solution.

---

## Why Backtracking is O(n²) or Worse:

- In the worst case, each index may lead to **n recursive calls**.
- For `n` indices, the number of total recursive calls can grow quadratically (or even worse in some cases) because you're exploring multiple paths at each step.
- The number of recursive calls grows like a tree, where each node can have several children (representing the possible jumps), leading to **O(n²)** time complexity or even **O(2^n)** in extreme cases, depending on how the jumps are structured.
