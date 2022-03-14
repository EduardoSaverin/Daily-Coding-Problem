class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        new_path = []
        for index, ele in enumerate(arr):
            if ele == ".":
                if len(new_path) == 0:
                    # new_path.append(".")
                    pass
                else:
                    pass
            elif ele == "..":
                if new_path:
                    new_path.pop()
            elif ele == '':
                continue
            else:
                new_path.append(ele)
        return "/"  + "/".join(new_path)