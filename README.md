rng
===

RNG means Rng is Not Graphical

Overview
--------

RNG will provide a natural language as interface of common daily tasks. For instance, saving notes, passwords, and more complex tasks such as accessing web based calendar and putting reminders there.
We will offer a console-like interface.

Motivation
----------

There are many situations when we need to save notes, ito access certain information and we don't have a proper tool. Moreover, if you love console-like administration, you will love this app.

Proposed examples
-----------------

First, you must to open RNG console


* Add simple note
```
$ in notes add new one
... enter note: <something here>
... saved
```

* Get all notes
```
$ in notes get all
1. The blue dog in the garden
2. This number is useful: 414213562
```

* Add calendar event (app might be connected to google calendar)
```
$ in calendar add new event for next sunday
... enter title: Football match
```

* Get next calendar events
```
$ in calendar get next events
1. Friday: some event
2. Sunday: Footbal match
```

* And a big etcetera

Plugins architecture
--------------------

RNG will be compounded by plugins. In previous examples, they should be: Calendar Plugin, Passwords Plugin, Notes Plugins.
People could write their own plugins thanks to an uniform and extensible interface.

*Work in progress*

