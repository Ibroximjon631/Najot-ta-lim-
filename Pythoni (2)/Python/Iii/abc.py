from fpdf import FPDF
class Ii_Information:
    def __init__(self):
        self.name = ""
        self.email = ""

    def inpt_info(self):
        print("Information larni kirting:")
        self.name = input("Name kiriting: ")
        self.email = input("Email kiriting: ")

    def create_pdf(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt="Info lar", ln=True, align="C")
        # Misol: Binafsha rang uchun
        pdf.set_text_color(128, 0, 128)  # Binafsha rang
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Name: {self.name}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {self.email}", ln=True)

        qr_code_image = "iii.png"
        pdf.image(qr_code_image, x=150, y=20,w=50)


        pdf_ii = "iii.pdf"
        pdf.output(pdf_ii)
        print(f"Saved ii: {pdf_ii}")

    def ii_info(self):
        self.inpt_info()
        self.create_pdf()

if __name__ == "__main__":
    ii = Ii_Information()
    ii.ii_info()

#source myenv/bin/activate
#deactivate