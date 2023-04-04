---
layout: ../../layouts/MarkdownPostLayout.astro
title: "Stupid Questions #1: Base64 Encoding"
date: 2018-02-04
tags: ["Stupid Questions", "tag"]
summary: "A very short introduction to Base64 Encoding"
---
<div class="alert alert-success" role="alert">
  <p style="text-align: justify;">
  This post is the first in a new category called "Stupid Questions". These will be short posts, answering questions with a simple but not always obvious answer. These questions are the kind of questions one (me included) could be ashamed to ask because they seem stupid, hence the title of this category!
  </p>
</div>

While reading recently about the new features of Python 3.6, I stumbled upon the [documentation](https://docs.python.org/3/library/secrets.html#secrets.token_urlsafe) of the brand new `secrets` module where we can find this sentence:

> The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.

Therefore, the question for today is the following: *why does a byte results in 1.3 characters with Base64 encoding?*

Put simply, Base64 is just a way to encode binary data as text. Instead of writing 0s and 1s, we write ASCII characters. As the name suggests, the *alphabet* used by Base64 consists of 64 symbols.

The exact list of symbols varies from one implementation to another, but the idea behind how they are chosen is to have as *universal* and *printable* data. That decreases the risk of encoding-related data corruption during the transmission of a message, and explains why emails are often Base64-encoded. Thus, most Base64 implementations use `A-Z`, `a-z` and `0-9` as the first 62 values.

We now know that Base64 uses 64 symbols and <del>surprisingly</del> 64 = 2<sup>6</sup>. Each one of the 64 symbols of Base64 encoding therefore represents a unique combination of 6 bits. Thus, if each character represents 6 bits, 1.3 characters are needed to represent a byte (*8* bits)! *QED*.

![Illustration of the Base64 encoding of 2 bytes](/images/2018-02-04-base64_encoding.png)