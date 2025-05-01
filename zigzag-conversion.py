class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for i in range(numRows)]
        if numRows == 1:
            cycle = 1
        else:
            cycle = numRows * 2 - 2
        for i in range(len(s)):
            i_ = i % cycle
            if (i_) < numRows:
                rows[i_] += s[i]
            else:
                rows[2 * (numRows - 1) - (i_)] += s[i]

        output = str()
        for row in rows:
            output += "".join(row)
        return output

print(Solution().convert("PAYPALISHIRING", 4))