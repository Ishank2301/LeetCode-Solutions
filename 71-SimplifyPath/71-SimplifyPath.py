# Last updated: 27/10/2026, 9:03:20 pm
class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        st = []

        for comp in components:
            if comp == "" or comp == ".":
                continue
            
            if comp == "..":
                if st:
                    st.pop()
            else:
                st.append(comp)
        
        return "/" + "/".join(st)