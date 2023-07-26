
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     Filename = cpe-project.cls v1.0
%     Data Jun 4, 2020
%     Author   = Peerapon Siripongwutikorn (peerapon@cpe.kmutt.ac.th)
% 
% This is a LaTeX class file for project report and thesis at CPE,
% KMUTT.
% Date: May 25, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Edited
% May 26, 2016
% - Width of box holding section number too small. 
% Old:    \@tempdima 2em        % width of box holding section number
% New:    \@tempdima 3em
% - Baseline skip 
% Old: 
% \def\baselineskipxii{24pt}
%\def\baselineskipxi{18.6pt}  % for title and signature page
% New:
%\def\baselineskipxii{16pt}
% \def\baselineskipxi{16pt}  % for title and signature page


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cpe-grad}[2016/05/30 CPE,KMUTT latex class]
\LoadClass{report}
\typeout{Document Style `CPE thesis/report'.}
\newcommand{\dotrule}[1]{% 
      \parbox[t]{#1}{\dotfill}} 


\usepackage[left=4cm,top=3cm,right=2cm,bottom=2cm]{geometry} 
\usepackage{graphicx} %%% Use the option pdftex instead of
                             %%% dvips if you use pdflatex 
\usepackage{array}
\usepackage{amsfonts,amsmath} %% For math fonts and operations

\usepackage{mathspec}
\usepackage[no-math]{fontspec} %Font package
\usepackage{xunicode,xltxtra}
\usepackage{url}
% April, 2022 by Thanin
% Fix error when use \url with polyglossia in Thai. Url default font doesn't work in Thai environment.
% Setting the style to be the same as Thai font solve the issue
\urlstyle{same}

\usepackage{hyperref}
\hypersetup{
	linktocpage,
    colorlinks=true, %set true if you want colored links
%    linktoc=all,     %set to all if you want both sections and subsections linked
    linkcolor=blue,  %choose some color if you want links to stand out
}

%%%% For using thaifonts
%%% Comment out if using Polyglossia package
%\newcommand{\textthai}[1]{{\fontspec[Language=Thai,Scale=1.23]{TH Sarabun New:script=thai}#1}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Definitions of major strings %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\disstitleone{TITLE OF DISSERTATION}      % 1st line of TITLE of dissertation
\def\disstitletwo{}                           % 2nd line of TITLE if needed
\def\disstitlethree{}                         % 3rd line of TITLE if needed
\def\disstitlefour{}                          % 4th line of TITLE if needed
\def\dissauthor{Your Name 1}              % Author of dissertation
\def\dissauthortwo{Your friend's name 2 }              % Author of dissertation
\def\dissauthorthree{Your friend's name 3}              % Author of dissertation

\def\dissdiplomaone{B.A., Carnegie Mellon University, 1991} % first degree
\def\dissdiplomatwo{M.S., University of Pittsburgh, 1993}   % second degree
\def\dissdiplomathree{}                       % still in school?
\def\dissdiplomafour{}                        % collecting them?
\def\dissdegree{Doctor of Philosophy}         % Name of the degree
\def\dissdegreeabrev{Ph.D.}                   % Abbreviation of the degree
\def\dissyear{1995}                           % Year of submission
\def\dissdefensedate{June 1 2000}             % Date of defense
%\def\disscommitteechair{Prof. Francis Crick}  % Name of the Chairman
\def\dissadvisor{Prof. My advisor }   % Advisor
\def\disscoadvisor{My Co-advisor, Ph.D.}  % Co-advisor
\def\disscoadvisorr{My Co-advisor2, Ph.D.}  % Co-advisor
\def\disscommitteetwo{Prof. Committee}   % 2rd committee member
\def\disscommitteethree{}   % 3rd committee member
\def\disscommitteefour{}                      % 4th committee member

\def\thaiworktype{}
\def\thaidisstitleone{}
\def\thaidisstitletwo{}
\def\thaidisauthor{}
\def\thaidisauthortwo{}
\def\thaidisauthorthree{}
\def\thaidissadvisor{}
\def\thaidissdegree{}
\def\thaidissyear{}

\def\fnum@figure{รูปที่~\thefigure}
\def\fnum@table{ตารางที่~\thetable}
\renewcommand{\chaptername}{บทที่}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 
% Include the following line (uncommented) in your dissertation file
% if your work has more than one appendix. This is what will be written on the 
% cover page preceding the appendices.  By default, it is set to {Appendix}.
% 
% \def\appendixnames{Appendices}              % if more than one appendix
% 
% Your dissertation should be structured the following way:
% \maketitlepage, \makecopyrightpage, \makesignaturepage,
% \abstract{}, \preface{}, \tableofcontents, \listoftables, \listoffigures,
% \chapter{},....., \appendix{},.....,
% \thebibliography (or \bibliography{} with BiBTeX), \theindex
% 
% ************************************************************************


% **************************************************************************
% Redefinition of some values
% **************************************************************************
\def\ssp{\def\baselinestretch{1.0}\large\normalsize}
\def\dsp{\def\baselinestretch{1.37}\large\normalsize}
%\def\dsp{\def\baselinestretch{1.1}\large\normalsize}
\newif\ifdraftmode \draftmodefalse
\ifdim \overfullrule > 0pt \draftmodetrue \ssp \else \dsp \fi  % draft mode on?
\def\truebaselineskip{\baselineskip}
\def\baselineskipxii{16pt}
\def\baselineskipxi{16pt}  % for title and signature page
\def\emptyline#1{\vspace*{#1\baselineskip}}
\newif\iffirstappendix \firstappendixtrue
\newif\iffirstchapter \firstchaptertrue
\def\tocprefix{}
\newif\ifprelude \preludetrue
\newif\ifromanmode \romanmodetrue \pagenumbering{roman}
\def\setarabic{\ifromanmode \romanmodefalse \pagenumbering{arabic} \fi}
\setcounter{secnumdepth}{5}
\topmargin -0.8cm \oddsidemargin 0.5 in
%\textheight 9.0truein \advance\textheight by \topskip \textwidth 6.0truein
\textheight 24.69cm \advance\textheight by \topskip \textwidth 6.0truein
\footskip 30pt \footnotesep 7.7pt
\headheight 12 truept \headsep 25 truept
\onecolumn \parindent 0em
\if@twoside\else\raggedbottom\fi
\widowpenalty=10000 \clubpenalty=10000 \looseness=1

% ***********************************************************************
% Modifications for single spacing and indentation, from Ethan V. Munson's 
% style file for dissertations at the Univ of California
% ***********************************************************************

\def\smallssp{\def\baselinestretch{1.0}\large\small}
\def\scriptsizessp{\def\baselinestretch{1.0}\large\scriptsize}
%\def\tabular{\par\ssp\let\@halignto\@empty\@tabular}
%\expandafter \def\csname tabular*\endcsname #1{\par\ssp\def\@halignto{to#1}\@tabular}
\def\smalltabular{\par\smallssp\let\@halignto\@empty\@tabular}
\def\endsmalltabular{\endtabular}
\expandafter \def\csname smalltabular*\endcsname #1{\par\smallssp\def\@halignto{to#1}\@tabular}
\expandafter \let \csname endsmalltabular*\endcsname = \endtabular
\def\scriptsizetabular{\par\scriptsizessp\let\@halignto\@empty\@tabular}
\def\endscriptsizetabular{\endtabular}
\expandafter \def\csname scriptsizetabular*\endcsname #1{\par\scriptsizessp\def\@halignto{to#1}\@tabular}
\expandafter \let \csname endscriptsizetabular*\endcsname = \endtabular
\long\def\@footnotetext#1{\insert\footins{\ssp\reset@font\footnotesize
    \interlinepenalty\interfootnotelinepenalty\splittopskip\footnotesep
    \splitmaxdepth \dp\strutbox \floatingpenalty \@MM \hsize\columnwidth \@parboxrestore
   \edef\@currentlabel{\csname p@footnote\endcsname\@thefnmark}\@makefntext
    {\rule{\z@}{\footnotesep}\ignorespaces #1\strut}}}
\def\@startsection#1#2#3#4#5#6{\if@noskipsec \leavevmode \fi
   \par \@tempskipa #4\relax \@afterindenttrue
   \ifdim \@tempskipa <\z@ \@tempskipa -\@tempskipa \relax\fi
   \if@nobreak \everypar{}\else
     \addpenalty{\@secpenalty}\addvspace{\@tempskipa}\fi \@ifstar
     {\@ssect{#3}{#4}{#5}{#6}}{\@dblarg{\@sect{#1}{#2}{#3}{#4}{#5}{#6}}}}

% ***********************************************************************
% Redefinition of main dissertation divisions, to comply with KMUTT 
% regulations.
% ***********************************************************************

%%%%%%%%%%%%%%%%%%%%%%%%% pagestyles %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\ps@plain{\let\@mkboth\markboth\def\@oddfoot{}\def\@evenfoot{}
   \def\@oddhead{\hbox{}\hfil\rm\thepage} \def\@evenhead{\rm\thepage\hfil\hbox{}}}
\def\ps@plainbottom{\let\@mkboth\markboth\def\@oddhead{}\def\@evenhead{}
   \def\@oddfoot{\hfil\rm\thepage\hfil} \def\@evenfoot{\hfil\rm\thepage\hfil}}
\ps@plainbottom

%%%%%%%%%%%%%%%%%%%%%%%%% Chapter font %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%% Chapter heading in the text for \chapter{}
\def\@makechapterhead#1{%\vspace*{.8truein}%
%  \fontsize{15}{18}{\centering{\bf \MakeUppercase{\@chapapp{}} \thechapter}\hskip 5\p@}%\vskip 20\p@
%  \fontsize{15}{18}{\centering\MakeUppercase{\bf #1}\par\nobreak\emptyline 2}}
  {\centering\MakeUppercase{\Large\bf \@chapapp{} \thechapter\hskip 5\p@ #1}\par\nobreak\vskip 30\p@ }}
%\def\@makeschapterhead#1{\vspace*{.8truein}%
%  {\centering{\large\bf #1}\par\nobreak\vskip 40\p@ }}


\def\chapter{\clearpage
%   \ifprelude \pagestyle{plainbottom} \else 
%   \pagestyle{plain}\thispagestyle{plainbottom} \fi
   \global\@topnum\z@ \@afterindenttrue
   \secdef\@chapter\@schapter}

\def\@chapter[#1]#2{\preludefalse\setarabic
%   \pagestyle{plain}\thispagestyle{plainbottom} % added in v2.4
   \pagestyle{plain}\thispagestyle{empty} % No page number in chapter.
   \refstepcounter{chapter}%
   \typeout{\@chapapp\space\thechapter.}% 
%% Put the work CHAPTER in ToC before the first chapter
%%   \iffirstchapter
%%       \addcontentsline{toc}{chapterxx}{\mdseries\bf บทที่}
%%       \firstchapterfalse
%%   \fi
%% Add the chapter heading in ToC
   \addcontentsline{toc}{chapter}{\normalsize\bf\MakeUppercase{บทที่ \tocprefix {\protect \numberline{\thechapter}\hskip -0.5em #1}}}
   \chaptermark{#1}%
   %\addtocontents{lof} {\protect\addvspace{0\p@}}
   %\addtocontents{lot} {\protect\addvspace{0\p@}}
   \addtocontents{lof} {\protect\addvspace{0em}}
   \addtocontents{lot} {\protect\addvspace{0em}}
   \pagestyle{plain}\thispagestyle{empty}
   % Must be added after addcontentsline 
   % Otherwise, the page number may not show up..
   \@makechapterhead{#2} \@afterheading}
%% Remove top space from \chapter*{}
%% Chapter heading in the text for \chapter*{}
\def\@makeschapterhead#1{%
  %\vspace*{50\p@}%
  {\parindent \z@ \centering%\raggedright
    \normalfont
    \interlinepenalty\@M
    \large \bfseries #1\par\nobreak
    \vskip 20\p@
  }}
\def\@schapter#1{\@makeschapterhead{#1} \@afterheading}

%%%%%%%%%%%%%%% Section heading fonts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
				   {0.1ex\@plus.1ex} 
                                   %{2.3ex \@plus.2ex}%
                                   {\normalfont\fontsize{12}{16.8}\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{2.5em}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {0.1ex \@plus .2ex}%
                                    {\normalfont\fontsize{11}{15.6}\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {0.1ex \@plus .2ex}%
                                     {\normalfont\normalsize\bfseries}}

%%%%%%%%%%%%%%% Table/figure caption font %%%%%%%%%%%%%%%%%%%%%%%%
\setlength\belowcaptionskip{10\p@}
\long\def\@maketablecaption#1#2{
    \global \@minipagefalse
    \hbox to \hsize{\parbox[t]{\hsize}{{\bf #1} #2 \vskip 0.5em}}}
\let\old@floatboxreset\@floatboxreset
\def\table{%
\let\@makecaption\@maketablecaption
%\def\@floatboxreset{%
% \old@floatboxreset
% \@tablesize
%}%
  \let\footnoterule\relax
  \let\contcaption\conttablecaption \@float{table}}
\def\endtable{\end@float}


\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{{\bf #1} #2}%
  \ifdim \wd\@tempboxa >\hsize
    {\bf #1} #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Define how the content lines show up in ToC when using
%%% addcontentsline{}{}{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Normal chapter %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1.0em \@plus\p@
    %\vskip 0.5em \@plus\p@    %% Space between entry in toc
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode %\bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      \bfseries #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}

%% Special lines such as abstract, acknowledgment
%% have no extra spacing between lines.
\newcommand*\l@chapterx[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 0.2em \@plus\p@    %% No spacing between lines
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode %\bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      \bfseries #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup 
  \fi}

%%% Special toc entry with no number
\newcommand*\l@chapterxx[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1em \@plus\p@ % Space between entry
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode %\bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      \bfseries #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss}\par
      \penalty\@highpenalty
    \endgroup \vskip -0.8em
  \fi}

%%% Section entries %%%%%%%%%%%%%%
\def\l@section#1#2{\addpenalty{\@secpenalty}  % good place for page break
   %\addvspace{1.0em plus 1pt}  % space above toc entry
   \addvspace{0.2em}  % space above toc entry
   \@tempdima 2em            % width of box holding section number
   \begingroup
     \parindent \z@ \rightskip \@pnumwidth 
     \parfillskip -\@pnumwidth   
     %\sc                  % Small caps
     \leavevmode          % TeX command to enter horizontal mode.       
      \advance\leftskip\@tempdima  %% added 5 Feb 88 to conform to 
      \hskip -\leftskip            %% 25 Jan 88 change to \numberline
      \hskip 1em #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
     %\hskip 2em #1\nobreak\hfil \nobreak\hbox to\@pnumwidth{\hss #2}\par
   \endgroup}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%\let\l@subsection\l@section
%% May 17, 2021
%% Add indentation to subsection in table of contents 
\def\l@subsection#1#2{ 
   %\addvspace{1.0em plus 1pt}  % space above toc entry
   \addvspace{0.2em}  % space above toc entry
   \@tempdima 3em     % width of box holding section number
   \begingroup
     \parindent \z@ \rightskip \@pnumwidth 
     \parfillskip -\@pnumwidth   
     %\sc                  % Small caps
     \leavevmode          % TeX command to enter horizontal mode.       
      \advance\leftskip\@tempdima  %% added 5 Feb 88 to conform to 
      \hskip -\leftskip            %% 25 Jan 88 change to \numberline
      \hskip 2.5em #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
   \endgroup}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%\let\l@subsubsection\l@section
%% Nov 6, 2021
%% Add indentation to subsubsection in table of contents 
\def\l@subsubsection#1#2{ 
   %\addvspace{1.0em plus 1pt}  % space above toc entry
   \addvspace{0.2em}  % space above toc entry
   \@tempdima 3.4em     % width of box holding section number
   \begingroup
     \parindent \z@ \rightskip \@pnumwidth 
     \parfillskip -\@pnumwidth   
     %\sc                  % Small caps
     \leavevmode          % TeX command to enter horizontal mode.       
      \advance\leftskip\@tempdima  %% added 5 Feb 88 to conform to 
      \hskip -\leftskip            %% 25 Jan 88 change to \numberline
      \hskip 4.5em #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
   \endgroup}
   
%%% Figure/table entries in list of figures and tables shows up
\def\l@figure#1#2{\addpenalty{\@secpenalty}  % good place for page break
   %\addvspace{1.0em plus 1pt}  % space above toc entry
  \addvspace{0.2em}  % space above toc entry
   \@tempdima 2.5em            % width of box holding section number
   \begingroup
     \parindent \z@ \rightskip \@pnumwidth 
     \parfillskip -\@pnumwidth   
     %\sc                  % Small caps
     \leavevmode          % TeX command to enter horizontal mode.       
      \advance\leftskip\@tempdima  %% added 5 Feb 88 to conform to 
      \hskip -\leftskip            %% 25 Jan 88 change to \numberline
      \hskip 0em #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
     %\hskip 2em #1\nobreak\hfil \nobreak\hbox to\@pnumwidth{\hss #2}\par
   \endgroup}
\let\l@table\l@figure

%%% Appendix content lines
\def\l@apdx#1#2{\addpenalty{\@secpenalty}  % good place for page break
   \addvspace{0.2em}  % space above toc entry
   \@tempdima 2.5em            % width of box holding section number
   \begingroup
     \parindent \z@ \rightskip \@pnumwidth 
     \parfillskip -\@pnumwidth   
     %\sc                 % Small caps
     \leavevmode          % TeX command to enter horizontal mode.       
      \advance\leftskip\@tempdima  %% added 5 Feb 88 to conform to 
      \hskip -\leftskip            %% 25 Jan 88 change to \numberline
      \hskip 2em #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
   \endgroup}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% Title page %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\faculty{}
\def\worktype{}  % Type of work..
\def\titleempty{}
\def\maketitlepage{\thispagestyle{empty}\c@page\@ne\baselineskip \baselineskipxii
   \emptyline 2 {\centering 
   \makebox{\MakeUppercase{\disstitleone}} \par
   \ifx \titleempty\disstitletwo \else  
   \makebox{\MakeUppercase{\disstitletwo}} \par
   \fi
   \vfill \MakeUppercase{\dissauthor} \par 
   
   \ifx \titleempty\dissauthortwo \else  
   \makebox{\MakeUppercase{\dissauthortwo}} \par
   \fi
   \ifx \titleempty\dissauthorthree \else  
   \makebox{\MakeUppercase{\dissauthorthree}} \par
   \fi
   \vfill
%   \emptyline 7 \MakeUppercase{\dissauthor} \par \emptyline 7
   %\makebox{\dissdiplomaone} \par \makebox{\dissdiplomatwo} \par
   %\makebox{\dissdiplomathree} \par \makebox{\dissdiplomafour} \par
    A \MakeUppercase{\worktype}\ SUBMITTED IN PARTIAL FULFILLMENT \par
   OF THE REQUIREMENTS FOR \par 
   THE DEGREE OF \MakeUppercase{\dissdegree}\ (\makebox{\MakeUppercase{\department}}) \par
   FACULTY OF \makebox{\MakeUppercase{\faculty}} \par
%   \makebox{\schoolname} in partial fulfillment \par
%   of the requirements for the degree of \par \dissdegree \par
   KING MONGKUT'S UNIVERSITY OF TECHNOLOGY THONBURI \par 
   \dissyear \vspace*{2cm}\par}
   \newpage\baselineskip \truebaselineskip}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Copyright page %%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\makecopyrightpage{\newpage
   {\centering{\vbox{}\vfill Copyright by \dissauthor\par\dissyear\par \vfill\vbox{}}}\newpage}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%% Signature page %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def\thesis{Thesis}
\def\makesignaturepage{
   \newpage\thispagestyle{empty}\baselineskip \baselineskipxi {\centering
   \makebox {\disstitleone} \par 
   \ifx \titleempty\disstitletwo \else  
   \makebox{\disstitletwo} \par
   \fi
   %\makebox {\disstitletwo} \par
   %\makebox {\disstitlethree} \par \makebox {\disstitlefour} \par
   \vfill \dissauthor\ \par 
   \ifx \titleempty\dissauthortwo \else  
   \makebox{\dissauthortwo} \par
   \fi
   \ifx \titleempty\dissauthorthree \else  
   \makebox{\dissauthorthree} \par
   \fi
   \vfill A \worktype\ Submitted in Partial Fulfillment \par
   of the Requirements for \par
   the Degree of \dissdegree \ (\department) \par
   Faculty of\ \makebox{\faculty} \par
   King Mongkut's University of Technology Thonburi \par 
   \dissyear \par}
 \emptyline 1
\begin{flushleft}
\worktype\ Committee \par\par
\begin{tabular*}{\textwidth}{@{}c@{\extracolsep{1.2cm}}l@{}}
   & \\
%%%%% Thesis or project advisor %%%%%%%%
  \dotrule{3.6in} & \worktype\ Advisor\\
  (\dissadvisor) & \\
   & \\ 
%%%%%%% Co-advisor %%%%%%%%%%%%%%%%%%
\ifx \titleempty\disscoadvisor \else
  \dotrule{3.6in} & \worktype\ Co-Advisor\\
  (\disscoadvisor) & \\
  & \\
\ifx \titleempty\disscoadvisorr \else
  \dotrule{3.6in} & \worktype\ Co-Advisor\\
  (\disscoadvisorr) & \\
  & \\
\fi
%%%%%%% 2nd committee %%%%%%%%%%%%%%%%%%
  \dotrule{3.6in} & Committee Member \\
  (\disscommitteetwo) & \\
   & \\
%%%%%%% 3rd committee %%%%%%%%%%%%%%%%%%
\ifx \titleempty\disscommitteethree \else
  \dotrule{3.6in} & Committee Member \\
  (\disscommitteethree) & \\
  & \\
\fi
%%%%%%%% 4th committee %%%%%%%%%%%%%%%%
\ifx \titleempty\disscommitteefour \else
  \dotrule{3.6in} & Committee Member \\
  (\disscommitteefour) & \\
   & \\
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\end{tabular*}
\end{flushleft}
\begin{center}	
\vspace*{\fill}Copyright reserved
\vspace*{\fill}
%\vfill Copyright reserved
\end{center}	
\newpage\baselineskip \truebaselineskip}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%% English Abstract %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\abstract{
\newpage
\setcounter{page}{2}
\pagestyle{plain}%\thispagestyle{empty}
\addcontentsline{toc}{chapterx}{\mdseries ABSTRACT}
\begin{flushleft}
\begin{tabular}{@{}lp{0.7\textwidth}}
 \worktype\ Title & \disstitleone\ \\ 
\ifx \titleempty\disstitletwo \else
              & \disstitletwo \\
\fi
Credits & \disscredit \\
 Member(s) & \dissauthor \\
\ifx \titleempty\dissauthortwo \else
              & \dissauthortwo \\
\fi
\ifx \titleempty\dissauthorthree \else
              & \dissauthorthree \\
\fi
\worktype\ Advisor & \dissadvisor \\
\ifx \titleempty\disscoadvisor \else
     Co-Advisor      & \disscoadvisor \\
           & \disscoadvisorr \\
\fi
 Program & \dissdegree \\
 Field of Study & \fieldofstudy \\
 Department & \department \\
 Faculty & \faculty \\
 Academic Year & \dissyear 
\end{tabular}
\end{flushleft}
%}
\emptyline 1
\begin{center} 
  \textbf{Abstract}
\end{center}
\par
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%% Thai Abstract %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\thaiabstract{
\newpage
\addcontentsline{toc}{chapterx}{\mdseries บทคัดย่อ}
\begin{flushleft}
\begin{tabular}{@{}lp{0.7\textwidth}}
 \textthai{หัวข้อ­}\thaiworktype & \thaidisstitleone\ \\ 
\ifx \titleempty\thaidisstitletwo \else
              & \thaidisstitletwo \\
\fi
 \textthai{หน่วยกิต} & \textthai{\disscredit} \\
 \textthai{ผู้เขียน} & \thaidissauthor \\
 \ifx \titleempty\thaidissauthortwo \else
              & \thaidissauthortwo \\
\fi
\ifx \titleempty\thaidissauthorthree \else
              & \thaidissauthorthree \\
\fi
 \textthai{อาจารย์ที่ปรึกษา} & \thaidissadvisor \\
 \ifx \titleempty\disscoadvisor \else
     & \thaidisscoadvisor \\
 \ifx \titleempty\disscoadvisorr \else
     & \thaidisscoadvisorr \\

\fi
 \textthai{หลักสูตร} & \thaidissdegree \\
 \textthai{สาขาวิชา} & \thaifieldofstudy \\
 \textthai{ภาควิชา} & \thaidepartment  \\
 \textthai{คณะ} & \thaifaculty  \\
 \textthai{ปีการศึกษา} & \textthai{\thaidissyear} 
\end{tabular}
\end{flushleft}
%}
\emptyline 1
\begin{center} 
  \textthai{บทคัดย่อ}
\end{center}
\par
}
\def\endabstract{\newpage}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%% Acknowledgement %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\preface{\chapter*{\large กิตติกรรมประกาศ}%
\addcontentsline{toc}{chapterx}{\mdseries กิตติกรรมประกาศ}
\thispagestyle{plain}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%% Content page %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Table of contents
\setcounter{tocdepth}{5}  % must be same as secnumdepth
\def\contentsname{สารบัญ}
\def\tableofcontents{\chapter*{\large\MakeUppercase{\contentsname}\@mkboth{}{}%
 \\ \emptyline 1 \hfill\textbf{หน้า}\\[-0.4em]}
% 23 Nov 2021, Thanin
% put \addcontentsline before \ssp\@starttoc to fix wrong numbering
\addcontentsline{toc}{chapterx}{\mdseries สารบัญ}
{\ssp\@starttoc{toc}}
\pagestyle{plain}\thispagestyle{plain}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%% List of table page %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% List of tables
\def\listtablename{สารบัญตาราง}
\def\listoftables{\chapter*{\large \MakeUppercase{\listtablename}\@mkboth{ตารางที่}{หน้า}\thispagestyle{plain}
\\ \emptyline 1 \normalsize\textbf{ตารางที่}\hfill\textbf{หน้า}\\[-0.4em] }
   \addcontentsline{toc}{chapterx}{\mdseries สารบัญตาราง} {\ssp\@starttoc{lot}}}
%\def\l@table{}
%\def\l@table{\vskip 1.0em plus\p@\@dottedtocline{1}{1.5em}{2.3em}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% List of figure page %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\listfigurename{สารบัญรูปภาพ}
\def\listoffigures{\chapter*{\large\MakeUppercase{\listfigurename}\@mkboth{รูปที่}{หน้า}\thispagestyle{plain}\\
   \emptyline 1
   \normalsize\textbf{รูปที่}\hfill\textbf{หน้า}\\[-0.4em]  }
   \addcontentsline{toc}{chapterx}{\mdseries สารบัญรูปภาพ} {\ssp\@starttoc{lof}}}
\let\l@figure\l@table

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% List of symbol page %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\listofsymbols{\chapter*{\large สารบัญสัญลักษณ์}
%\\ \emptyline 1 \textbf{SYMBOL}\hfill\textbf{UNIT}\\[-1cm]}
\addcontentsline{toc}{chapterx}{\mdseries สารบัญสัญลักษณ์}\thispagestyle{plain}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% List of vocab page %%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\listofvocab{\chapter*{\large สารบัญคำศัพท์ทางเทคนิคและคำย่อ}%
\addcontentsline{toc}{chapterx}{\mdseries สารบัญคำศัพท์ทางเทคนิคและคำย่อ}\thispagestyle{plain}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% Appendix pages %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\firstappendixtrue
\def\appendixnames{ภาคผนวก} % assume only one appendix
\def\appendixcover#1{%
\newpage\pagestyle{plain}\thispagestyle{empty}
\iffirstappendix %
  \setcounter{chapter}{0} % Reset chapter numbering
  \setcounter{figure}{0}  % Reset figure numbering (May 2022 by Thanin)
  \renewcommand{\thechapter}{\Alph{chapter}}
  \def\@chapapp{\MakeUppercase{\appendixname}}%
  \addcontentsline{toc}{chapter}{\mdseries\bf \MakeUppercase{\appendixnames}}%
  \firstappendixfalse% 
\fi 
   \setcounter{equation}{0} % Reset equation numbering
   \setcounter{figure}{0} % Reset figure numbering (May 2022 by Thanin)
   \addtocounter{chapter}{1}  % Start the 1st appendix 
   {\centering{\vbox{}\vfill \MakeUppercase{\LARGE \bf
    ภาคผนวก \thechapter} \par \bigskip \MakeUppercase{\Large #1} \vfill\vbox{}}}\newpage}
%   {\centering{\vbox{}\vfill \MakeUppercase{{\normalsize\bf APPENDIX
%\thechapter}} \par \MakeUppercase{#1}} \vfill\vbox{}}}\newpage}

\def\appendix#1{% 
\appendixcover{#1}
\addcontentsline{toc}{apdx}{\thechapter\hskip 1em #1}%
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%% Bibliography page %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\refname{บรรณานุกรม}
\def\referencepage{\chapter*{\large\bf \MakeUppercase{\refname} \\
\emptyline 1}%
\addcontentsline{toc}{chapter}{\mdseries\bf \MakeUppercase{\refname}}\thispagestyle{empty}
}
%\def\bibliographycover{\newpage \typeout{\bibname .} \thispagestyle{empty}
%   {\centering{\vbox{}\vfill {\LARGE\bf \bibname} \vfill\vbox{}}}\newpage}
%%% Change the brackets to dot around bib number.%%%%%%%%%%%%%%
\newdimen\bibindent
\bibindent=2em
\def\@biblabel#1{#1.}
\def\thebibliography#1{%\bibliographycover
  %\chapter*{\bibname\@mkboth{}{}}
  %\addcontentsline{toc}{chapter}{\bibname} \ssp
  \referencepage \vspace*{-30\p@}\ssp\pagestyle{plain}	
  \list{\@biblabel{\arabic{enumiv}}}{\settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth \advance\leftmargin\labelsep
    \usecounter{enumiv} \let\p@enumiv\@empty
    \def\theenumiv{\arabic{enumiv}}}%
    \def\newblock{\hskip .11em plus.33em minus.07em}%
    \sloppy\clubpenalty4000\widowpenalty4000 \sfcode`\.=\@m }
\def\endthebibliography{\ifdraftmode \dsp \fi
  \def\@noitemerr{\@warning{Empty `thebibliography' environment}} \endlist}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Vitae %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\vitae{
\clearpage
\chapter*{\large\bf CURRICULUM VITAE}%
\vspace*{-5\p@}\ssp
\addcontentsline{toc}{chapter}{\normalsize\bf CURRICULUM VITAE}
\pagestyle{plain}\thispagestyle{plain}
}

% ************************************************************
% personal stuff

%\input latexsym.sty
\usepackage{latexsym}

\newcounter{definition}[chapter]
\newenvironment{definition}[1]{\refstepcounter{definition}
   \par\hbox{}\par\noindent
   {\bfseries Definition \thechapter.\thedefinition\ #1}
   \par\noindent\ignorespaces}
   {\par\hbox{}\par}

\newenvironment{proof}{
   \par\noindent{\bfseries Proof: }\ignorespaces}
   { $\Box$\par\hbox{}\par}

% *******************************************************************
\endinput

