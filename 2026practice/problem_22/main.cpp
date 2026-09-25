#include <iostream>
#include <string>
#include <vector>
#include <cstring>

long long dp[12][2][2][12]; 
std::string num_str;

// Digit DP function to count total zeros up to a given number
long long count_zeros_up_to(long long n) {
    if (n < 0) return 0;
    if (n == 0) return 1; // Explicitly counting 0 if range includes it
    
    num_str = std::to_string(n);
    int len = num_str.length();
    
    // Reset DP table: dp[index][is_limit][is_leading_zero][zero_count]
    std::memset(dp, -1, sizeof(dp));
    
    auto solve = [&](auto& self, int idx, bool is_limit, bool is_leading_zero, int zero_count) -> long long {
        if (idx == len) {
            return zero_count;
        }
        
        if (dp[idx][is_limit][is_leading_zero][zero_count] != -1) {
            return dp[idx][is_limit][is_leading_zero][zero_count];
        }
        
        long long ans = 0;
        int limit = is_limit ? (num_str[idx] - '0') : 9;
        
        for (int digit = 0; digit <= limit; ++digit) {
            bool next_limit = is_limit && (digit == limit);
            bool next_leading_zero = is_leading_zero && (digit == 0);
            
            // Count '0' only if it is not a leading placeholder zero
            int next_zero_count = zero_count + ((digit == 0) && !next_leading_zero ? 1 : 0);
            
            ans += self(self, idx + 1, next_limit, next_leading_zero, next_zero_count);
        }
        
        return dp[idx][is_limit][is_leading_zero][zero_count] = ans;
    };
    
    // Add 1 to account for the actual number '0' itself if needed, 
    // but since your range starts at 1, we focus on the structure.
    return solve(solve, 0, true, true, 0) + 1; 
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    long long start, end;
    if (std::cin >> start >> end) {
        if (end < start) {
            std::cout << start << " " << end << ": 0\n";
        } else {
            // Number of zeros in [start, end] = Zeros up to 'end' - Zeros up to 'start - 1'
            long long total_zeros = count_zeros_up_to(end) - count_zeros_up_to(start - 1);
            std::cout << start << " " << end << ": " << total_zeros << "\n";
        }
    }
    return 0;
}
