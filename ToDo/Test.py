import maliang

root = maliang.Tk()
canvas = maliang.Canvas()
canvas.pack(expand=True, fill="both")

maliang.Button(canvas, (20, 20), text="Button").bind_on_update(lambda s, _: print(s))
root.mainloop()
