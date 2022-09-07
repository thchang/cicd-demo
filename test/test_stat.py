def test_os_path_exists():
    """ Test whether the os.path.exists() function works on GH Actions. """

    import os

    fp = open("test file.txt", "w")
    fp.write("Testing 123...")
    fp.close()

    assert(os.path.exists("test file.txt"))
