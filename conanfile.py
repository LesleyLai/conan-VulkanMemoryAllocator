import os

from conans import ConanFile, tools


class VulkanmemoryallocatorConan(ConanFile):
    name = "VulkanMemoryAllocator"
    version = "2.2.0"
    license = "MIT"
    author = "Lesley Lai lesley@lesleylai.info"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Vulkanmemoryallocator here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        self.run("git clone https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git")
        # tools.download("url", "file.zip")
        # tools.unzip("file.zip" )

    def package(self):
        self.copy("VulkanMemoryAllocator/src/vk_mem_alloc.h", dst="include", keep_path=False)
