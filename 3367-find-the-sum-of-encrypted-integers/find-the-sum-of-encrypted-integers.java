class Solution {

    public int sumOfEncryptedInt(int[] nums) {

        int sum = 0;

        for (int i : nums) {

            int ori = i;
            int max = 0;

            // Find maximum digit
            while (i > 0) {
                int temp = i % 10;
                max = Math.max(max, temp);
                i /= 10;
            }

            // Create encrypted number
            int newnum = 0;
            int place = 1;

            while (ori > 0) {
                int digit = ori % 10;

                newnum += max * place;

                place *= 10;
                ori /= 10;
            }

            sum += newnum;
        }
        return sum;
    }
}