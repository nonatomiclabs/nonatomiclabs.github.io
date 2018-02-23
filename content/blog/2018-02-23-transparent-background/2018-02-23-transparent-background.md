Title: How to Make an Image's Background Transparent?
Date: 2018-02-23
Category: Image Processing
Summary: Learn how to use ImageMagick to adjust an image's background

You probably have already downloaded once an image with a white background, such as this one (the grey area around the logo just serves the purpose of seeing the white background).

<figure class="figure">
  <img src="./logo-white.png" alt="Logo with white background" style="padding: 20px; background:rgb(222, 222, 222); border-radius: 5px;"/>
  <figcaption class="figure-caption">Logo with white background</figcaption>
</figure>

For a number of reasons, one could want to have the same image with a transparent background. Luckily, [ImageMagick](http://imagemagick.org/script/index.php) has our back covered once more.

If you haven't already, install ImageMagick:

~~~
brew update && brew install imagemagick
~~~

<div class="alert alert-info" role="alert">
  <h4 class="alert-heading">Info</h4>
  Even though installed as <code>imagemagick</code>, there is no <code>imagemagick</code> command. Instead, <a href="https://imagemagick.org/script/command-line-tools.php">many separate commands</a> are defined for different use cases. Today, we'll use the <code>convert</code> command.
</div>

With ImageMagick installed, the easiest way to remove the white background is to use the following command:

~~~
convert test.png -transparent white transparent.png
~~~

The command is very simple: we pass an input and output files and the [`-transparent` option](https://imagemagick.org/script/command-line-options.php#transparent) is used to select the color we want to make transparent which can be passed as a color name or in hex/RGB format. Of course, you should choose an output format which handles transparency, such as PNG. The input can be in any format though.

Trying this command with our image from above gives the following. This looks fine, however if we look more closely we'll see that not all white parts have been removed.

<div class="container">
  <div class="row">
    <div class="col-xs-12 col-md-6">
      <figure class="figure">
        <img src="./logo-transparent1.png" alt="Logo with transparent background" style="padding: 20px; background:rgb(222, 222, 222); border-radius: 5px;"/>
        <figcaption class="figure-caption">Logo with transparent background</figcaption>
      </figure>
    </div>

    <div class="col-xs-12 col-md-6">
      <figure class="figure">
        <img class="figure-img img-fluid rounded" src="./logo-transparent1-detail.png" alt="Close-up of the logo with transparent background" style="padding: 20px; background:rgb(222, 222, 222); border-radius: 5px;"/>
        <figcaption class="figure-caption">Close-up of the logo</figcaption>
      </figure>
    </div>
  </div>
</div>

The `-fuzz` option can help us here. It simply matches colors that are within *x* percents of the intensity of the target color. In most cases, 2% is a reasonable value.

~~~
convert test.png -fuzz 2% -transparent white transparent.png
~~~

Voilà!

<div class="container">
  <div class="row">
    <div class="col-xs-12 col-md-6">
      <figure class="figure">
        <img src="./logo-transparent2.png" alt="Logo with transparent background" style="padding: 20px; background:rgb(222, 222, 222); border-radius: 5px;"/>
        <figcaption class="figure-caption">Logo</figcaption>
      </figure>
    </div>

    <div class="col-xs-12 col-md-6">
      <figure class="figure">
        <img class="figure-img img-fluid rounded" src="./logo-transparent2-detail.png" alt="Close-up of the logo with transparent background" style="padding: 20px; background:rgb(222, 222, 222); border-radius: 5px;"/>
        <figcaption class="figure-caption">Close-up</figcaption>
      </figure>
    </div>
  </div>
</div>
