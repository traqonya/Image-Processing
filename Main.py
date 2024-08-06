inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_imagefile(f):
    global height, width
    first_linex= f.readline().rstrip()
    first_line= first_linex.split()
    width = int(first_line[1])
    height = int(first_line[2])
    img_matrixx=[[] for _ in range(height)]
    for i in range(height):
        current_rowx = f.readline().rstrip()
        current_row = current_rowx.split()
        for num in current_row:
            img_matrixx[i].append(int(num))
    f.close()
    return img_matrixx
def write_imagefile(f, img_matrixx):
    code = "P2"
    max_level = 255
    f.write(f"{code} {width} {height} {max_level}\n")
    for i in range(len(img_matrixx)):
        row = img_matrixx[i]
        f.write(" ".join(map(str, row)))
        if i < len(img_matrixx) - 1:
            f.write("\n")
    f.write("\n")
    return img_matrixx
def misalign(img_matrixx):
    for i in range(height//2):
        for j in range(width):
            if j %2 !=0:
                prev = img_matrixx[i][j]
                after = img_matrixx[height-i-1][j]
                img_matrixx[i][j] = after
                img_matrixx[height-i-1][j] = prev
            else: continue
    return img_matrixx
def sort_columns(img_matrixx):
    for j in range(width):
        my_list = list()
        for i in range(height):
            my_list.append((img_matrixx[i][j]))
            my_list.sort()
        for k in range(height):
            img_matrixx[k][j]= my_list[k]
    return img_matrixx
def sort_rows_border(img_matrixx):
    img_matrixx_final = [[] for _ in range(height)]
    for i in range(height):
        img_matrix_sort = []
        for num in img_matrixx[i]:
            if num != 0:
                img_matrix_sort.append(num)
            else:
                img_matrix_sort.sort()
                img_matrix_sort.append(0)
                img_matrixx_final[i].extend(img_matrix_sort)
                img_matrix_sort = []
        if img_matrix_sort:
            img_matrix_sort.sort()
            img_matrixx_final[i].extend(img_matrix_sort)
    return img_matrixx_final
def convolution(img_matrixx, kernel):
    img_matrix_last = list()
    for i in range(height+2):
        img_matrix_last.append([])
        for j in range(width+2):
            img_matrix_last[i].append(0)
    for i in range(height):
        for j in range(width):
            img_matrix_last[i+1][j+1]=img_matrixx[i][j]
    for i in range(height):
        for j in range(width):
            sum = 0
            for a in range(3):
                for b in range(3):
                    sum += img_matrix_last[i+a][j+b] *kernel[a][b]
            if sum > 255:
                sum = 255
            elif sum <0:
                sum=0
            img_matrixx[i][j]= sum
    return img_matrixx
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
