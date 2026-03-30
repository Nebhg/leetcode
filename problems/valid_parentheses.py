class Solution:
    inputs =[

        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]"
    ]

    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(','{','[']
        closing = [')', '}', ']']

        for p in s:
            if len(s) % 2 != 0:
                return False
            elif p in opening:
                stack.append(p)
            elif p in closing:
                if not stack or opening.index(stack.pop()) != closing.index(p):
                    return False
        return not stack

if __name__ == "__main__":
    solution = Solution()
    for test in solution.inputs:
        result = solution.isValid(test)
        print(f"isValid('{test}') = {result}")
