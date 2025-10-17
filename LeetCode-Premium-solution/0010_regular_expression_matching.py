class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with dimensions (len(s)+1) x (len(p)+1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* etc.
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # Two cases:
                    # 1. Ignore the pattern with * (zero occurrences)
                    dp[i][j] = dp[i][j-2]
                    
                    # 2. Use the pattern with * if the current char matches the preceding char in pattern
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]