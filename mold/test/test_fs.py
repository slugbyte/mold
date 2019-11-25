import os
import mold.util.fs as fs

TEMP_DIR = __file__.replace('test_fs.py', 'temp')

class TestFS:
    def setup_method(self, test_method):
        fs.mkdir(TEMP_DIR)

    def teardown_method(self, test_method):
        fs.rimraf(TEMP_DIR)

    def test_exists(self):
        assert  fs.exists(TEMP_DIR)
        assert not fs.exists(TEMP_DIR + '/not-existing-file')

    def test_isdir(self):
        assert fs.is_dir(TEMP_DIR)
        fs.mkfile(TEMP_DIR + '/plainfile')
        assert not fs.is_dir(TEMP_DIR + '/plainfile')

    def test_create_mv_and_destory_file(self):
        path = TEMP_DIR + '/test_makfile'
        fs.mkfile(path)
        assert fs.exists(path)
        assert not fs.is_dir(path)
        fs.mv(path, path + 'renamed')
        assert not fs.exists(path)
        assert fs.exists(path + 'renamed')
        assert not fs.is_dir(path  + 'renamed')
        fs.rm(path + 'renamed')
        assert not fs.exists(path)

    def test_create_and_destory_dir(self):
        dirpath = TEMP_DIR + '/test_mkdir'
        filepath = TEMP_DIR + '/test_mkdir/cool'
        fs.mkdir(dirpath)
        fs.mkfile(filepath)
        assert fs.exists(dirpath)
        assert fs.is_dir(dirpath)
        fs.rimraf(dirpath)
        assert not fs.exists(dirpath)

    def test_dirname_and_basename(self):
        assert fs.basename('/hello/world') == 'world'
        assert fs.dirname('/hello/world') == '/hello'

    def test_copy(self):
        path = TEMP_DIR + '/test_copy_file'
        f = open(path, 'w')
        f.write('test_copy text')
        f.close()
        fs.copy(path, path + '_copy')
        assert fs.exists(path)
        assert fs.exists(path + '_copy')
        one = open(path, 'r')
        two = open(path + '_copy', 'r')
        assert one.read() == two.read()

    def test_link(self):
        a_path = TEMP_DIR + '/test_link_file'
        with open(a_path, 'w') as f:
            f.write('test_copy text')
        b_path = a_path + '_link'
        fs.link(a_path, b_path)
        with open(b_path, 'w') as f:
            f.write('boom')
        with open(a_path, 'r') as a, open(b_path, 'r') as b:
            assert a.read() == b.read()

    def test_force_link(self):
        a_path = TEMP_DIR + '/force_link_test_a'
        b_path = TEMP_DIR + '/force_link_test_b'
        fs.mkfile(a_path)
        fs.mkfile(b_path)
        fs.force_link(a_path, b_path)
        with open(b_path, 'w') as f:
            f.write('boom')
        with open(a_path, 'r') as a, open(b_path, 'r') as b:
            assert a.read() == b.read()
    
    def test_unpack_tarball(self): 
        os.chdir(TEMP_DIR)
        fs.unpack_tarball(__file__.replace('test_fs.py', 'assets/tar_test.tar.gz'))
        path = TEMP_DIR + '/tar_test' 
        assert fs.exists(path)
        assert fs.is_dir(path)
        assert fs.exists(path + '/1.txt')
        assert fs.exists(path + '/2.txt')
        assert fs.exists(path + '/3.txt')
