INSTRUCTIONS
=============

1. Go to these locations:

   a. showing Musicbrainz_ getting metadata (given an artist, all the albums + all songs of artist): `howdy.music.music.MusicInfo.get_music_metadata <get_music_metadata_>`_

   b. showing choose the correct YouTube clip: `howdy.music.music.youtube_search <youtube_search_>`_
      
   c. showing part of downloading from `youtube-dl`_: `howdy.music.music.get_youtube_file <get_youtube_file_>`_

2. ``howdy_music_songs`` documentation at `this website`_.
      
3. Show animation of getting songs, ``plex_music_songs_download_artist_songs.mp4``, with video viewer.

4. Show how to get ``All I Need`` by ``Air``

   .. code-block:: console

      howdy_music_songs -a Air -s "All I Need" --musicbrainz

   Which can take a bit of time.
   
.. _MusicBrainz: https://musicbrainz.org
		   
.. _`get_music_metadata`: https://github.com/tanimislam/howdy/blob/874627024f0aad9bbf9cad97b5e23f2ba9fb8437/howdy/music/music.py#L412

.. _`youtube_search`: https://github.com/tanimislam/howdy/blob/874627024f0aad9bbf9cad97b5e23f2ba9fb8437/howdy/music/music.py#L896

.. _`youtube-dl`: https://rg3.github.io/youtube-dl

.. _`this website`: https://tanimislam.github.io/howdy/howdy-music/cli_tools/howdy_music_cli.html?highlight=howdy_music_songs#howdy-music-songs

.. _`get_youtube_file`: https://github.com/tanimislam/howdy/blob/874627024f0aad9bbf9cad97b5e23f2ba9fb8437/howdy/music/music.py#L856
