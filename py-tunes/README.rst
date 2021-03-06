py_tunes
========

py_tunes provides access to the iTunes music library and application.

Controlling iTunes
------------------
The py_tunes.ITunesApp class can be used to play items, pause, adjust the volume,
configure shuffling, seek within a track, move between tracks, and so on.

Reading the iTunes Library
--------------------------

Assuming an index has been generated (in ~/Library/Caches/py_tunes/itunes.sqlite3),
an instance of py_tunes.ITunesLibrary can be used to read the iTunes library. It
is a fairly thin wrapper over a SQLAlchemy session, so querying is similar.

Indexing
--------
Since the iTunesLibrary framework requires a code signed application or executable,
py_tunes does not access it directly. Instead, it reads from a SQLite database
generated by `an Objective-C program`_. Running this program
from Python causes issues with OS X's entitlements system, so it is distributed
and run separately.

.. _an Objective-C program: https://github.com/roguePanda/itunes-remote/tree/master/itunes-indexer
