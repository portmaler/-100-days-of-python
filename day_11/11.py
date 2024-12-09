class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31

        negative = (dividend < 0) ^ (divisor < 0)

        absDividend, absDivisor = abs(dividend), abs(divisor)

        quotient = 0

        while absDividend >= absDivisor:
            tempDivisor, multiple = absDivisor, 1
            while absDividend >= (tempDivisor << 1):
                tempDivisor <<= 1
                multiple <<= 1
            absDividend -= tempDivisor
            quotient += multiple

        return -quotient if negative else quotient

def test_remove_duplicates():
    solution = Solution()

    dividend = 10
    divisor = 3
    result = solution.divide(dividend,divisor)
    assert result == 3, f"Test failed for division. Expected length 3, got {result}."

    dividend = 21752
    divisor = 870
    result = solution.divide(dividend, divisor)
    assert result == 25, f"Test failed for division. Expected length 3, got {result}."


# Run the tests
test_remove_duplicates()

