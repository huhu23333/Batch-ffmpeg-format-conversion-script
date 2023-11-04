import os
import sys

ffmpegPath = "ffmpeg"



if __name__ == "__main__":
    if "-sp" in sys.argv:
        inputPath = input("inputPath:")
        outputPath = input("outputPath:")
    elif "-sp_io" in sys.argv:
        inputPath = "./input/"
        outputPath = "./output/"
    else:
        print("!!!Working in the current path!!!")
        inputPath = "./"
        outputPath = "./"
    fileList = os.listdir(inputPath)
    inputFormat = input("inputFormat:")
    outputFormat = input("outputFormat:")

    otherArgv = ""

    if "-ow_n" in sys.argv:
        otherArgv += "-n "
    elif "-ow_y" in sys.argv:
        otherArgv += "-y "

    for fileName in fileList:
        if fileName[-len(inputFormat):] == inputFormat:
            #os.system(ffmpegPath+" -i \""+inputPath+fileName+"\" "+otherArgv+"\""+outputPath+fileName[:-len(inputFormat)]+outputFormat+"\"")
            os.system("{} -i \"{}\" {}\"{}\"".format(ffmpegPath,inputPath+fileName,otherArgv,outputPath+fileName[:-len(inputFormat)]+outputFormat))
