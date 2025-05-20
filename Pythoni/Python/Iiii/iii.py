#Qrcode yoq ligida Link blan
#Qr ni yuklash kerak
#pip3 install qrcode[pil]
#source .venv/bin/activate
#python3 iii.py
#Linux(Ubuntu)
import qrcode
from fpdf import FPDF
from PIL import Image
import os

class Ii_Information:
    def __init__(self):
        self.name=""
        self.email=""
        self.link="https://t.me/Lol_i_La_la_la"#Tg link.Ozgartirmang:(
    def inpt_info(self):
        print("Information larni kirting:")
        self.name=input("Name kiriting:")
        self.email=input("Email kiriting:")
    def create_qr_code(self):
        qr_code=qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,#Norm Skaner ucun yaxshi
        )
        qr_code.add_data(self.link)
        qr_code.make(fit=True)
        picture=qr_code.make_image(fill_color="black", back_color="white")#Qr rangi
        tmp_picture_file="iii.png"
        picture.save(tmp_picture_file,format='PNG')

        return tmp_picture_file



    def create_pdf(self):
        pdf=FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(200,10,txt="Info lar",ln=True,align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(200,10,txt=f"Name: {self.name}",ln=True)
        pdf.cell(200,10,txt=f"Email: {self.email}",ln=True)
        pdf.ln(10)
        pdf.cell(200,10,txt=f"Link: {self.link}",ln=True)
        picture_buffer=self.create_qr_code()
        pdf.image(picture_buffer,x=50,y=100)

        pdf_ii="iii.pdf"
        pdf.output(pdf_ii)
        print(f"Saved ii: {pdf_ii}")

    def ii_info(self):
        self.inpt_info()
        self.create_pdf()
if __name__ == "__main__":
    ii=Ii_Information()
    ii.ii_info()



#May 17 03:25 AM

