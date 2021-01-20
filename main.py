import pdfplumber  # module used to read pdf files
PDF_NAME = "PSY290Lecture2"


def _write_csv(text):
    title = PDF_NAME + ".txt"
    f = open(title, "wb")
    f.write(text.encode())
    f.close()


if __name__ == '__main__':
    pdf_name = r"C:\Users\Alice\PycharmProjects\NotesCreator\\" + PDF_NAME + ".pdf"
    pdf = pdfplumber.open(pdf_name)
    total_text = ""
    for p in pdf.pages:
        print("NEW PAGE====================================================")
        page_content = p.extract_text()
        page_number = page_content.rfind("\n")
        page_content = page_content[:page_number].replace("•", "-").replace("", "delta ")
        page_content = page_content.replace("Copyright © 2011 Pearson Education, Inc.", "")

        # format new lines
        page_content_split = page_content.split("\n")
        page_text = page_content_split[0]
        for i in range(1, len(page_content_split)):
            if page_text[-1] == " " and page_content_split[i][0] in "abcdefghijklmnopqrstuvwxyz":
                page_text += page_content_split[i]
            else:
                page_text += "\n"
                page_text += page_content_split[i]
        total_text += page_text
        total_text += "\n\n"
        print(page_text)

    _write_csv(total_text)
