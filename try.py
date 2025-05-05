# def chatbot():

#     print("Hello This is ChatBot")

#     while True:
#         user_in = input("you :").lower()
#         if 'hello' in user_in:
#             print("Heyy ! My Name is chatbot")
#         elif 'how are you' in user_in:
#             print("I am Fine what about you !")
#         elif 'fine' in user_in:
#             print("yahh good")
#         elif 'bye' in user_in:
#             print('ok bye bye !')
#             break
#         else:
#             print("invalid input")

# chatbot()



# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min_index]:
#                 min_index = j

#         arr[i],arr[min_index] = arr[min_index],arr[i]

# arr=[8,7,12,20,21,33,45]
# print("orignal array : ",arr)
# selection_sort(arr)
# print("sorted array :",arr)
def dfs_sort(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for i in graph[node]:
            dfs_sort(visited,graph,i)

def bfs_sort(visited,graph,s_node):
    queue = [s_node]
    visited.add(s_node)

    while queue:
        current = queue.pop(0)
        print(current,end=" ")

        for i  in graph[current]:
            if i not in visited:
              visited.add(i)
              queue.append(i)

def main():

    graph={
        1:[2,3],
        2:[4,5],
        3:[6,7],
        4:[],
        5:[],
        6:[],
        7:[]
    }

    print("\nDFS SHORT : ")
    dfs_sort(set(),graph,1)

    print("\nDFS SHORT : ")
    bfs_sort(set(),graph,1)

main()