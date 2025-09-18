from fpdf import FPDF

class PDF(FPDF):

    def main():
        name = input("Name: ").strip()

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(False)
        pdf.add_page()

        #Title
        pdf.set_font("Helvetica", size=30)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=20, text="CS50 Shirtificate", align="C")

        #Shirt
        img_path = "shirtificate.png"
        pdf.image(img_path, x=17.5, y=50, w=175)

        #Name
        pdf.set_font("Helvetica", "B", 24)
        pdf.set_text_color(255, 255, 255)
        name_text = f"{name} took CS50"
        pdf.set_xy(0, 100)
        pdf.cell(w=210, h=10, text=name_text, align="C")

        pdf.output("shirtificate.pdf")

    if __name__ == "__main__":
        main()

