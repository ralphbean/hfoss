Syllabus
========

Projects Seminar in FLOSS Game Development
------------------------------------------

 - Syllabus - http://hfoss.rtfd.org/ -- (subject to change)
 - Course Number - 4080.445.01
 - Room - Room 2435, Golisano Building
 - Monday, Wednesday -- 10:00am-12:00noon
 - Instructor - Ralph Bean <rjbpop@rit.edu>

   - Office:  The Center for Student Innovation
   - Office Hours:  Monday, Wednesday, 12:00-1:00pm

 - IRC - irc.freenode.net, ``#floss-seminar``
 - Email list - `floss-seminar@lists.rit.edu
   <https://lists.rit.edu/mailman/listinfo.cgi/floss-seminar>`_
 - Blog Planet - http://threebean.org/floss-planet
 - The source for this syllabus can be found at
   http://github.com/ralphbean/hfoss

Text Books
----------

There is one textbook we'll be referencing throughout the quarter.  You can
download it for free from http://open-advice.org

What You'll Do
--------------

This course will introduce students to the Free and Open Source Software (FOSS)
and Open Content movements, to the open source development process,
and to the open questions of the efficacy of technology in the classroom.

Students will learn FOSS process and Tools with class projects that support
the One Laptop Per Child community by creating content and
software for free distribution to students and teachers around the world.
The OLPC project is driven by a world-wide community.

For this course students will be expected to attend and make final
presentations to the RIT and Rochester FOSS communities via the irregular
Rochester Pythonistas meet-ups and FOSSBox hack-a-thons when possible.
Students will also become members of the Sugar and OLPC international
communities. Local FOSS community members may join us in class sessions as
well.  Treat them as you would another instructor, but they’re also your
peers in moving this innovative project forward.

The spirit of the course
------------------------

While still a course where you will receive a letter grade, the spirit of the
course is intended to be both `open` and `fun`.

An `open` course -- students will have access to the 'document source' for the
syllabus.  While you are reading `the syllabus` right now,
as a student of the class you have a right to `fork the upstream repository
<http://github.com/ralphbean/hfoss>`_, make modifications,
and submit patches for review.  Barring a troll festival, this can create a fun,
dynamic environment in which the course curriculum can develop by the very same
mechanism being taught during the quarter (community-driven).

Licensing
---------

All code developed by students in the course must be licensed (by the student)
under any one of the `licenses approved by the open source initiative
<http://www.opensource.org/licenses/category>`_.

Your code that you write is your code, with which you can do what you will;
true.  However, if you're unwilling to license code you write for an open source
course with an open source license, you're in the wrong course.

Schedule
--------

+----+---+----------------------------+-------------------+-------------------+
|Week|Day|Topic                       | Assigned          | Due               |
+----+---+----------------------------+-------------------+-------------------+
|1   |1  | Meet online.  Introductions|                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Doh!                       |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|2   |1  | Go over the syllabus.      | :doc:`hw/fflight` |                   |
|    |   | Discuss open-advice and    |                   |                   |
|    |   | PyCon videos.              |                   |                   |
|    |   | Introduction to git.       |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |   | Lightning Talks.           |                   |                   |
|    |2  | Introduction to Python     |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|3   |1  | Intermediate Python        | :doc:`hw/bugfix`  |:doc:`hw/fflight`  |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | "Advanced" Python          |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|4   |1  | Git Seminar.               | :doc:`hw/stest`   |:doc:`hw/bugfix`   |
|    |   | OLPC Distribution.         |                   |                   |
|    |   | OLPC Smoke Test.           |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | Introduction to Sugar      |                   |:doc:`hw/stest`    |
+----+---+----------------------------+-------------------+-------------------+
|5   |1  | Project Choices and Teams  | :doc:`fnl/project`|                   |
|    |   | http://bit.ly/AeDmaK       |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | In class development.      |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|6   |1  | User Testing               |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | In class development.      |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|7   |1  | User Testing               |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | In class development.      |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|8   |1  | User Testing               |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | In class development.      |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|9   |1  | User Testing               |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Lightning Talks.           |                   |                   |
|    |   | Crunch Time.               |:doc:`fnl/present` |                   |
+----+---+----------------------------+-------------------+-------------------+
|10  |1  | Crunch Time.               |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Final Presentations        |:doc:`fnl/assmnt`  |:doc:`fnl/present` |
|    |   |                            |                   |:doc:`fnl/project` |
+----+---+----------------------------+-------------------+-------------------+
|11  |?  | Return the OLPCs           |                   |:doc:`fnl/assmnt`  |
+----+---+----------------------------+-------------------+-------------------+

Grading
-------

Assignments are due at midnight of the day they are marked as due.

Late submissions will be deducted 10% per day they are late.

----

Your final grade for the quarter will be derived from the following weights.

+--------------------------------------------------------+--------------+
| Component                                              | Weight       |
+========================================================+==============+
|In-Class Participation                                  | 15%          |
+--------------------------------------------------------+--------------+
|FLOSS Dev Practices (Blogging, patching, writing, IRC)  | 25%          |
+--------------------------------------------------------+--------------+
|Team Peer Assessment                                    | 20%          |
+--------------------------------------------------------+--------------+
|Completed Project                                       | 20%          |
+--------------------------------------------------------+--------------+
|Final Presentation                                      | 20%          |
+--------------------------------------------------------+--------------+

----

*Blog updates* -- students are required to keep a blog to which they post updates
about their investigations, progress, success, and pitfalls.  This blog can be
hosted anywhere, but must be added to the course `planet
<http://threebean.org/floss-planet/>`_ (there are instructions on how to do this
in :doc:`hw/fflight`).

 - You must make at least one blog post per week to receive full credit.
 - You must participate regularly in the course's IRC channel: asking and
   answering questions.
 - You must participate in the course's mailman list,
   `floss-seminar@lists.rit.edu
   <https://lists.rit.edu/mailman/listinfo.cgi/floss-seminar>`_.
 - Contributions to the course curriculum, syllabus, and rubric are factored in
   here as well.

Blogging is good for you and good for the `FLOSS community at large
<http://xkcd.com/979/>`_.

Lightning Talks - Extra Credit
------------------------------

Every Wednesday for the first portion of class, any student has the opportunity
to give a `lightning talk <http://en.wikipedia.org/wiki/Lightning_Talk>`_ on a
topic of their chosing.  Your lightning talk must be less than 5 minutes in
length and must be at least remotely related to the course material.

You will receive +1 extra credit points towards your final grade for every
lightning talk you give.  Only the first three lightning talks offered will be
allowed during a given class.  Talks will be chosen from among those offered by
students on a FIFO basis.
