import subprocess
from datetime import datetime

def GetMovieMetadata( filename ) :
    '''
    Get movie metadata. Based on exiftools.

    metadata = GetMovieMetadata( filename )

    Arguments:
    filename (string): Path and name of the movie file.

    Output:
    metadata (dict): The movie metadata.
    '''

    subprocess_command = [ 'exiftool', filename ]
    stdout = subprocess.run( subprocess_command, capture_output=True ).stdout.decode()

    metadata = {}

    for line in stdout.split('\n')[:-1] :

        key, value = line.split( ':', 1 )
        metadata[ key.strip() ] = value.strip()

    return metadata

def GetMovieTime( metadata = None, filename = None ) :
    '''
    Extract interesting times from movie metadata. Based on exiftools.

    time_metadata = GetMovieTime( metadata = None, filename = None )

    Arguments:
    medadata (dict): The movie metadata (output of exiftools).
    filename (string): Path and name of the movie file.
    '''

    p = {}

    if metadata is  None :
        metadata = GetMovieMetadata( filename )

    p['file_creation_time'] = datetime.strptime( metadata[ 'File Modification Date/Time' ], "%Y:%m:%d %H:%M:%S%z" ).isoformat()
    p['duration'] = metadata[ 'Duration' ].split(' ')[0]
    p['FPS'] = metadata[ 'Video Frame Rate' ]

    return p

if __name__ == '__main__' :

    # import cv2 as cv

    #####################
    #
    # Parameters
    #
    #####################

    p = dict(
        data_path = '/run/user/1000/gvfs/smb-share:server=dfgnas3.local,share=devauchelle2/sauvegarde_manip_thermophorese/manip_2/',
        background_movie_file = 'background.mov',
        )

    metadata = GetMovieMetadata( p['data_path'] + p['background_movie_file'] )

    for item in metadata.items() :
        print(*item)

    print('---------------------')

    for item in GetMovieTime( metadata ).items() :
        print(*item)
    ######################
    #
    # Load movie & extract background
    #
    ######################

    # movie = TinyTag.get( p['data_path'] + p['background_movie_file'] )
    # sub_process_command = [ 'ffmpeg', '-i', p['data_path'] + p['background_movie_file'] ]

    # print( subprocess.run( sub_process_command, capture_output = True ) )

    # print( datetime.fromtimestamp( getctime( p['data_path'] + p['background_movie_file'] ) ) )
    # movie = cv.VideoCapture( p['data_path'] + p['background_movie_file'] )

    # for item in cv.__dict__.items() :
    #     print(*item)

    # for item in MovieTime( p['data_path'] + p['background_movie_file'] ).items() :
    #     print(*item)
