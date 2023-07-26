Software installation
Windows 
 - Install MikTex from https://miktex.org/download
 - Use Texworks or Texnic center (free) 
Mac 
 - Install MacTex from https://www.tug.org/mactex/
 - Use Texpad (paid) or use Texshop that comes with MacTex distribution.

Read the tutorial of how to setup and run Latex from
http://course1.winona.edu/eerrthum/LaTeX/Windows.html


File list
undergrad-thai/eng-project.cls -- Class file for KMUTT Undergrad Project format
cpe.bib -- Example bibliography file. To be run with bibtex
undergrad-sample.pdf -- Example output generated from latex
undergrad-sample.tex -- Example latex source file. This should be the only file
                   that you modify. 
kmutt.bst -- Bibtex bibliography style file for the reference format. 
logo02.jpg -- Figure of KMUTT logo to be placed in the cover page.
model2.pdf -- Example graphic file in the sample output.
string.bib -- Predefined abbrevations to be used with cpe.bib

The latex file is to be used with xelatex.
To generate the output pdf, 
1. Run 'xelatex undergrad-sample.tex' for a few times 
2. Run 'bibtex undergrad-sample'
3. Run 'xelatex undergrad-sample.tex' again for a few times 

