class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        for i in range(numCourses):
            pre_map[i] = []

        for prereq in prerequisites:
            pre_map[prereq[0]].append(prereq[1])

        visited = set()

        def dfs(cid) -> bool:
            print(f"evalutating {cid=}")
            if cid in visited:
                print(f"in visited {cid=}")
                return False
            if pre_map[cid] == []:
                print(f"empty value {cid=}")
                return True

            visited.add(cid)
            for pre in pre_map[cid]:
                print(f"{pre=}")
                if not dfs(pre):
                    print(f"returning false {cid=}")
                    return False


            pre_map[cid] = []
            visited.remove(cid)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True