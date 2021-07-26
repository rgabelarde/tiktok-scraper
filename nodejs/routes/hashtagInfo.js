const express = require("express");
const router = express.Router();

const { getHashtagInformation } = require("../controllers/scraperController");

// @route GET /hashtag/:hashtag
// @description Route to get all albums associated with hashtag
// @access Public
router.get("/:hashtag", getHashtagInformation);

module.exports = router;
