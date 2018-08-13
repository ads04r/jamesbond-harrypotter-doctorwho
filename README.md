jamesbond-harrypotter-doctorwho
===============================

You've not made it in the UK unless you've been in at least one of the above.
Bonus points for a Downton Abbey appearance.

What the hell is this?
----------------------

A while back, some friends of mine and I decided that James Bond, Harry Potter
and Doctor Who are basically the 'standards' of British entertainment. Each
of these franchises has featured pretty much anyone who's anyone over the years,
and it helps that two of them have been running for over 50 years each. We
were interested to discover who (if anyone) has been in all three, and who is
the most prevalent among the rest. So I wrote a Python script that queries IMDB
to cross-compare the three.

Of course it's not all that straightforward... Doctor Who has three entries in
IMDB, one for the 1963-1989 run, one for the 1996 movie and one for the current
run that's been on the telly since 2005. Harry Potter features eight movies, and
the number of Bond movies is always increasing. Not to mention Never Say Never
Again and the original Casino Royale... do they count? :)

Usage
-----

* The script 'jbhpdw.py' does all the work, and spits out a JSON file.

* Pipe this JSON into report.py to generate an HTML table ready to copy/paste
  into a blog post.

* output.json and report.html are the outputs of the previous two files,
  respectively, as of 2014.

