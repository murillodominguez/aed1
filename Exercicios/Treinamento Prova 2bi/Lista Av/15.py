# 15. Sudoku – Linhas Únicas
# Implemente `linhas_validas(sudoku)` que receba uma matriz 9x9 e verifique se todas as
# linhas contêm apenas números de 1 a 9 sem repetição.

# def linhas_validas(sudoku):
#     if len(sudoku) != 9:
#         return False
#     for row in sudoku:
#         if len(row) != 9:
#             return False
#         seen = set()
#         for num in row:
#             if not (1 <= num <= 9):
#                 return False
#             if num in seen:
#                 return False
#             seen.add(num)
#     return True

def linhas_validas(sudoku):
	if len(sudoku) != 9:
		return False
	for row in sudoku:
		if len(row) != 9:
			return False
		char_list = []
		for element in row:
			if not isinstance(element, int):
				return False
			if element < 1 or element > 9:
				return False
			if element in char_list:
				return False
			char_list.append(element)
	return True

result = linhas_validas([[6,3,4,7,5,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]])

print(result)