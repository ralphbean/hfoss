Notes for Class Sessions
========================

Week 02, Day 1:  First Flight
-----------------------------

 - Introductions
 - Covering the Syllabus
 - Discussing Open-Advice on Community Building
 - Discussing PyCon Videos
 - Introduction to ``git`` by ryansb from http://ryansb.com/seminars/git
 - :doc:`hw/fflight`


Week 02, Day 2:  Introduction to Python
---------------------------------------

 - Lightning Talks!!!
 - More ``git`` with ryansb and http://ryansb.com/seminars/git
 - Introduction to Python (check out http://learnpythonthehardway.org/book/)

   - basic operators
   - strings
   - formatting
   - multiplying strings
   - lists
   - dicts
   - conditionals
   - boolean trickery, not and in
   - any and all
   - while loops
   - continue
   - break
   - for loops
   - functions
   - args and kwargs
   - whitespace

Week 03, Day 1:  Intermediate Python
------------------------------------

 - :doc:`hw/fflight` is due.  How'd it go?
 - Other business
 - Intermediate Python

   - stdlib

     - argparse
     - urllib2
     - itertools

   - virtualenv
   - setup.py
   - sweet modules on pypi

     - shelve
     - fabulous
     - nose
     - sqlalchemy

   - zip
   - map
   - filter
   - list comprehensions (!)
   - generators
   - decorators
   - classes
   - dunder methods (reference, http://www.siafoo.net/article/57)
   - context managers
   - multiple inheritance

Week 03, Day 2:  So-called "Advanced" Python
--------------------------------------------

 - Announcements

   - The `planet <http://threebean.org/floss-planet>`_ is up.  Subscribe to it
     with your RSS reader.
   - Homework 2 is due on Monday.  Good to go?
   - Special guest `Luke Macken <http://lewk.org>`_!

 - Lightning Talks!!!
 - Advanced Python

   - context managers revisited

     - https://github.com/ralphbean/pyrasite/commit/cdca3dfc4b757249d50fcc2ab6fc7de6d40dc0f5

   - locals() and globals()
   - the inspect module

     - docstrings and 'help'
     - inspect.stack
     - inspect.getsource

   - the abstract syntax tree

     - desmaj's tool
     - macchiato

   - synthesizing stuff

     - getattr and __getattr__, two sides of the coin

   - metaclasses

Week 04, Day 1:  OLPCs!!!
-------------------------

 - Homework 2 is due.  How did it go?
 - There is a TA for the class; Nate Case.
   ``qalthos`` in IRC or qalthos ~@~ gmail.com
 - OLPC Distribution

   - I need your DCE name.
   - These must be returned at the end of the quarter under penalty of death.

 - OLPC Smoke Test

   - http://wiki.laptop.org/go/Smoke_test/10.1.x/1_hour_smoke_test
   - The one exception to the smoke test is that you need to
     use ``connect-rit`` in the terminal activity to connect
     to ``ritwpa2``.  Just open the terminal activity and run
     ``./connect-rit``.  Each XO should have it.
   - **Oh no!** the ``connect-rit`` script is busted!

     - If this is the case for you, you can get a new copy of it from
       https://github.com/Qalthos/connect-rit -- Use a USB key to transfer it
       to the OLPC.

Week 04, Day 2:  Sugar
----------------------

 - Lightning Talks
 - Announcements

   - Project pitches are due on Monday

 - Introduction to Sugar

   - Reading you can do later if you want more detail:

     - http://en.flossmanuals.net/make-your-own-sugar-activities
     - http://wiki.laptop.org/go/Understanding_Sugar_code

   - Sugar concepts

     - Journal
     - Different Views
     - Sandboxing, not signing.

   - You can bust out ``/usr/bin/sugar-session`` (
     http://git.sugarlabs.org/sugar/mainline/blobs/master/bin/sugar-session or
     http://gist.github.com/2297065 for a syntax-highlighted version)

     - ``ps -ef | grep sugar``
     - ``sudo yum -y install vim``
     - ``vim /usr/bin/sugar-session`` and you'll see:

       - A lot of ``from sugar import env, logger``
       - And some ``from jarabe import model, view, keyhandler``

   - Check out http://git.sugarlabs.org for the big `tamale`.

   - What is an activity?

     - A MANIFEST file.
     - ``activity.info`` with metadata
     - A .svg icon
     - Translation files
     - The source code (you'll need a class that extends ``Activity``)

   - For an example, let's take a look at Fortune Hunter,
     http://git.sugarlabs.org/project-xavier/mainline/trees/master/MAFH.activity

   - What modules to use when writing your code?  You can use either of the
     following.  They will both be installed on whatever XO your activity
     makes its way to.

     - PyGTK - http://www.pygtk.org/tutorial.html
     - pygame - http://www.pygame.org/wiki/tutorials


Week 05, Day 1:  Projects
-------------------------

 - Lightning Talks
 - Introduction to Sugar
