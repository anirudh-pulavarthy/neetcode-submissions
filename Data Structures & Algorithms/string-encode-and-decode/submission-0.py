class Solution:
    # v1: Brute-force solution using non ascii characters 
    # é as delimiter and ñ to indicate a null string

    def encode(self, strs: List[str]) -> str:
        if strs:
            strs = ['ñ' if s == '' else s for s in strs]
            return 'é'.join(strs)
        return ''

    def decode(self, s: str) -> List[str]:
        if s == '': return []
        strs = s.split('é')
        strs = ['' if s == 'ñ' else s for s in strs]
        return strs