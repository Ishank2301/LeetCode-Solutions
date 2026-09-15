# Last updated: 15/9/2026, 11:34:13 pm
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # Union set is list of parents
        # Ending in smallest number in set

        # everyone is in their own set
        parents = [x for x in range(n)]

        def find(a):
            """Find set that a is in"""
            if parents[a] == a:
                return a
            
            p = find(parents[a])
            parents[a] = p
            return p
        
        # Restrictions are between components
        # After joining, restrictions are the union of former restrictions
        # So can have simple map of restrictions and update after union

        rest = defaultdict(set)
        for u,v in restrictions:
            rest[u].add(v)
            rest[v].add(u)
        
        res = []

        for a,b in requests:
            ca, cb = find(a), find(b)
            if ca == cb:
                res.append(True)
                continue
            # Not yet connected
            # Is there a restriction?
            if cb in rest[ca]:
                res.append(False)
                continue
            
            # Let's connect
            res.append(True)
            parents[cb] = ca
            rest[ca] |= rest[cb]
            # Add restriction to ca to all cb targets
            for target in rest[cb]:
                rest[target].discard(cb)
                rest[target].add(ca)
        
        return res


        