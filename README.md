# Weekend Health Take-home Challenge

**Objective:**

Implement a function named **`findWords`** that accepts two arguments: 1) an input string and 2) a dictionary. This function should return an array of words from the dictionary that can be formed by rearranging some or all of the letters in the input string. Each letter in the input string may be used up to once per word.

Please submit your solution by sharing a link to a Github repo.

**Function signature:**

```tsx
function findWords(inputString: string, dictionary:string[]): string[]

```

**Input:**

- **`inputString`** (type: **`string`**): A string consisting of lowercase English letters. The string may contain repeated letters.
- **`dictionary`** (type: **`string[]`**): An array that specifies the universe of valid output words. You can assume all words will consist of lowercase English letters.

**Example usage:**

```jsx
console.log(findWords("ate", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]));
// Expected output: ["ate", "eat", "tea"]

console.log(findWords("oogd", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]));
// Expected output: ["dog", "do", "god", "goo", "go", "good"]

```

**Additional Instructions:**

- Please submit this solution by sharing a link to a Github repo.
- A TypeScript solution would be ideal given that’s our tech stack, but other modern languages (e.g. Python) are fine too.
- Using third-party libraries is okay, but please avoid using libraries like **`itertools`** because they abstract away much of what makes this challenge interesting.
- We value strong engineering communication, so we're looking to see clean code that’s well-documented, functionally correct, and easy to read. Since the focus is on your thought process, you may want to be more verbose with your comments than with a typical PR.
- Please include at least a couple reasonable test cases. Instead of aiming for full test coverage, just tell us what else you'd test given more time.
- Consider edge cases, such as input strings with a single character or repeated letters.

**Evaluation Criteria:**

- Code Quality: The code should be well-organized, commented, and easy to read.
- Correctness: The function must correctly identify all possible words as per the specified rules.
- Efficiency: Efficiency will be considered, but should not come at the expense of code quality and correctness.


**How To Run**

 - Execute the solution.py file to see the output result
 ```
#python3 solution.py

Input:  ['ate', ['ate', 'eat', 'tea', 'dog', 'do', 'god', 'goo', 'go', 'good']]
Output:  ['ate', 'eat', 'tea']


Input:  ['oogd', ['ate', 'eat', 'tea', 'dog', 'do', 'god', 'goo', 'go', 'good']]
Output:  ['dog', 'do', 'god', 'goo', 'go', 'good']


Input:  ['', []]
Output:  []


Input:  ['', ['enlist', 'silent', 'inlet', 'tinsel', 'apple']]
Output:  []


Input:  ['listen', []]
Output:  []


Input:  ['a', ['a', 'b', 'c']]
Output:  ['a']


Input:  ['adc', ['a', 'b', 'c', 'a', 'a', 'd', 'b']]
Output:  ['a', 'c', 'a', 'a', 'd']


Input:  ['abc', ['a', 'b', 'c']]
Output:  ['a', 'b', 'c']


Input:  ['Listen', ['enlist', 'silent', 'inlet', 'tinsel']]
Output:  []


Input:  ['hello!', ['hello', 'world', 'hi']]
Output:  ['hello']

rishighanti@Rishikeshs-MacBook-Pro ds-algo % python3 solution.py

Input:  ['ate', ['ate', 'eat', 'tea', 'dog', 'do', 'god', 'goo', 'go', 'good']]
Output:  ['ate', 'eat', 'tea']


Input:  ['oogd', ['ate', 'eat', 'tea', 'dog', 'do', 'god', 'goo', 'go', 'good']]
Output:  ['dog', 'do', 'god', 'goo', 'go', 'good']


Input:  ['', []]
Output:  []


Input:  ['', ['enlist', 'silent', 'inlet', 'tinsel', 'apple']]
Output:  []


Input:  ['listen', []]
Output:  []


Input:  ['a', ['a', 'b', 'c']]
Output:  ['a']


Input:  ['adc', ['a', 'b', 'c', 'ax', 'ac', 'd', 'b']]
Output:  ['a', 'c', 'ac', 'd']


Input:  ['abc', ['a', 'b', 'c']]
Output:  ['a', 'b', 'c']


Input:  ['Listen', ['enlist', 'silent', 'inlet', 'tinsel']]
Output:  []


Input:  ['hello!', ['hello', 'world', 'hi']]
Output:  ['hello']

 ```