import html2text
from dropbox import client, rest, session
import codecs
import os.path
import pickle

def main():
    page = html2text.html2text("http://furbo.org/2013/04/11/logging-with-xcode-breakpoints/")

    APP_KEY = open('APP_KEY', 'r').read();
    APP_SECRET = open('APP_SECRET', 'r').read();
    ACCESS_TYPE = 'app_folder'

    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    if os.path.exists('access_token_file'):
        access_token_file = open('access_token_file', 'r')
        access_token = pickle.load(access_token_file)
        access_token_file.close()
        sess.set_token(access_token.key, access_token.secret)
    else:
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
        print "url:", url
        print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
        raw_input()
        access_token = sess.obtain_access_token(request_token)

        access_token_file = open('access_token_file', 'w')
        pickle.dump(access_token, access_token_file, -1)
        access_token_file.close()

    my_file = codecs.open('test_upload.md', 'w', 'utf-8-sig')
    my_file.write(page)
    my_file.close()

    # now open the file for reading
    my_file2 = open('test_upload.md')
    myclient = client.DropboxClient(sess)
    response = myclient.put_file('test_upload.md', my_file2)
    print "uploaded: ", response
    my_file2.close()


if __name__ == "__main__":
    main()