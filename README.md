A Pythonista script to save web pages as markdown files in Dropbox.

In order to use this script, you need to do the following steps:

* register a new app with Dropbox;
* get a app key and secret
* create two files in the project folder, APP_KEY and APP_SECRET containing the app key and secret

 This is required for development purposes only. Once you want to run the script in Pythonista, you can
 hardcode the APP_KEY and APP_SECRET in the script itself.

I've included HTMLParser.py and markupbase.py because I've found some bugs in them for some URLs
(for example [here][1] and [here][2]) and at some point I'd like to attempt to fix them.

I use Aaron Swartz's excellent html2text script which converts html to markdown. Original repo for
it is [here][3].

[1]: http://strobist.blogspot.ch/2013/03/in-depth-new-fujifilm-x100s.html
[2]: http://www.cocoanetics.com/2013/03/moving-from-svn-to-git/
[3]: https://github.com/aaronsw/html2text