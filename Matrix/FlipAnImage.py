nums = [[1,1,0],[1,0,1],[0,0,0]]
for image in nums:
    image.reverse()
    for indx in range(len(image)):
        image[indx]^=1
print(nums)





  














# for i in range(len(image)-1):
#     start = 0
#     end = len(image[i])-1
#     while start< end:
#         image[i][start],image[i][end] = image[i][end],image[i][start]
#         start+=1
#         end-=1
#     print(end)