class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        run = 0
        while True:
            if len(students) == 0:
                return 0
            elif len(students) == run:
                return len(students)
            elif students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                run = 0
            else:
                students.append(students[0])
                students.pop(0)
                run += 1
        return len(students)       