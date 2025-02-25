import fitz

# file = fitz.open("book.pdf")
# for page in file:
#     text = page.get_text()
#     print(text)

# with open('yy.txt', 'w') as f:
#     for page1 in file:
#         f.write(page1.get_text())   

# f.close()


# file = fitz.open("book2.pdf")
# for page1 in file:
#     text1 = page.get_text()
#     print(text1)

# with open('yy.txt', 'a') as f:
#     for page2 in file:
#         f.write(page2.get_text())  











# for i in file:
#     print(i)
#print(file[0])

# page = 0



def read_book(name):
    file = fitz.open(name)
    for page in file:
        text = page.get_text()
        print(text)

    with open('yy.txt', 'a') as f:
        for page1 in file:
            f.write(page1.get_text())

read_book('book.pdf')
read_book('book2.pdf')