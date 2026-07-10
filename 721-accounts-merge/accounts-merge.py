from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = list(range(len(accounts)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        email_to_id = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        groups = defaultdict(list)

        for email, idx in email_to_id.items():
            groups[find(idx)].append(email)

        result = []

        for idx, emails in groups.items():
            result.append([accounts[idx][0]] + sorted(emails))

        return result