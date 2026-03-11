class Solution:
    def bitwiseComplement(self, n: int) -> int:
        no_of_bits = len(str(bin(n))) - 2
        mask = ( 1 << no_of_bits ) -1
        all_set_bits = 1 | mask
        return n ^ all_set_bits