#!/usr/bin/python3
import os,shutil,glob
import argparse

parser = argparse.ArgumentParser(description="HEIC görüntülerini istenilen kalitede JPEG formatına çevirir.")
parser.add_argument('-g','--quality',default=80, help="Varsayılan Kalite 80")
args =  parser.parse_args()

for infile in glob.glob("*.HEIC"):
    dosya, ext = os.path.splitext(infile)
    klasor = "HEIC"
    os.makedirs(klasor, exist_ok=True)
    command = f"convert {dosya}.heic -quality {args.quality} {dosya}_q{args.quality}.jpg"
    os.system(command)
    shutil.move(infile,klasor)
    print(f"Bitti... {dosya}.HEIC -> {dosya}_q{args.quality}.jpg")
