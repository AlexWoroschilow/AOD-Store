import re
import os
import glob
import shutil
from subprocess import Popen
from subprocess import PIPE

stdin = ""
stdout = ""


class DependencyCalculator:
    collection = []

    def get_dependencies(self, package=None):
        if package is None: return None

        self.collection.append(package)
        process = Popen("apt-cache depends {}".format(package), shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

        for index, line in enumerate(process.stdout.readlines()):
            line = line.decode('utf-8')
            line = line.strip("\n")

            match = re.match(r"[\w\s]*:[\s<]*([\w\d\-\_\.\:]*)[\s>]*", line)
            if match is None:
                continue

            package = match.group(1)
            if package in self.collection:
                continue

            self.collection.append(package)

        return self.collection

    def download(self, package=None):
        print("apt-get download {}".format(package))
        if package is None: return None

        process = Popen("apt-get download {}".format(package), shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
        return process.stdout.read()

    def get_downloaded(self):
        for name in glob.glob('*.deb'):
            yield name

    def unpack(self, package=None, destination='./build'):
        if package is None: return None
        process = Popen("dpkg-deb -x {} {}".format(package, destination),
                        shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)

        return process.stdout.read()

    def merge(self, build='./build'):

        libs = '{}/usr/lib'.format(build)
        if os.path.exists(libs) and os.path.isdir(libs):
            print(os.system('cp -r {}/* {}/lib'.format(libs, build)))
            shutil.rmtree(libs)

        bins = '{}/usr/bin'.format(build)
        if os.path.exists(bins) and os.path.isdir(bins):
            os.system('cp -r {}/* {}/bin'.format(bins, build))
            shutil.rmtree(bins)

        bins = '{}/usr/sbin'.format(build)
        if os.path.exists(bins) and os.path.isdir(bins):
            os.system('cp -r {}/* {}/bin'.format(bins, build))
            shutil.rmtree(bins)


test = DependencyCalculator()

# for package in test.get_dependencies("mc"):
#     print('{} downloading...'.format(package))
#     test.download(package)
#
for package in test.get_downloaded():
    print('{} extracting...'.format(package))
    test.unpack(package)

test.merge()
