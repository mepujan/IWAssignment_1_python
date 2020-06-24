# Write a Python function to create the HTML string with tags around the
# word(s).

def html_function(html_string,html_tag):
    return "<%s>%s</%s>"%(html_tag,html_string,html_tag)

def main():
    html_string=input("Enter html string: ")
    html_tag = input("Enter html tag: ")
    print(html_function(html_string,html_tag))

if __name__ == '__main__':
    main()
