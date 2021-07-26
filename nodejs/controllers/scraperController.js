// Credits to @drawrowfly for scraper + example codes
// https://github.com/drawrowfly/tiktok-scraper

const axios = require("axios");
const express = require("express");
const mongoose = require("mongoose");
const TikTokScraper = require("tiktok-scraper");

const getVideosFromHashtag = async (req, res) => {
  try {
    const hashtag = req.params.hashtag;
    const posts = await TikTokScraper.hashtag(hashtag, {
      number: 10000,
      sessionList: ["sid_tt=58ba9e34431774703d3c34e60d584475;"],
    });
    console.log(posts);
    // fs.writeFileSync("output.json", posts.collector);
    res.status(200).json({ posts: posts.collector });
  } catch (error) {
    console.log(error);
    res
      .status(400)
      .json({ error: "Could not find videos associated with hashtag" });
  }
};

// Get single hashtag information: Number of views and etc
// input - HASHTAG NAME
// options - not required
const getHashtagInformation = async (req, res) => {
  try {
    const hashtag = req.params.hashtag;
    const hashtagMeta = await TikTokScraper.getHashtagInfo(hashtag, {});
    console.log("NEW" + hashtagMeta);
    res.status(200).json({ hashtagMeta: hashtagMeta });
  } catch (error) {
    console.log(error);
    res.status(400);
  }
};

module.exports = {
  getVideosFromHashtag,
  getHashtagInformation,
};
