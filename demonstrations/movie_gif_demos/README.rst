INSTRUCTIONS
=============

1. Go to these locations in `nprstuff.core.convert_image <convert_image_>`_.

   a. mp4togif: `nprstuff.core.convert_image.mp4togif <mp4togif_>`_

   b. youtube2gif: `nprstuff.core.convert_image.youtube2gif <youtube2gif_>`_

2. Lower level FFMPEG_ command comes from `this website`_.
      
3. MP4 to animated GIF:

   .. code-block:: console

      convertImage movie -f covid19_conus_cases_04072020.mp4

   Creates animated GIF ``covid19_conus_cases_04072020.gif``, open in browser.
      
4. YouTube Clip to GIF:

   .. code-block:: console
   
      convertImage youtube -u "https://www.youtube.com/watch?v=R-pmYwr8zbU" -o "lucas_bros.gif" -q high

   Creates animated GIF ``lucas_bros.gif``, open in browser.


.. _`convert_image`: https://github.com/tanimislam/nprstuff/blob/master/nprstuff/core/convert_image.py

.. _mp4togif: https://github.com/tanimislam/nprstuff/blob/b1a27810eeedb1e742895127f57287e838ac576e/nprstuff/core/convert_image.py#L154

.. _youtube2gif: https://github.com/tanimislam/nprstuff/blob/b1a27810eeedb1e742895127f57287e838ac576e/nprstuff/core/convert_image.py#L129

.. _`this website`: http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html

.. _FFMPEG: https://ffmpeg.org
