import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

class BookCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Book Creator")
        
        self.pages = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="Enter Text:")
        self.text_label.pack()
        
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack()
        
        self.add_text_button = tk.Button(self.root, text="Add Text", command=self.add_text)
        self.add_text_button.pack()
        
        self.add_image_button = tk.Button(self.root, text="Add Image", command=self.add_image)
        self.add_image_button.pack()
        
        self.save_button = tk.Button(self.root, text="Save Book", command=self.save_book)
        self.save_button.pack()
    
    def add_text(self):
        text = self.text_entry.get()
        if text:
            self.pages.append(("text", text))
            self.text_entry.delete(0, tk.END)
    
    def add_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if image_path:
            self.pages.append(("image", image_path))
    
    def save_book(self):
        book_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if book_path:
            c = canvas.Canvas(book_path, pagesize=letter)
            width, height = letter
            
            for page in self.pages:
                if page[0] == "text":
                    text = page[1]
                    # Add colorful design and beautiful text here
                    c.setFont("Helvetica", 12)
                    c.setFillColorRGB(0, 0, 0.8)  # Example: Blue Color
                    c.drawString(100, height - 100, text)
                elif page[0] == "image":
                    image_path = page[1]
                    # Add aesthetic design to image display
                    c.drawImage(image_path, 100, height - 500, width=400, height=400)
                c.showPage()
            
            c.save()
            print(f"Book saved as {book_path}")

root = tk.Tk()
app = BookCreator(root)
root.mainloop()
