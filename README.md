# bioinformatics 2017-2018

Branch|[![Travis CI logo](TravisCI.png)](https://travis-ci.org)
---|---
master|[![Build Status](https://travis-ci.org/richelbilderbeek/bioinformatics_2017_2018.svg?branch=master)](https://travis-ci.org/richelbilderbeek/bioinformatics_2017_2018)

Practical Informatics for Biologists is a course at the University of Groningen 2017-2018.

## Schedule

Time|What
---|---
9:30-10:30 | git & GitHub #1
10:30-10:45 | Break
10:45-11:30 | git & GitHub #2
11:30-11:45 | Break
11:45-12:30 | Travis CI #1
12:30-13:30 | Lunch
13:30-14:30 | discuss problem iff any + prepare presentations
14:30-14:45 | Break
14:45-15:30 | Prepare presentations

First lecture starts *sharply* at the time indicated.

## Teaching goals

 * git & GitHub #1: 
    * how does `git` help you become a better scientist?
    * how does GitHub help you become a better scientist?
    * how today works
    * practice the workflow: correct_cpp_scoreboard
 * git & GitHub #2: 
    * practice the workflow: correct_cpp_hello
    * what is a merge conflict?
 * Travis CI #1: 
    * how does Travis CI help you become a great scientist?

## Submitting your grade

 * Fork this repo
 * Modify the file called `grade_me.txt`:
    * `ownername`: the owner of the repository
    * `reponame`: the name of the repository
    * `committername`: your name
 * Create a Pull Request. If your Pull Request improves this repository, mention it in the commit message
 * Check the Travis build log, as it contains your grade
 * If Travis CI gives an incorrect grade (it can be fooled), add this as a comment

If Travis CI gives a too high grade of `X` points, and a human finds out, the grade is reduced by `2X`.

Unless you improve this repository, your Pull Request will be rejected, to keep `grade_me.txt` intact.

## Grading exercise git and GitHub 

#|Exercise|Information
---|---|---
1|Do correct_cpp_scoreboard|[correct_cpp_scoreboard](https://github.com/richelbilderbeek/correct_cpp_scoreboard)
2|Do correct_cpp_hello|[correct_cpp_hello](https://github.com/richelbilderbeek/correct_cpp_hello)
3|Create a README.md file for your research | [GitHub article: create a README.md](https://help.github.com/articles/about-readmes/)
4|Show a picture (`jpg`, `png`, `gif`, `jpeg`) in the README.md of your GitHub|[GitHub guide: mastering Markdown](https://guides.github.com/features/mastering-markdown/)
5|Link to a presentation or documentation (`pdf`, `ppt`, `pptx`, `doc`, `docx`) in the README.md of your GitHub|[GitHub article: basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/#relative-links)
6|Travis calls proselint on README.md|[Minimal example](https://github.com/richelbilderbeek/travis_proselint)
7|Travis checks for broken links|[Minimal example](https://github.com/richelbilderbeek/travis_markdown-link-check)
8|Travis checks your last Python exercise's result to have a correct answer | [introduction](https://medium.com/ellisonleao/an-introduction-to-git-github-and-travis-ci-for-version-control-and-testing-ac97f158f520)
9|More then 250 commits | [set up git](https://github.com/richelbilderbeek/correct_cpp/blob/master/doc/set_up_git.md)
10|Fix a bug in this course I was unaware of, using a Pull Request to this repo | Read the `test` and `functions` file, add both a positive and negative control

Your grade will equal the number of exercise you did, with a minimum grade of 1.

Your grades are determined using Travis CI for points 1-9 and a human for point 10.

Deadline for these exercises are Friday the 26th January 2018 at 17:00.

Grades will be entered before Sunday 28th January 17:00.

## External links

 * [git and GitHub](https://github.com/richelbilderbeek/CppPresentations/blob/master/Git.pdf) by Richel Bilderbeek
 * [Correct C++](https://github.com/richelbilderbeek/correct_cpp) by Richel Bilderbeek, course with many guides how to use git, GitHub
 * [An introduction to Git, GitHub and Travis CI for version control and testing for Python](https://medium.com/ellisonleao/an-introduction-to-git-github-and-travis-ci-for-version-control-and-testing-ac97f158f520) by Ellison Leao
 * [Simplify C++ article about Travis CI](https://arne-mertz.de/2017/04/continuous-integration-travis-ci) by Richel Bilderbeek
 * [SDJ articlice about Travis CI and R](https://github.com/richelbilderbeek/sdj_raising_your_code_to_professional_standards), by Richel Bilderbeek
 * [CppCast episode 103: Travis CI with Richel Bilderbeek](https://www.youtube.com/watch?v=p30AA9JLVJY) by Jason Turner and Rob Irving
 * [C++ Weekly, episode 79: Intro To Travis CI](https://www.youtube.com/watch?v=3ulKzD2cmSw) by Jason Turner
 * [Example of data analyis redone, with different conclusions](https://github.com/richelbilderbeek/Bolnick_and_Stutz_2017)
