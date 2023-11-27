import re

cd_re = re.compile("\$ cd ([\w]+|/|\.\.)")
ls_re = re.compile("\$ ls")
file_re = re.compile("([\d]+) ([\w]+)")
dir_re = re.compile("dir ([\w]+)")

class FakeFile:
    def __init__(self, name, size=0):
        self.name = name
        self.parent = None
        self.contents = {}
        self.size = size

    def AddFile(self, f):
        self.contents[f.name] = f
        f.parent = self

    def Size(self):
        size = self.size
        for name in self.contents.keys():
            size += self.contents[name].Size()
        return size

    def ChangeDir(self, target):
        if target == "/":
            if self.parent == None:
                return self
            else:
                return self.parent.ChangeDir("/")
        elif target == "..":
            return self.parent
        else:
            return self.contents[target]

    def AllDirs(self):
        dirs = []
        for name in self.contents.keys():
            nested_dirs = self.contents[name].AllDirs()
            for _dir in nested_dirs:
                dirs.append(_dir)
        if len(self.contents) > 0:
            dirs.append(self)
        return dirs

def LoadFilesystem(lines):
    root = FakeFile("/")
    current_dir = root
    for line in lines:
        matches = cd_re.match(line)
        if matches:
            current_dir = current_dir.ChangeDir(matches[1])
            continue
        matches = ls_re.match(line)
        if matches:
            continue
        matches = file_re.match(line)
        if matches:
            current_dir.AddFile(FakeFile(matches[2], size=int(matches[1])))
            continue
        matches = dir_re.match(line)
        if matches:
            current_dir.AddFile(FakeFile(matches[1]))
            continue
        raise Exception("Unmatched line: %s" % (line))
    return root
