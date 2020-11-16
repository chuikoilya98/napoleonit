class Solution: 
    def romanToInt(self, s: str) -> int:

        #выписываем основные значение римских символов
        romanValue = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        #для удобства переведем в верхний регистр
        romanSymbols = s.upper()
        arabicList = []
        summ = 0

        #делим инпут на отдельные символы и вычисляем для каждого значения 
        for letter in romanSymbols:
            arabicList.append(romanValue[letter])

        #собираем сумму и выводим ответ
        for i,j in zip(arabicList[:-1], arabicList[1:]) :
            if i >= j:
                summ += i 
            else : 
                summ -= i
        summ += arabicList[-1]
        print(f'Ответ: {summ}')    

if __name__ == "__main__":
    s = input()
    sol = Solution().romanToInt(s)

