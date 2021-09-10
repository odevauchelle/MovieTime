# MovieTime

Two convenience functions to read the metadata of a movie.

## Simple example

To read the metadata of `movie.mov`:
```python
metadata = GetMovieMetadata( movie.mov )
```
The `metadata` dictionary stores the output:
```python
for item in metadata.items() :
        print(*item)
```
```console
>>> ExifTool Version Number 11.16
File Name background.mov
...
Image Size 1280x720
Megapixels 0.922
Rotation 0
```

## Time data

```python
for item in GetMovieTime( metadata ).items() :
        print(*item)
```
```console
>>> file_creation_time 2021-09-07T16:07:57+02:00
duration 6.28
FPS 50
```

## Requirements

- [ExifTools](https://exiftool.org/)
