/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let totalSum = 0; 
    let leftSum =0;
   nums.forEach((element) => totalSum += element);
   for(let e=0; e<nums.length; e++){
      if(totalSum - leftSum - nums[e] === leftSum){
         return e;
      }
      leftSum += nums[e];
   }
   return -1;
};