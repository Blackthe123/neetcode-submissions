class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = {}
        output = []
        for i in range(len(points)):
            mapping[i] = (points[i][0])**2 + (points[i][1])**2
        print(mapping)
        sorted_dict = {k: v for k, v in sorted(mapping.items(), key=lambda item: item[1])}
        key_list = list(sorted_dict.keys())
        print(key_list)
        for i in range(k):
            output.append(points[key_list[i]])
        return output


        