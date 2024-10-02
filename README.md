# **Coding Adventures: A Journey Through My "Stupid" Free Time**

### Welcome to my collection of quirky coding challenges!

This repository contains a series of problems I've tackled during my free time—each one a step in my ongoing journey as a programmer. I call them "stupid things," but they represent the grind and learning every coder goes through. 

Here's the fun part: alongside each of my initial attempts, you’ll find optimized versions provided by ChatGPT. It's a way to compare brute-force attempts with more optimized, elegant solutions.

---

## **Table of Contents**

1. [Filling in the Smallest Missing Positive Integer](#1-filling-in-the-smallest-missing-positive-integer)
2. [Finding the Duplicated Number in an Array](#2-finding-the-duplicated-number-in-an-array)
3. [Summing the Minimums of All Subarrays](#3-summing-the-minimums-of-all-subarrays)
4. [Finding the Largest Rectangle in a Histogram](#4-finding-the-largest-rectangle-in-a-histogram)

*Compare and contrast my raw attempts with ChatGPT’s optimized solutions.*

---

## 1. **Filling in the Smallest Missing Positive Integer**

### Problem Description:
Given an unsorted array of integers, the goal is to find the smallest missing positive integer.

### My Attempt:
- **Approach**: Brute-force method using array sorting and filling.
- **Complexity**: O(n²) in the worst case.
- **Result**: It works but is slow for larger arrays.

### ChatGPT’s Optimized Solution:
- **Approach**: Optimized with in-place swapping for better space complexity.
- **Complexity**: O(n).
- **Result**: Efficient and scales well with large arrays.

---

## 2. **Finding the Duplicated Number in an Array**

### Problem Description:
In an array of `n+1` integers where each integer is between `1` and `n`, find the duplicated number.

### My Attempt:
- **Approach**: Sort the array and scan for duplicates.
- **Complexity**: O(n log n) due to sorting.
- **Result**: Functional but can be inefficient for large datasets.

### ChatGPT’s Optimized Solution:
- **Approach**: Use a set to detect duplicates in a single pass.
- **Complexity**: O(n).
- **Result**: Efficient, using O(n) space but runs in linear time.

---

## 3. **Summing the Minimums of All Subarrays**

### Problem Description:
For a given array, find the sum of the minimum value of every possible subarray.

### My Attempt:
- **Approach**: Brute-force with nested loops to generate and evaluate each subarray.
- **Complexity**: O(n³).
- **Result**: Gets the job done, but the time complexity is far from ideal.

### ChatGPT’s Optimized Solution:
- **Approach**: Monotonic stack to efficiently calculate subarray minimums.
- **Complexity**: O(n).
- **Result**: Drastically faster and scalable for large arrays.

---

## 4. **Finding the Largest Rectangle in a Histogram**

### Problem Description:
Given an array where each element represents the height of a bar in a histogram, find the area of the largest rectangle that can be formed.

### My Attempt:
- **Approach**: Brute-force checking of all possible rectangle heights and widths.
- **Complexity**: O(n³) due to nested loops.
- **Result**: Works, but painfully slow for larger inputs.

### ChatGPT’s Optimized Solution:
- **Approach**: Monotonic stack for efficient calculation of largest rectangle area.
- **Complexity**: O(n).
- **Result**: Fast, with an elegant approach that minimizes redundant calculations.

---

## **Why Compare?**

By juxtaposing my initial solutions with ChatGPT’s optimized algorithms, I’ve been able to:
- **Learn** about various data structures and algorithms, such as monotonic stacks, in-place operations, and optimal searching.
- **Recognize** the importance of algorithmic complexity when scaling up to larger inputs.
- **Improve** my problem-solving skills, understanding that there’s always a better way to tackle even seemingly simple problems.

---

## **Conclusion**

This repository is a collection of humble coding attempts that evolve with each problem, along with lessons learned along the way. I hope you enjoy comparing my brute-force, "trial-and-error" approaches with more refined, optimized solutions from ChatGPT.

It’s proof that no attempt is ever really stupid—each is a step toward becoming a better programmer. So let’s embrace the messiness of learning!

---

*The best part? You can explore both solutions and compare my code with ChatGPT’s directly.*

---

_**James Potter**_

---

### **License**
This project is open-source and available under the [MIT License](LICENSE).
