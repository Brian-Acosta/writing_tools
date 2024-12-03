import pymupdf       # https://pypi.org/project/PyMuPDF/
import argparse

def highlight_weak_words(input_pdf_path, output_pdf_path):
    # List of weak words to highlight
    weak_words = [
        ' very ',
        ' pretty ', 
        ' somewhat ', 
        ' quite ',
        ' extremely ', 
        ' much ',
        ' dynamic  ', 
        ' dynamically ',
        ' quickly ',
        ' online ',
        ' robust ', 
        ' robustly '
        ' reliable ', 
        ' reliably ',
        ' reasonable ',
        ' nearly',
        ' relatively ', 
        ' kind of ',
        ' strongly ', 
        ' sort of ', 
        ' quite ', 
        ' seemingly ', 
        ' fairly ', 
        ' slightly ', 
        ' arguably ', 
        ' a lot ',  
        ' apparently ', 
        ' generally ', 
        ' typically ', 
        ' potentially ', 
        ' especially ', 
        ' fully ', 
        ' completely ',
        ' naturally ', 
        ' complex ', 
        ' fundamental ',
        ' fundamentally ',
        ' significantly ',
        ' clean ',
        ' elegant '
        ' basically ',
        ' possibly ', 
        ' should ',
        ' easily ',
        ' arguably ',
        ' simply ', 
        ' simple ',
        ' can ',
        ' practically ',
        ' believe ', 
        ' possible '
        ' might ', 
        ' really ',
        ' could ', 
        ' suggest ', 
        ' implies ', 
        ' seems ', 
        ' tends to', 
        ' may ',
        ' approximately '
    ]

    # Open the input PDF
    with pymupdf.open(input_pdf_path) as doc:
        for page in doc:
            for word in weak_words:
                text_instances = page.search_for(word)

                for inst in text_instances:
                    highlight = page.add_highlight_annot(inst)
                    highlight.update()
    
        doc.save(output_pdf_path, garbage=4, deflate=True, clean=True)

def main():
    parser = argparse.ArgumentParser(description='Highlight weak words in a PDF')
    parser.add_argument('input', help='Input PDF file path')
    parser.add_argument('-o', '--output', help='Output PDF file path', 
                        default='highlighted_weak_words.pdf')
    
    args = parser.parse_args()
    highlight_weak_words(args.input, args.output)

if __name__ == '__main__':
    main()
