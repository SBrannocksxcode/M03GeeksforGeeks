class Solution:
    
    # Function to perform binary search
    def binarysearch(self, arr, N, K):
        # Initialize low and high pointers to define the search range
        low = 0  # Pointer to the start of the array
        high = N - 1  # Pointer to the end of the array
        
        # Perform binary search until low pointer is less than or equal to high pointer
        while low <= high:
            # Calculate mid index to divide the search range
            mid = (low + high) // 2
            
            # If element at mid is equal to K, return mid
            if arr[mid] == K:
                return mid
            
            # If element at mid is greater than K, search in left half
            elif arr[mid] > K:
                high = mid - 1  # Adjust high pointer to search in the left half
                
            # If element at mid is less than K, search in right half
            else:
                low = mid + 1  # Adjust low pointer to search in the right half
        
        # If K is not found in the array, return -1
        return -1
