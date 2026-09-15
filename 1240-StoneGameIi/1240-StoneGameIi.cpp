// Last updated: 15/9/2026, 11:35:04 pm
class Solution {
public:
    //26 24 17 8 4
    int solve(int ind, int m, vector<int>&nums, vector<vector<int>>&dp){
        if(ind>=nums.size())return 0;
        if(ind+m*2>=nums.size())return nums[ind];
        if(dp[ind][m]!=-1)return dp[ind][m];
        int cost = INT_MAX;
        for(int i=1;i<=2*m;i++){
            cost = min(cost, solve(i+ind,max(i,m),nums,dp));
        }

        return dp[ind][m] = nums[ind] - cost;
    }

    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        for(int i=n-2;i>=0;i--){
            piles[i]+=piles[i+1];
        }

        vector<vector<int>>dp(n,vector<int>(n,-1));
        return solve(0,1,piles,dp);
    }
};