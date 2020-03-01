#
# https://dev.to/goyder/automatic-reporting-in-python---part-1-from-planning-to-hello-world-32n1
# https://www.w3.org/Math/
# https://tex.stackexchange.com/questions/23804/how-to-incorporate-tex-into-a-website
#

#Jinja tom combine
from jinja2 import FileSystemLoader, Environment
import shutil 
from numpy import sqrt
import pdfkit

#Math
a = 10
b = 3
c = 0

# Content to be published
content1 = "Hello, world!! Ass!"
content2 = 'This is a test'
a_input = a
b_input = b
c_input = c


#Calc
x1 = (-b+sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b-sqrt(b**2 - 4*a*c))/(2*a)

# Configure Jinja and ready the template
env = Environment(
    loader=FileSystemLoader(searchpath="template")
)
template = env.get_template("report_template.html")


def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """
    src = 'template/styles.css'
    dst = 'out/'

    #Copys styles.css to your output foler
    shutil.copy(src, dst, follow_symlinks=True)
    
    with open("out/report_out.html", "w") as f:
        f.write(template.render(content1=content1,
                                content2=content2,
                                x1_input=x1,
                                x2_input=x2,
                                a_input = a_input,
                                b_input = b_input,
                                c_input = c_input))

    

    

if __name__ == "__main__":
    main()

#pdfkit.from_file('report_out.html', 'out.pdf') 

print(x1,x2)
print('Done')