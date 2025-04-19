Moving to a new country can be an exciting and daunting experience in equal measure. The new language, culture and cuisine can be tantalizing to some and yet disorienting to others.

​

Given that living in different cities around the world is a central part of the Minerva experience, your task in this assignment is to develop an expert system (as introduced in week 12) that can be used to help students living in your rotation city or cities for the first time to make their way around the city. You may be freely creative in deciding what your expert system will focus upon, but it should allow students to quickly locate what they are looking for by answering a series of questions, following the paradigm of expert systems discussed during class. It should also be readily testable by visiting one or more places around the city (more on this below). Some ideas could include:

An expert system to recommend local restaurants to hungry students, taking into account the type of cuisine, budget, distance from the residence hall and dietary restrictions.
An expert system to recommend local tourist attractions, considering distance, time, type and budget.
An expert system to recommend local bars or nightclubs, considering distance, time, budget and vibe.
​

Assignment Instructions - Basic Requirements

​

​

In groups, you are required to do the following:

Detail on what your expert system will focus upon, and what the askables will be. You need to have a minimum of 8 askables in your expert system, regardless of the domain of your KB. [#rightproblem]
Perform data collection for building your expert system by surveying resources available online, guided by the askables that you have chosen. [#evidencebased, #sourcequality].
Explain the logic of your expert system by showing which values of the askables lead to what specific information being provided to the end user. Any visualization that makes the logic of your expert system clear is acceptable (for example, a tree diagram or table). [#ailogic]
Using this visualization to help you, code your expert system using either a native Prolog front-end, or one using the PySWIP library to interface a Python frontend. [#aicoding]
Demonstrate and document the performance of your expert system for at least 3 different test cases. [#modeling].
For at least one of the test cases, visit the location recommended by your expert system and comment on how well it performed in real life. Take a selfie of your group at the location to prove that you went there [#evidencebased].
​

Possible Extensions

​

Include menu-based responses, rather than simple yes/no queries. Further extend this to providing a numbered list so that users can simply enter the option number rather than having to type in the full word for the option. [#aicoding].
Present queries to the user in more natural language than simply a query of the form "attribute is value". [#ailogic, #aicoding]. DCG's in Prolog may be helpful for this.
Design a graphical user interface rather than a text-based one. However, note that your interface must still be dynamic - you have to ask the user only relevant questions based on answers received previously. Simply having a series of checkboxes on a form will not suffice, since some of those options would be irrelevant given answers to previous questions from the user. This is not a trivial extention, since you will either need to use multi-threading or have a suitable front-end / back-end architecture to allow PySWIP to run while keeping the user interface responsive. [#aicoding]
​

Report

​

[#professionalism]

In your groups, prepare a short report of maximum length 5 pages (excluding references and appendices) detailing your solution to the assignment. In addition to the basic requirements:

Detail briefly the contribution of each group member to the assignment.
List any references you used when building your expert system.
Provide an HC / LO appendix that describes how you applied the HCs and LOs tagged for each task, in addition to any others that you used.
Include your Prolog / Python code as an appendix.
Include an AI statement describing in detail how you applied any AI tools in your submission.
​

Submission Instructions

​

Submit your group’s report in PDF format, and submit your code as a secondary file. It is important to submit a PDF so that comments can be tagged in the appropriate places on the report.

​
