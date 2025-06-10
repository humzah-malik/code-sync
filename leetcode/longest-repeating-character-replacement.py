class Solution {
    public int characterReplacement(String s, int k) {
        int maxCount = 0;
        int freq[] =  new int[26];
        char[] b = s.toCharArray();
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = b[right];
            freq[c-'A']++;
            maxCount = Math.max(maxCount, freq[c-'A']);
            if ((right - left + 1) - maxCount > k) {
                freq[b[left]-'A']--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}