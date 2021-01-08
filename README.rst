Python for Quick, Useful Multimedia Manipulation: Anecdotes from a Python Programmer
=====================================================================================

One of Python's many killer features is that a programmer can organically create snippets of code, and coherently join them into larger collections of module code. In this presentation, I describe and demonstrate relatively simple Python tools -- for image, video, and audio manipulation -- that I use every day at work and outside work.

* automatically cropping out whitespace in images (surprisingly easy to do).

* creating movies from a sequence of generated images.

* conversion of movie clips, either files or YouTube clips, into animated GIFs (useful where the online service does not allow for video animations from movie files, such as GitHub_ or `Read the Docs`_).

If there's time or interest, I can even describe and demonstrate how to retrieve and label music you might find, all within Python.

Demonstrations live in the ``demonstrations`` subdirectory, each demonstration is its own directory within ``demonstrations``, and each demonstration has its own ``README.rst``. Here are the four directories with description.

1. ``autocropping_images``: autocropping a PNG image and a PDF image.

2. ``movie_image_demos``: converting a sequence of images into an MP4 file.

3. ``movie_gif_demos``: converting an MP4 file and a YouTube clip into animated GIFs.

4. ``making_music_youtube``: using a tool, `plex_music_songs`_, that takes metadata from MusicBrainz_ and the YouTube clip using `youtube-dl`_, into an M4A file.

.. _GitHub: https://github.com
.. _`Read the Docs`: https://www.readthedocs.io
.. _CloudConvert: https://cloudconvert.com
.. _`plex_music_songs`: https://plexstuff.readthedocs.io/plex-music/cli_tools/plex_music_cli.html?highlight=plex_music_songs#plex-music-songs
.. _MusicBrainz: https://musicbrainz.org
.. _`youtube-dl`: https://rg3.github.io/youtube-dl
