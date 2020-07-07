#!/usr/bin/env python3

"""
I developed this Python CLI script to demonstrate creating an MP4 movie from an image sequence.
I follow instructions from https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video. I make an MP4 movie that is 5 FPS with psychovisual quality of 25.
"""
import os, sys, numpy, subprocess, glob, re, logging, time
from PIL import Image
from distutils.spawn import find_executable
from argparse import ArgumentParser

def create_movie_from_sequence( prefix, output_file_name, dirname = os.getcwd( ), fps = 5 ):
    """
    Creates an MP4 movie from a sequence of PNG images. The output file name must end in .mp4.

    :param str prefix: the beginnning base name of all the PNG images. If `foo` is the prefix, then will look for images that are like `foo0001.png`, `foo0002.png` and so forth. To make life simpler, the prefix *MUST* be alphanumeric.
    :param str output_file_name: the name of the output file. Must end in .mp4.
    :param str dirname: optional argument. The directory that contains the image sequence. Default is the current working directory.
    :param int fps: frames per second. Default is 5.
    :returns: `True` if successful, `False` otherwise.
    :rtype: bool
    """
    time0 = time.time( )
    assert( os.path.isdir( dirname ) ) # is a directory
    assert( os.path.basename( output_file_name ).endswith( '.mp4' ) ) # ends with mp4
    assert( re.match( '^[a-zA-Z]+', prefix ) is not None ) # alphanumeric
    assert( find_executable( 'ffmpeg' ) is not None )
    assert( fps >= 1 ) # fps must be positive
    ffmpeg_exec = find_executable( 'ffmpeg' )
    #
    ## now sequence of images
    sorted_filenames = sorted(
        filter(lambda fname: re.match('.*[0-9]+\.png', os.path.basename( fname ) ) is not None and
               os.path.basename( fname ).startswith( prefix ),
               glob.glob( os.path.join( dirname,'%s*.png' % prefix ) ) ) )
    if len( sorted_filenames ) == 0:
        print( 'ERROR, COULD FIND NO IMAGE SEQUENCE.' )
        return False
    def is_divis_2( fname ):
        img = Image.open( fname )
        if img.size[0] % 2 != 0: return False
        if img.size[1] % 2 != 0: return False
        return True
    try:
        assert(all(filter(is_divis_2, sorted_filenames))) # all widths and heights div by 2
    except:
        print( "ERROR, NOT ALL IMAGES HAVE WIDTHS + HEIGHTS DIVISIBLE BY 2.")
        return False
    
    #
    ## 
    num_base_10 = 1 + int( numpy.log10(len(sorted_filenames)))
    sequence_ffmpeg = '%%%02dd' % num_base_10 # this is tricky!
    input_ffmpeg_image_string = '%s%s.png' % ( os.path.join( dirname, prefix ), sequence_ffmpeg )
    logging.info( 'got here, %s.' % input_ffmpeg_image_string )
    #
    ## now run the ffmpeg command
    command_to_process =  [
        ffmpeg_exec, '-y', '-r', '%d' % fps, '-f', 'image2', '-i', input_ffmpeg_image_string,
        '-vcodec', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p',
        output_file_name ]
    logging.info( 'COMMAND TO RUN: %s.' % ' '.join( command_to_process ) )
    proc = subprocess.Popen( command_to_process, stdout = subprocess.PIPE,
                            stderr = subprocess.STDOUT )
    stdout_val, stderr_val = proc.communicate( )
    logging.info( 'STDOUT_MESSAGE.' )
    logging.info( '%s\n' % stdout_val )
    logging.info( 'TOOK %0.3f SECONDS TO RUN TO COMPLETION.' % (
        time.time( ) - time0 ) )

if __name__=='__main__':
    parser = ArgumentParser( )
    parser.add_argument( '--prefix', dest='prefix', type=str, required = True,
                        help = 'The prefix to the sequence of PNG images.' )
    parser.add_argument( '--output', dest='output', type=str, required = True,
                        help = 'The name of the MP4 output file.' )
    parser.add_argument( '--dirname', dest='dirname', type=str, default = os.getcwd( ),
                        help = 'The directory containing the image sequence. Default is CWD.')
    parser.add_argument( '--fps', dest='fps', type=int, default = 5,
                        help = 'Frames per second of movie. Default is 5.' ) 
    parser.add_argument( '--info', dest='do_info', action='store_true', default = False,
                        help = 'If chosen, then print out INFO debug logging.' )
    args = parser.parse_args( )
    logger = logging.getLogger( )
    #
    if args.do_info: logger.setLevel( logging.INFO )
    status = create_movie_from_sequence(
        args.prefix, args.output, dirname = args.dirname, fps = args.fps )
    
