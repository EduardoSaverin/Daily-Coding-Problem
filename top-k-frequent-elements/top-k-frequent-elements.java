class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num , 1);
            }
        }
        class Pair {
            int num;
            int count;
            Pair(int num, int count) {
                this.num = num;
                this.count = count;
            }
        }
        Comparator<Pair> comp = new Comparator<Pair>() {
            public int compare(Pair p1, Pair p2) {
                if (p1.count == p2.count) {
                    return p1.num - p2.num;
                }
                return p1.count - p2.count;
            }
        };
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>(k, comp);
        for (int num : nums) {
            if (!map.containsKey(num)) {
                continue;
            }
            Pair p = new Pair(num, map.get(num));
            if (queue.size() < k) {
                queue.offer(p);
            } else {
                Pair top = queue.peek();
                if (top.count < p.count) {
                    queue.poll();
                    queue.offer(p);
                }
            }
            map.remove(num);
        }
        int[] result = new int[k];
        int index = 0;
        for (Pair p : queue) {
                result[index++] = (p.num);
            }
            return result;
    }
}