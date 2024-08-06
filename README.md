# Image-Processing
This project involves implementing a small image processing application with various functionalities. The goal is to develop six distinct functions, each contributing to a specific image manipulation task. The project is divided into five main tasks, each worth 20 points, totaling 100 points.

Tasks Outline
Reading and Writing PGM Image Files

read_imagefile(f): This function reads a .pgm image file and returns the image as a matrix.
write_imagefile(f, img_matrix): This function writes a given image matrix to a .pgm file.
These functions are essential for loading images into the program and saving the processed images.
Misalign Columns

misalign(img_matrix): This function reverses the order of odd-numbered columns in the given image matrix. It introduces a misalignment effect by altering the column arrangement.
Sort Columns

sort_columns(img_matrix): This function sorts each column of the image matrix in ascending order from top to bottom. It rearranges the pixel values in each column.
Sort Rows with Borders

sort_rows_border(img_matrix): This function sorts each row of the image matrix in ascending order from left to right. However, the sorting is done independently within bordered sections of the row, preserving specific boundary constraints.
Convolution Operation

convolution(img_matrix, kernel): This function applies a convolution operation to the image matrix using a provided 3x3 kernel. The convolution process enhances or detects features in the image based on the kernel values.
