class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        2 pointers problem to know if you have moved on to the next letter
        
        ["a", "a", "a", "b"]
          l              r
        ["a", "b"]
        '''
        chars += [None]                                 # Trick to deal with the last element.
        cur = chars[0]      
        count = 0                                       # count: record the times one element had appeared. 
        slow = 0                                        # slow:  the idx ready to be modified.
        
        for i, char in enumerate(chars):    
            if char != cur:                             # When we meet a new element,
                chars[slow] = cur                       # we modify char[slow] to cur.
                cur = char                              # Update cur to new element.
                slow += 1                               # Update the position of slow.
				
                if count == 1:                          # If the previous element only appear once, skip below.
                    continue
                    
                for c in str(count):                    # Modify chars[slow] to appear times.
                    chars[slow] = c
                    slow += 1
                
                count = 1                               # Reset count = 1 because we met the new element.
				
            elif char == cur:
                count += 1
        
        return slow
        
#         if len(chars) == 1:
#             return 1
#         l, r = 0, 1
#         while r < len(chars):
#             if chars[l] != chars[r]:
#                 if (r-l) == 1:
#                     pass # do nothing
#                 else:
#                     # happens when there is duplicates
#                     # res.append(chars[l])
#                     # res.append(str(r-l))
#                     print(r)
#                     print(l)
#                     print(r-l)
#                     if r-l < 10:
#                         chars[r-1] = str(r-l)
#                     else:
#                         count = str(r-l)
#                         chars[r-1] = count[0]
#                         for j in range(1,len(count)):
#                             chars.insert(r - 1 + j, count[j])
#                     for i in range(r-3, l-1, -1):
#                         chars.pop(i)
#                 l = r
#                 r = l+1
#                 # print(l)
#                 # print(r)
                
#             else:
#                 r += 1
#         if r - l != 1:
#             if r - l < 10:
#                 chars[-1] = str(r-l)
#             else:
#                 count = str(r-l)
#                 chars[r-1] = count[0]
#                 for j in range(1,len(count)):
#                     chars.append(count[j])
#             for i in range(r-3, l-1, -1):
#                 chars.pop(i)
        # return len(chars)
    
    
        