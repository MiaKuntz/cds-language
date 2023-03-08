# load packages
import spacy

# initialize spaCy
nlp = spacy.load("en_core_web_lg")

# defining main function
def main():
    text = "This is a string"
    doc = nlp(text)
    for token in doc:
        print(token.text)

if __name__=="__main__":
    main()