INSTRUCTIONS
=============

1. Go to this gist: `demo_create_movie_sequence.py`_.

2. Instructions on the FFMPEG_ syntax to make an MP4 movie from a sequence of images come from `this website`_.

3. MP4 movie of MCMC demo:

   .. code-block:: console

      python3.7 demo_create_movie_sequence.py --prefix=img --output="mcmc_images.mp4" --dirname="mcmc_animation_images" --fps=10

   Open ``mcmc_images.mp4`` with a video viewer. This is 10 frames per second.

4. MP4 movie of cumulative COVID-19 cases in continental United States:

   .. code-block:: console

      python3.7 demo_create_movie_sequence.py --prefix="covid19_conus_cases_04072020." --output="covid19_conus_cases_04072020.mp4" --dirname=--dirname="covid19_conus_cases_04072020_imagefiles" --fps=5

   Open ``covid19_conus_cases_04072020.mp4`` with a video viewer. This is 5 frames per second.
      
.. _`demo_create_movie_sequence.py`: https://gist.github.com/tanimislam/406a1379e746c9882c101f656a6da949
.. _FFMPEG: https://ffmpeg.org
.. _`this website`: https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/
