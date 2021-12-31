class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: 
            return 0
        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            # print('Deck id', deck_idx)
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx-1], -num)
                n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]
            # print("n Paths", n_paths)
            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0,n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])
            # print(decks)
            # print(paths)
            # print(ends_decks)
            # print("="*10)
        return paths[-1][-1]