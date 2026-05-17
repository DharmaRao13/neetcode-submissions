class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length;
        
        Map<Integer,Integer> arr =  new HashMap<>();
        for(int i =0;i<n;i++){
            arr.put(nums[i], arr.getOrDefault(nums[i], 0)+1);
        }
        for(Map.Entry<Integer,Integer> j: arr.entrySet()){
            int count = j.getValue();
            
            if (count>1){
                return true;
            }
        }
        return false;
    }
}

// class Solution {
//     public boolean hasDuplicate(int[] nums) {
//         // Use a HashSet for O(1) lookups
//         Set<Integer> seen = new HashSet<>();
        
//         for (int num : nums) {
//             // .add() returns false if the element already exists in the set
//             if (seen.add(num)) {
//                 return true; // Found a duplicate, exit immediately!
//             }
//         }
        
//         return false; // No duplicates found after checking everything
//     }
// }