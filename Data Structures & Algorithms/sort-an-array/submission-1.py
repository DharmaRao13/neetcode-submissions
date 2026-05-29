class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr)<=1:
            return arr

        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]

        self.sortArray(left_arr)
        self.sortArray(right_arr)

        i=0
        j=0
        k=0

        while (i<len(left_arr) and (j<len(right_arr))):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1


        while (i<len(left_arr)):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

        return arr                      