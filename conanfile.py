from conans import ConanFile, CMake
from conans import tools
from conans.errors import ConanInvalidConfiguration

class PocoTimerConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   options  = {"shared": [True, False]}
   generators = "cmake", "gcc"
   default_options = "shared=False"
   exports_sources = "cmake"

   def source(self):
      self.run("git clone https://github.com/kvmkrao/jenkins.git"
      self.run("cd jenkins ")

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
