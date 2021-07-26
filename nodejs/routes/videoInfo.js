const express = require("express");
const router = express.Router();

const { getVideosFromHashtag } = require("../controllers/scraperController");

// @route GET /video/:hashtag
// @description Route to get all albums associated with hashtag
// @access Public
router.get("/:hashtag", getVideosFromHashtag);

module.exports = router;
