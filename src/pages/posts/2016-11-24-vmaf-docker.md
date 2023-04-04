---
layout: ../../layouts/MarkdownPostLayout.astro
title: "Netflix's VMAF in a Travis CI Pipeline With Docker"
date: 2016-12-03
tags: ["Linux"]
# summary: "A shrinked version of Netflix's VMAF Docker image to run easily in your CI pipeline"
---
# The VMAF quality metric

My main project currently is about improving certain points of the x265 implementation of the HEVC encoder.  
Therefore, quality metrics are particularly important (and even more given that my improvements target only constant bitrate mode).  
After reading [this](http://techblog.netflix.com/2016/06/toward-practical-perceptual-video.html) article from Netflix's techblog about their new VMAF quality metric, I decided to give it a try.

The great thing is that, thanks to [Leandro Moreira](https://github.com/Netflix/vmaf/pull/33) (who actually recently wrote a nice [article](https://leandromoreira.com.br/2016/10/09/how-to-measure-video-quality-perception) article about video quality metrics), [there](https://github.com/Netflix/vmaf/blob/master/Dockerfile) is a Dockerfile for the project.

However, the Dockerfile installs dependencies for each and every one feature of the project, resulting in a Docker image of over 3GB.  
With the help of my one-liner to get the download size of a package prior to downloading it published [recently]({filename}2016-11-23-packages-size.md), I could identify which packages take most of the space (namely `python-pandas` and `python-sympy`).

So I created a new version of the Docker image, which packs only the stuff necessary to compute the VMAF. It now weighs around 1GB and you can find on Docker hub at [this address](https://hub.docker.com/r/nonatomiclabs/vmaf/)! 🎉

# Use it in your Travis CI pipeline

You can use my lighter VMAF image in your Travis CI pipeline by applying the following steps:

1. Enable Docker in your Travis build, by adding those lines to your Docker file (see the [docs](https://docs.travis-ci.com/user/docker/) for more details)

        sudo: required
        services:
          - docker

2. Pull the VMAF Docker image in the `before_install` or `install` step

        before_install:
          - docker pull nonatomiclabs/vmaf:1.0

3. Run the Docker image

        docker run --rm -v /folder/with/video/resources:/tmp nonatomiclabs/vmaf:1.0 run_vmaf yuv420p 1920x1080 /tmp/ref.yuv /tmp/comp.yuv --out-fmt json

Enjoy!
