
def Sol(arr, num):
    start = 0
    end = len(arr)
    if end = 0 or (end > 0 and arr[0] > num) or (end > 0 and arr[-1] > num):
        return -1
    while start < end:
        mid = int((start + end) / 2)
        if (num < arr[mid]):
            end = mid - 1
        elif (num > arr[mid]):
            start = mid + 1
        else:
            return mid

    return - 1
    



# 给一个 n * m 的 二维数组，每行元素递增，每列元素递增； 如何使用优秀的时间复杂度找到某个数字或者判断不存在？ 

arr = [[1, 2, 3], [2, 5, 6]]
num = 3

def Sol2(arr, num):
    row, col = 0, 0
    if arr == []: return -1
    row_len, col_len = len(arr[0]), len(arr) 
    
    for arr1 in arr:
        if (arr1[0] > num or arr1[-1] < num):
            continue
        s, e, m = 0, row_len, 0
        while s < e:
            m = int((s + e) / 2)
            if arr1[m] == num:
                return True
            elif arr1[m] < num:
                e = m - 1
            else:
                s = m + 1
    return False
                   


def Sol(arr, num):
    start = 0
    end = len(arr)
    if end == 0 or (end > 0 and arr[0] > num) or (end > 0 and arr[-1] < num):
        return -1
    while start <= end:
        mid = int((start + end) / 2)

        if (num < arr[mid]):
            end = mid - 1
        elif (num > arr[mid]):
            start = mid + 1
        else:
            return mid

    return - 1
    
##print (Sol([1, 2, 4], 4))
##       
##print (Sol([1, 2, 4], 3))
##
##print (Sol([1, 2, 4], 1))




def Sol1(input):
    result = {1:1, 2: 1}
    
    def countOne(num):
        print("num", num)
        counter = 0
        if num == 1: return 1
        while num > 1:
            divid = int(num / 2)
            print (num >> 1, num >> 1 , num - (num >> 1))
            ## return result[1 >> divid] + result[num - (num >> 1)]
            num = num - 2 ** (divid - 1)
            counter += 1            
        return counter
    for i in range(3, input):
        print (result)
        if (i % 2) == 0:
            result[i] = 1
        else:
            result[i] = (countOne(i))
    return result

print (Sol1(16))

