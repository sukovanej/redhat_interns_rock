Hi! My name is Chris Ward.  I'm working on a data mining, 
analytic's and communications related projects at Red Hat. 

If you are reading this, it likely means I've seen your CV 
and believe you could be a great match for type of work my 
team is looking for some help with.

The following is a simple homework assignment I've cooked up 
for you to demonstrate your Python skillz and general 
ambitions to impress me and other folks here at Red Hat.

If you're interested, please fork this repo and solve the
following problem as best as you can within 24 hours of
forking the repo.

Ping me with a 'pull request' when your solution is ready 
for review. 

Assignment:: 

    Write a single python 2.7 compatible class that is capable 
    of generating an arbitrary data structure filled with 
    (pseudo)random string data inside it, with a special 
    string hidden somewhere (pseudo)randomly inside.

    Write tests that can be run to verify all Requirements 
    have been met, automtically.
            
Requirements::

    * The special string 
     + must be 'I am Red Hat'
     + must live >= 3 (nested) levels deep within 
       the data structure

    * The nested data structure must be made up of >= 1 "container" instances:
      + *Mapping (eg, dict)
      + *Sequence (eg, tuple)

    * Each node within the data structure must have either 2 or 4 
      branches/sub-nodes

    * The data structure should be no more than 5 (nested) levels deep

    * The output must be in the form of a JSON compatible string dump

Example execution::

    $> python assignment.py 
    {
        "BCAYP": {
            "84": 85,
            "MRWM?": {
                "68": "I am Red Hat",
                "98": [
                    "IZHIZ",
                    [
                        ">UJJJ",
                        "U@NJ@",
                        "[45GG",
                        "53",
                    ]
                ]
            },
            "RRSBM": 61,
            "26": "SDFFF"
        },
        "94": "LPTVR"
    }

    $> py.test tests.py
    ==================== test session starts =====================
    platform linux2 -- Python 2.7.8 -- py-1.4.26 -- pytest-2.7.0
    rootdir: /home/$HOME/repos/redhat_interns_rock, inifile: 
    collected 8 items 

    tests.py ......

    ================= 8 passed in 0.83 seconds ==================


--------------------------------------------

If you have any questions, file an issue in GitHub. 

Looking forward to hearing from you! Good luck!

-Chris <cward@redhat.com>
