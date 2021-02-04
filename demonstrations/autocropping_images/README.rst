INSTRUCTIONS
=============

1. Go to these locations:

   a. autocropping lossy images: `nprstuff.core.autocrop_image.autocrop_image <autocrop_image_>`_

   b. autocropping PDFs: `nprstuff.core.autocrop_image.crop_pdf_singlepage <autocrop_image_pdf_>`_

2. Cropping a PNG image:

   .. code-block:: console

      autoCropImage --input=iwanttobelieve_uncropped.png --output=iwanttobelieve_cropped.png

   Compare ``iwanttobelieve_uncropped.png`` and ``iwanttobelieve_cropped.png`` in a browser.
      
3. Cropping a PDF image:

   .. code-block:: console

      autoCropImage --input=cumulative_plot_emission_uncropped.pdf --output=cumulative_plot_emission_cropped.pdf

   Compare ``cumulative_plot_emission_uncropped.pdf`` and ``cumulative_plot_emission_cropped.pdf`` in a PDF viewer.
      

.. _`autocrop_image`: https://github.com/tanimislam/nprstuff/blob/fd23d5057d91be019a517534816788a253c71b3a/nprstuff/core/autocrop_image.py#L30

.. _`autocrop_image_pdf`: https://github.com/tanimislam/nprstuff/blob/fd23d5057d91be019a517534816788a253c71b3a/nprstuff/core/autocrop_image.py#L219
