__author__ = 'Grayj and Harman_a'

import tkinter as tk
import time
 
def main():
    width = 800
    height = 600
    root = tk.Tk()
    canvas = tk.Canvas(root, width = width, height = height)
    canvas.pack()
    canvas['bg'] = 'Beige'
    for number in range(1,21):   #cycles through all 20 text files
        file_name = 'vocabulary/g{}.txt'.format(number)
        filename = file_input(file_name)
        font_size = 24
        wpm = 450
        root.after(3000, cycle_text, root, canvas, filename, width, height, font_size, wpm)

    tk.mainloop()

def file_input(file_name):
             #"reads in the file and separates the information into tokens as well as strips the new line from being displayed on the canvas
             data = []
             with open(file_name, 'r', encoding= 'utf-8')as f:
                       text = f.read()
                       data.append(text)
                       for string in data:
                          data = string.strip('\n')
                          data = string.split()
             return data
                       
 
def cycle_text(root, canvas, filename, width, height, font_size, wpm):
    """reads the text in the format needed for the speed reading format"""
    wait_time = (1/(wpm/60))  #formula to determine wpm

    for t in filename:
        fi, padded_word = focus_index(t)
        if t.endswith(':'):
            topic = t
        canvas.create_rectangle(0, 0, width, height, fill = 'Beige')
        canvas.create_text(2*width//5, 2*height//5, text=topic, font=("Courier", font_size))
        canvas.create_text(width//2, height//2, text=padded_word , font=("Courier", font_size))
        canvas.create_text(width//2, height//2, text=t[fi], font=("Courier", font_size), fill = "red")
        time.sleep(wait_time) # do a calculation to convert wpm to required delay in seconds
        if t.endswith('.') or t.endswith(',') or t.endswith(";") or t.endswith(':'): # adds in additional delay for special characters.
            root.update()
            time.sleep(wait_time*2)

        root.update()
        canvas.delete('all') # clears the canvas of all elements to prevent slowdown as iterations are performed.




def focus_index(t):
     # determines how many spaces to add to the words to make sure the focus is on the letter at the correct index
    if len(t) <= 1:
         fi = 0
    elif len(t) >=2 and len(t) <= 5:
        fi = 1
        rs = len(t[fi+1:])
        ls = len(t[:fi])
        if ls < rs:
            p = rs - ls
            t = (' '*p)+t
        else:
            p = ls - rs
            t = t +(' '*p)
    elif len(t) >= 6 and len(t) <= 9:
        fi = 2
        rs = len(t[fi+1:])
        ls = len(t[:fi])
        if ls < rs:
            p = rs - ls
            t = (' '*p)+t
        else:
            p = ls -rs
            t = t +(' '*p)
    elif len(t) >= 10 and len(t) <= 13:
        fi = 3
        rs = len(t[fi+1:])
        ls = len(t[:fi])
        if ls < rs:
            p = rs - ls
            t = (' '*p)+t
        else:
            p = ls - rs
            t = t +(' '*p)
    else:
        fi = 4
        rs = len(t[fi+1:])
        ls = len(t[:fi])
        if ls < rs:
            p = rs - ls
            t = (' '*p)+t
        else:
            p = lf - rs
            t = t +(' '*p)

    return fi,t



if __name__ == '__main__':
             main()
