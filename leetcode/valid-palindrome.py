class Solution {
    public boolean isPalindrome(String s) {
        int right = s.length() - 1;
        char[] b = s.toCharArray();
        for (int i = 0; i < right; i++) {
            while (i < right && !Character.isLetterOrDigit(b[i])) {
                i++;
            }
            while (i < right && !Character.isLetterOrDigit(b[right])) {
                right--;
            }
            if (Character.toLowerCase(b[i]) != Character.toLowerCase(b[right])) {
                return false;
            }
            right--;
        }
        return true;
    }
}