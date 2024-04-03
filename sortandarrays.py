# Define a class named Solution.
class Solution:
    
    # Define a function named sort012 within the Solution class, which takes an array arr and its length n as input.
    def sort012(self, arr, n):
        
        # Initialize three pointers: low, mid, and high.
        low = 0  # Pointer for the current position of 0s.
        high = n - 1  # Pointer for the current position of 2s, initialized to the last index.
        mid = 0  # Pointer for the current position under observation.
        
        # Iterate until the mid pointer is less than or equal to the high pointer.
        while mid <= high:
            
            # If the element at mid is 0, swap it with the element at low and move both pointers.
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]  # Swap the elements at mid and low.
                mid += 1  # Move the mid pointer forward.
                low += 1  # Move the low pointer forward as well.
                
            # If the element at mid is 1, move the mid pointer.
            elif arr[mid] == 1:
                mid += 1  # Move the mid pointer forward.
                
            # If the element at mid is 2, swap it with the element at high and move the high pointer backward.
            else:
                arr[mid], arr[high] = arr[high], arr[mid]  # Swap the elements at mid and high.
                high -= 1  # Move the high pointer backward.
