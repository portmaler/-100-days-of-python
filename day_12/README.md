# Length of Last Word - LeetCode Solution

## 📝 Problem Description
Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

**Example:**
- **Input:** `s = "Hello World"`
- **Output:** `5`
- **Explanation:** The last word is "World" with length 5.

---

## 🚀 My Solution
I used a backward iteration approach to solve this efficiently. 

### Logic:
1.  **Trim:** Start from the end of the string and skip any trailing spaces.
2.  **Count:** Once a character is found, count backwards until the next space is hit.
3.  **Return:** The final count is the length of the last word.