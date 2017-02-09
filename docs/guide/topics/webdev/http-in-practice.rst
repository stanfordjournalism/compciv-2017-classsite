****************
HTTP in Practice
****************

Understanding the HTTP

HTTP and the World Wide Web is a rightfully complex topic, much too big for this class to adequately cover.

In fact, even students in Stanford computer science program fail to understand its basics; here's a well-known example of a question that any 8-year-old today could figure out by Googling:

Q: Setting User-Agent Field? https://groups.google.com/forum/#!msg/comp.lang.java/aSPAJO05LIU/ushhUIQQ-ogJ



Tools
=====

This guide assumes you're familiar with these 3 ways of accessing a URL on the Internet, in ascending order of granularity:


Using your web browser:



Programmatically, such as using the


via ``curl``:

.. code-block:: shell

    $ curl http://www.example.com






What is a webpage?
==================

Since the nature of computing is ``1``s and ``0``s, it should logically follow that a webpage is made up of discrete elements. But -- because web browsers do their job so well, hence their world-changing impact -- we generally think of a web page as a monolithic, analog, and immutable *experience*.

That is, the webpage is the webpage. It's like when public information officers give you a PDF or printout of a spreadsheet, instead of the spreadsheet itself, because they fear how a spreadsheet can be "edited".

Via the New York Times: "Data on Fees to Doctors Is Called Hard to Parse"

http://www.nytimes.com/2010/04/13/business/13docpay.html

    Among the four leading drug companies making physician payment disclosures, Mr. Coukell said, Eli Lilly, which was the first to disclose, presents data as an Adobe Flash image, which he said was impossible to download or to sort. “They’ve gone out their way, I think, to present it as a Flash document,” Mr. Coukell said.

    Mr. Dunston said Obsidian had to retype all the Lilly data.

    Carole Puls, a Lilly spokeswoman, said the company purposely made its report impossible to download "to protect the integrity of the data." Lilly was concerned someone could change numbers and create a false report outside the company’s Web site, Ms. Puls said.


At this point, please read the following guides on how to use your browser's developer tools -- the preferred browser is Chrome, though all modern browsers share the same feature set:

- Inspecting the Web with Chrome's DevTools http://www.compjour.org/tutorials/intro-to-the-web-inspector/
- Elements of a Webpage http://www.compjour.org/tutorials/elements-of-a-webpage/
- The Styles of a Webpage
 http://www.compjour.org/tutorials/styles-of-a-webpage/
- Watching Traffic with the Network Panel http://www.compjour.org/tutorials/watching-traffic-network-panel/


The HTTP GET method
===================

In Python, we're accustomed to using the ``get()`` method of the ``requests`` package. That method wasn't named arbitrarily, but of course maps to the actual name of the ``GET`` method as it exists in HTTP:

.. code-block:: python

    import requests
    requests.get('http://www.example.com')





