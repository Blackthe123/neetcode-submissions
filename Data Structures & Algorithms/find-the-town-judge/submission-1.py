class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {}
        judge = []
        for i in trust:
            if i[1] not in trustMap:
                trustMap[i[1]] = set()
                trustMap[i[1]].add(i[0])
            else:
                trustMap[i[1]].add(i[0])

        print(trustMap)
        for person in trustMap:
            if (len(trustMap[person]) == n-1):
                judge.append(person);
                for personCheck in trustMap:
                    if person in trustMap[personCheck]:
                        judge.remove(person)
                        break
                
        
        if len(judge) == 1:
            return judge[0]
        else:
            return -1


        